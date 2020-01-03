import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.common.exceptions
import selenium.webdriver.support.expected_conditions as ec
import logging


class challenge7(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        list_of_elements = [
            "//*[@ng-repeat=\"popularSearch in popularSearches | limitTo: 5\"]//a",
            "//*[@ng-repeat=\"popularSearch in popularSearches | limitTo: 5 : 5\"]//a",
            "//*[@ng-repeat=\"popularSearch in popularSearches | limitTo: 5: 10\"]//a",
            "//*[@ng-repeat=\"popularSearch in popularSearches | limitTo: 5 : 15\"]//a"
        ]
        make_model_links = {}
        # Navigate to Copart
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        # Go to Makes/Models & store all the values displayed on the page along w/ URLs for the links
        for x in list_of_elements:
            make_model_list = self.driver.find_elements_by_xpath(x)
            for y in make_model_list:
                make_model_links[y.text] = y.get_attribute("href")
        # Verify all the elements in the array navigate to the correct page
        print(make_model_links)
        for x in make_model_links:
            try:
                print("Opening Link for : " + str(x) + "")
                self.driver.get(make_model_links[x])
                print("Success!")
            except Exception:
                print("A page didn't load properly - Test Failed")


if __name__ == '__main__':
    unittest.main()
