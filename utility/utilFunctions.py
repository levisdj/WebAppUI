import os
import sys
from functools import partialmethod

sys.path.append(os.getcwd())


def sreenshotOnFail(browser_attr='driver'):
    screenshots_folder = os.getcwd() + "\\..\\..\\screenshots\\"
    def decorator(cls):
        def with_screen_shot(self, fn, *args, **kwargs):
            """Take a Screen-shot of the drive page, when a function fails."""
            try:
                return fn(self, *args, **kwargs)
            except Exception:
                # This will only be reached if the test fails
                driver = getattr(self, browser_attr)
                filename = 'screen-%s.png' % fn.__name__
                driver.get_screenshot_as_file(screenshots_folder + filename)
                print('Screenshot saved as %s, in %s' % (filename, screenshots_folder))
                raise

        for attr, fn in cls.__dict__.items():
            if attr[:5] == 'test_' and callable(fn):
                setattr(cls, attr, partialmethod(with_screen_shot, fn))

        return cls
    return decorator

