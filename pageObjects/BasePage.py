from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def retry(func):
    """Decorator to retry up to 3 times if an exception is raised"""

    def function_wrapper(*args, **kwargs):
        max_retries = 3
        retry_count = 0
        while(retry_count <= max_retries):
            
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(("| %s in %s" % (type(e).__name__, func)) + "".join([("\n|  | %s" % x) for x in e.__str__().splitlines()]))
                if (retry_count == max_retries):
                    # Max retries -> re-raise the exception
                    print("| -> No more retry")
                    raise
                else:
                    retry_count += 1
                    print("| -> Retry (%d/%d)" % (retry_count, max_retries))

        return None

    return function_wrapper


class BaseLocator:
    """
    Base locator wrapping the locator strategy and value.
    Overload some operators for easier usage (locator addition, internal string formating, unpacking).
    To be attached as class attributes to BasePage (descriptor).
    """

    explicit_timeout = 15  # seconds
    implicit_timeout = 5

    def __init__(self, by, value_format):
        # The locator strategy
        self.__by = by

        # The value format to be used as format string for customizable locators with the __call__ operator overload
        self.__value_format = value_format 
        
        # Actual value of the locator to be used by the web driver
        # (initialized to __value_format in case there is no need for format placeholders replacement)
        self.__value = self.__value_format

        # The BaseLocator descriptor is meant to be used as a class attribute of the BaseLocator class.
        # The following attributes are bindings to the BasePage the Baselocator is attached to, they will be defined by __get__

        # The name of the BaseClass page the BaseLocator is class attribute of
        self.__page_name = None

        # The name of the BaseLocator as class attribute in the BasePage class
        self.__name = None

        # The driver to be used by the locator
        self.__driver = None

    
    def __get__(self, obj, objtype=None):
        # Identify parent BasePage class at first access
        if (self.__page_name is None):
            # Parent page name
            self.__page_name = objtype.__name__

            # Find out the element name among the parent BasePage class attributes
            for name, attr in objtype.__dict__.items():
                if (isinstance(attr, BaseLocator) and self is attr):
                    self.__name = name

        # Refresh the driver at each access
        self.__driver = obj.driver

        return self


    def __call__(self, *args):
        """Apply the arguments to the __value_format as a format string for __value"""
        self.__value = self.__value_format % args
        return self

    
    def __add__(self, other_str):
        """
        Create a new BaseLocator by adding the other_str string to the __value_format,
        resulting in a locator with the same __by but concatenated __value_format strings
        """
        return BaseLocator(self.__by, self.__value_format + other_str)


    def __radd__(self, other_str):
        """
        Create a new BaseLocator by adding the other_str string at the beginning of the __value_format,
        resulting in a locator with the same __by but concatenated __value_format strings
        """
        return BaseLocator(self.__by, other_str + self.__value_format)

    def __str__(self):
        return "%s.%s\n    <%s: \"%s\">" % (self.__page_name, self.__name, self.__by, self.__value)

    def __getitem__(self, key):
        """Unpack (__by, __value) to call webdriver find_element more concisely"""
        if key == 0:
            return self.__by
        elif key == 1:
            return self.__value
        else:
            raise IndexError

    @retry
    def send_keys(self, keys, clear=False):
        """
        Send the keys to the located element.
        The element is cleared before, if requested.
        """
        print("Send keys %s to %s" % (keys, self))
        print("    <url: \"%s\">" % self.__driver.current_url)
        if (clear):
            print("    Clear content")
            self.__driver.find_element(*self).clear()
        if (keys):
            self.__driver.find_element(*self).send_keys(keys)
        print("    => keys sent")
        return self # Return self to be able to chain the actions

    @retry
    def click(self):
        """Click on the located element."""
        print("Click %s" % self)
        print("    <url: \"%s\">" % self.__driver.current_url)
        self.__driver.find_element(*self).click()
        print("    => clicked")
        return self # Return self to be able to chain the actions

    @retry
    def is_displayed(self):
        """Check if the located element is displayed."""
        print("Is displayed %s" % self)
        print("    <url: \"%s\">" % self.__driver.current_url)
        is_displayed = self.__driver.find_element(*self).is_displayed()
        print("    => displayed: %s" % is_displayed)
        return is_displayed

    @retry
    def is_enabled(self):
        """Check if the located element is enabled."""
        print("Is enabled %s" % self)
        print("    <url: \"%s\">" % self.__driver.current_url)
        is_enabled = self.__driver.find_element(*self).is_enabled()
        print("    => enabled: %s" % is_enabled)
        return is_enabled

    @retry
    def get_text(self, wait_until_not_empty=False):
        """Get the text contained in the located element."""

        print("Get text %s" % self)
        print("    <url: \"%s\">" % self.__driver.current_url)
        
        if (wait_until_not_empty):
            print("    Waiting until not empty for %d s..." % self.explicit_timeout)
            class element_to_be_not_empty(object):
                def __init__(self, locator):
                    self.locator = locator

                def __call__(self, driver):
                    element = driver.find_element(*self.locator)   # Finding the referenced element
                    if element.text != "":
                        return element
                    else:
                        return False
            
            wait = WebDriverWait(self.__driver, self.explicit_timeout)
            element = wait.until(element_to_be_not_empty(self))
            text = element.text
            print("    => text: %s" % text)
            return text
        else:
            text = self.__driver.find_element(*self).text
            print("    => text: %s" % text)
            return text

    @retry
    def wait_until_visibility(self, visibility=True):
        """Wait until the element is visible (visibility=True) or invisble (visibility=False)."""
        print("Waiting until %s for %d s... %s" % ("visible" if visibility == True else "invisible", self.explicit_timeout, self))
        print("    <url: \"%s\">" % self.__driver.current_url)

        wait = WebDriverWait(self.__driver, self.explicit_timeout)
        
        element = None
        if (visibility):
            element = wait.until(EC.visibility_of_element_located((self.__by, self.__value)))
            print("    => visible")
        else:
            element = wait.until(EC.invisibility_of_element_located((self.__by, self.__value)))
            print("    => invisible")

        assert element is not None, "Element is not %s" % ("visible" if visibility == True else "invisible")

        return self # Return self to be able to chain the actions


class BasePage:
    """BasePage model to be composed of BaseLocators as class attributes."""

    def __init__(self, driver):
        self.driver = driver
