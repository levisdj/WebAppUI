import time
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.BasePage import BasePage, BaseLocator
from utility.MouseAndKeyBoardActions import MouseActions
from selenium.webdriver.common.by import By

default_wait_time = 15  # seconds


class PageLogin(BasePage):
    Inscription_Connexion_link_xpath = BaseLocator(By.XPATH, "/html/body/header/div[1]/div[3]/gbx-button/button/span")
    input_adresse_mail_id = BaseLocator(By.ID, "connectionForm-username")
    input_mot_de_passe_id = BaseLocator(By.ID, "connectionForm-password")
    button_Connexion =      BaseLocator(By.XPATH, "//*[@id='connectionForm']/div[5]/button")

    button_mot_de_passe_oublie_id = BaseLocator(By.ID, "connectionFormPasswordForgotten")
    button_reinitialiser_mdp_xpath = BaseLocator(By.XPATH, "//*[@id='forgotPasswordForm']/div[3]/button")

    def login_with_profile(self, profile):
        """Log-in with the specify LoginProfile"""

        print("Logging in as %s..." % profile.name)

        ma = MouseActions(self.driver)
        # Escape from KeyBoard to remove the popup
        time.sleep(0.5)
        ma.escape(self.driver)

        #Clicking on Incription ou Connexion
        self.Inscription_Connexion_link_xpath.click()

        # Fill email
        self.input_adresse_mail_id.send_keys(profile.email)

        # Set password
        self.input_mot_de_passe_id.send_keys(profile.pwd)

        # Submit button
        self.button_Connexion.click()

    def forgotten_password_open_reinitialization_form(self):
        """Click on 'Mot de Pass Oublié' and access the re-initialization form """
        self.button_mot_de_passe_oublie_id.click()
        # self.button_reinitialiser_mdp_xpath.click()
        # print("The Text is ====>>>>", self.button_reinitialiser_mdp_xpath.get_text())

    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, default_wait_time)
