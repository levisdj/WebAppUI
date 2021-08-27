from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pageObjects.BasePage import BasePage, BaseLocator

default_wait_time = 15  # seconds


class PageHome(BasePage):
    container_user_profile =    BaseLocator(By.XPATH, "//*[@id='dropdownUserMenu']")
    button_show_user_profile =  container_user_profile + "/span"

    def get_user_profile_info(self):
        """Returns the first name (this is what is displayed from the webApp) of the connected user
                                                                        (as indicated in the UserProfile Class)."""

        # Show user profile
        self.button_show_user_profile.get_text(True)
        self.button_show_user_profile.click()       # This is not mandatory to do

        # Return first name and some other User Profile Param if we desire.
        name = self.button_show_user_profile.get_text()
        print("The logged user is %s" % name)

        return name

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, default_wait_time)
