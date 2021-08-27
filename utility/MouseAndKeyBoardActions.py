from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class MouseActions():
    def __init__(self, driver):
        self.driver = driver

    def escape(self, driver):
        action = ActionChains(driver)
        action.send_keys(Keys.ESCAPE).perform()




