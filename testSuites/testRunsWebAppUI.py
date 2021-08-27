import unittest

from unittest import TestSuite, TextTestRunner, TestLoader
from testCases.chrome.test_Login_OK import Login as LoginChrome
from testCases.chrome.test_reinitialiser_mot_de_pass import ReinitMDP as ReinitMDPChrome
from testCases.firefox.test_Login_OK_firefox import LoginFirefox
from testCases.firefox.test_reinitialiser_mot_de_pass_firefox import ReinitMDPFirefox


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, True)


    if __name__ == '__main__':
        loader = TestLoader()
        webAppSuite = TestSuite((loader.loadTestsFromTestCase(LoginChrome),
                           loader.loadTestsFromTestCase(ReinitMDPChrome),
                           loader.loadTestsFromTestCase(LoginFirefox),
                           loader.loadTestsFromTestCase(ReinitMDPFirefox)
                            ))

        runner = TextTestRunner(verbosity=3, descriptions=True)
        runner.run(webAppSuite)
        # unittest.main()
