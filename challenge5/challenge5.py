import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec


class challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        # Navigate to Copart
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        # Do a search for “porsche”
        input_field = self.driver.find_element_by_id("input-search")
        input_field.send_keys("porsche")
        input_field.send_keys(Keys.RETURN)
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((
            By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody//td[6]/span")))
        # Change the drop down for “Show Entries” to 100 from 20
        input_field.send_keys(Keys.ESCAPE)
        self.driver.find_element_by_xpath("//*[@name=\"serverSideDataTable_length\"]").click()
        self.driver.find_element_by_xpath("//*[@name=\"serverSideDataTable_length\"]//option[3]").click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((
            By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody//td[6]/span")))
        # Count how many different models of porsche are in the results on the first page
        total_models = 0
        porsche_element_text = []
        porsche_model_types = {}
        porsche_element = self.driver.find_elements_by_xpath("//*[@id=\"serverSideDataTable\"]/tbody//*/td[6]/span")
        for x in porsche_element:
            porsche_element_text.append(x.text)
        print(porsche_element_text)
        for x in porsche_element_text:
            if x not in porsche_model_types:
                porsche_model_types[x] = 1
                total_models += total_models
            else:
                porsche_model_types[x] += porsche_model_types[x]
        # Return in the terminal how many of each type exists
        print(str(porsche_model_types))
        # Create a switch statement to count the types of damages:
        # REAR END, FRONT END, MINOR DENT/SCRATCHES, UNDERCARRIAGE, Other types are grouped into MISC


if __name__ == '__main__':
    unittest.main()
