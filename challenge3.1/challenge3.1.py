import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec


class challenge3_1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3_1(self):
        # Navigate to Sling.com
        self.driver.get("https://www.sling.com")
        self.assertIn("Sling TV", self.driver.title)
        # Print the ALT text for the icons, and URLs
        channel_icon_list = self.driver.find_elements_by_xpath("//*[@id=\"channelList\"]/li/img")
        print("--------------- This is the list of channels ---------------")
        for x in channel_icon_list:
            print((x.get_attribute("alt") + ": \"" + x.get_attribute("src") + "\""))


if __name__ == '__main__':
    unittest.main()
