from utility.WebAppUITestCase import WebAppUITestCase
from pageObjects.PageHome import PageHome
from pageObjects.PageLogin import PageLogin
from testCases import variables as var
from utility.utilFunctions import sreenshotOnFail
import sys, os
sys.path.append(os.getcwd())


@sreenshotOnFail()
class LoginFirefox(WebAppUITestCase):
    login_profile = var.LoginProfiles.MEMBER  # BM profile
    driver = None
    do_login = False
    browser = var.Browsers.firefox

    def test_01_login_with_valid_credentials(self):
        pl = PageLogin(self.driver)
        ph = PageHome(self.driver)

        # Login with the specified profile
        pl.login_with_profile(self.login_profile)

        # Check the connected user
        (name) = ph.get_user_profile_info()
        assert name == self.login_profile.name, "The logged user is not %s" % self.login_profile.name
