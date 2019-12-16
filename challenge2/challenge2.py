import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        # Navigate to Copart.com
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        # Search for "Exotics"
        input_field = self.driver.find_element_by_id("input-search")
        input_field.send_keys("exotics")
        input_field.send_keys(Keys.RETURN)
        # Verify "Porsche" is present
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.XPATH,
                                                                               "//*[@id=\"serverSideDataTable\"]//td")))
        data_table = self.driver.find_element_by_xpath("//*[@id=\"serverSideDataTable\"]")
        self.assertIn("PORSCHE", data_table.text)


if __name__ == '__main__':
    unittest.main()
