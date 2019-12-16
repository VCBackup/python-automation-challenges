import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec


class challenge3_2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3_2(self):
        # Navigate to Help.Sling.com
        self.driver.get("https://help.sling.com/")
        self.assertIn("Help Center", self.driver.title)
        print("Landed on Help.Sling.com")
        # Run a search for Roku
        search_input = self.driver.find_element_by_xpath("//*[@name=\"term\"]")
        search_input.send_keys("Roku")
        search_input.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((
            By.XPATH, "//*[@class=\"search-results-list\"]//*[@class=\"article-list-group\"]")))
        # Ensure the returned list is > 0
        returned_list = self.driver.find_elements_by_xpath("//*[@class=\"search-results-list\""
                                                           "]//*[@class=\"article-list-group\"]")
        self.assertGreater(len(returned_list), 0, "The returned search is smaller than, or equal to, zero.")
        print("The returned list is greater than zero.")


if __name__ == '__main__':
    unittest.main()
