import unittest
from context import crazythursday
from freezegun import freeze_time

@crazythursday.CrazyThursday
def demo():
    return "demo"

class CrazyTestSuite(unittest.TestCase):
    def test_is_thursday(self):
        with freeze_time("2022-09-08"): # Thursday
            with self.assertRaises(crazythursday.CrazyThursdayException):
                demo()

    def test_is_not_thursday(self):
        with self.assertRaises(AssertionError):
            with freeze_time("2022-09-09"): # Friday
                demo()
                raise AssertionError

if __name__ == '__main__':
    unittest.main()
