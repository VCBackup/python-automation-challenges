import unittest
import fibonacci_sequence_generation
from selenium import webdriver


# Display the string representation for the number 21 (i.e. 21 - twenty one)
class challenge_four(unittest.TestCase):

    # A one line call out to another function (fibonacci_sequence_generation)
    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge_four(self):
        fibonacci_sequence_generation.fibo_twenty_one()


if __name__ == '__main__':
    unittest.main()
