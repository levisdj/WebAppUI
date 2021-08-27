from utility.WebAppUITestCase import WebAppUITestCase
from pageObjects.PageLogin import PageLogin
from testCases import variables as var
from utility.utilFunctions import sreenshotOnFail
import sys, os
sys.path.append(os.getcwd())


@sreenshotOnFail()
class ReinitMDP(WebAppUITestCase):
    login_profile = var.LoginProfiles.NON_MEMBER  # BM profile
    driver = None
    do_login = False
    browser = var.Browsers.chrome

    def test_01_bouton_reinitialiser_mdp(self):
        pl = PageLogin(self.driver)

        # Try to Login with the specified profile (a Non Member or a Member with wrong email and/or password)
        pl.login_with_profile(self.login_profile)

        # Here we are testing the capability to reset a Password
        pl.forgotten_password_open_reinitialization_form()
        self.assertEqual(pl.button_reinitialiser_mdp_xpath.get_text(), var.text_button_reinitialiser_mdp, "Bouton Réinitialsé bien présent sur le site")
        self.assertTrue(pl.button_reinitialiser_mdp_xpath.is_displayed(), "Bouton réinitialiser visible")
        self.assertTrue(pl.button_reinitialiser_mdp_xpath.is_enabled(), "Bouton réinitialiser activé")
