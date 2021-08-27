# All variables used in all tests cases are here:

# Possible Envs
intBaseURL = "https://www.smood.ch/fr"
uatBaseURL = "https://www.smood.ch/fr"
stgBaseURL = "https://www.smood.ch/fr"

# =========== Login Profiles: start ===============
class LoginProfile:
    def __init__(self, email, pwd, name, role):
        self.email = email
        self.pwd = pwd
        self.name = name
        self.role = role


# possible test profiles
class LoginProfiles:
    MEMBER =     LoginProfile("<your_email_here>",    "<your password_here>", "Man0",  "Already User")
    NON_MEMBER = LoginProfile("blablabla@test.com", "xxxxxxxxx", "Unknown", "Non User")


# Possible Browsers
class Browsers:
    chrome = 'CHROME'
    firefox = 'FIREFOX'
    safari = 'SAFARI'


text_button_reinitialiser_mdp = "Réinitialiser mon mot de passe"

