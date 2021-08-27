"""
WebAppUITestCase module
"""

import unittest
import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from testCases import variables as var
from pageObjects.PageLogin import PageLogin
from pageObjects.BasePage import BaseLocator


class WebAppUITestCase(unittest.TestCase):
    """
    Parent class to factorize setup and teardown for all test cases
    """

    login_profile = var.LoginProfiles.MEMBER # Default is MEMBER, can be overloaded in derived test classes
    implicit_timeout = 5  # Default implicit timeout to 5s, to be overloaded in derived test classes if needed
    do_login = True
    window_size = None  # Specify window size couple (x, y), None to maximize window (default value)
    start_date_time = datetime.datetime.now()
    start_time = time.time()  # script running start time
    browser = var.Browsers.chrome  # webbrowser to be used for a particular Test Class

    @classmethod
    def setUpClass(cls) -> None:
        print("")
        # Make sure the clock starts when the test setup is called and not when the class is imported
        cls.start_date_time = datetime.datetime.now()
        cls.start_time = time.time()
        print("Run started at: ", str(cls.start_date_time))
        print("-------------------------------------------------")
        print("Chrome Env Set Up")

        # Make sure we are able to open the Smood WebApp and login (if requested) before running the test
        # 5 attempts to reach Smood page, including the driver creation
        for i in range(1, 6):
            try:
                print("Setup attempt: %d/5" % i)

                if cls.browser == var.Browsers.chrome:
                    # Driver options & capabilities
                    chrome_options = Options()
                    chrome_options.headless = False
                    # Driver creation (on grid or locally)
                    cls.driver = webdriver.Chrome(executable_path="C:\\WebAppUITestProject\\drivers\\chromedriver", options=chrome_options)

                if cls.browser == var.Browsers.firefox:
                    options = FirefoxOptions()
                    cls.driver = webdriver.Firefox(executable_path="C:\\WebAppUITestProject\\drivers\\geckodriver")

                if cls.browser == var.Browsers.safari:
                    cls.driver = webdriver.Safari()

                cls.driver.implicitly_wait(cls.implicit_timeout)
                # Let the BaseLocator class know the current value of the implict wait when it needs to turn it off and back on...
                BaseLocator.implicit_timeout = cls.implicit_timeout
                if (not cls.window_size):
                    cls.driver.maximize_window()
                else:
                    cls.driver.set_window_size(cls.window_size[0], cls.window_size[1])
                
                # Go to smood URL (base on the current Testing environment)
                cls.driver.get(var.intBaseURL)
                time.sleep(1)

                # Login if requested
                if (cls.do_login):
                    # Login with the specified profile
                    PageLogin(cls.driver).login_with_profile(cls.login_profile)

            except Exception as e:
                print("Test setup exception !!!")
                print(e)

                # Close the current driver for the retry or test abortion
                cls.driver.quit()

                if (i < 5):
                    # Retry if this was not the last attempt
                    print("Retry setup")
                    continue
                else:
                    # Propagate the exception otherwise and abort the tests (tear down won't be run)
                    print("Unable to setup abort test")
                    raise
            else:
                # No need to retry
                break


    @classmethod
    def tearDownClass(cls) -> None:
        # cls.driver.close()
        cls.driver.quit()
        print("")
        print("Closed browser")
        print("-------------------------------------------------")
        print("Run finished at: ", str(datetime.datetime.now()))
        end_time = time.time()  # script running end time
        print("Run finished after: ", ((end_time - cls.start_time)/60), "Minutes")
