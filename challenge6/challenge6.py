import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.common.exceptions
import selenium.webdriver.support.expected_conditions as ec
import logging


class challenge6(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        # Navigate to Copart
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        # Do a search for “Nissan”
        input_field = self.driver.find_element_by_id("input-search")
        input_field.send_keys("Nissan")
        input_field.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((
            By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody//td[6]/span")))
        # Change the drop down for “Show Entries” to 100 from 20
        input_field.send_keys(Keys.ESCAPE)
        self.driver.find_element_by_xpath("//*[@name=\"serverSideDataTable_length\"]").click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((
            By.XPATH, "//*[@name=\"serverSideDataTable_length\"]//option[3]")))
        self.driver.find_element_by_xpath("//*[@name=\"serverSideDataTable_length\"]//option[3]").click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((
            By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody/tr[100]")))
        # Search for Model "Skyline"
        counter = 1
        try:
            nissan_models = self.driver.find_elements_by_xpath("//*[@id=\"serverSideDataTable\"]//td[6]")
            for x in nissan_models:
                if x.text == "ARMADA":
                    self.driver.find_element_by_xpath("//*[@id=\"serverSideDataTable\"]"
                                                      "//tr["+str(counter)+"]/td[3]/div/a").click()
                counter += 1
        # If it doesn't exist throw an exception, catch the exception, and take a screenshot
        except Exception:
            logging.warning("No Skyline link to click")
            self.driver.save_screenshot("skyline_missing.png")


if __name__ == '__main__':
    unittest.main()
