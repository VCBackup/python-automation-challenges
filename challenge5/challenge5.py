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
        # Create a switch statement to count the types of damages
        porsche_data_columns = {
            "selection": 1,
            "image": 2,
            "lot number": 3,
            "year": 4,
            "make": 5,
            "model": 6,
            "item number": 7,
            "location": 8,
            "sale date": 9,
            "odometer": 10,
            "doc type": 11,
            "damage": 12,
            "retail value": 13,
            "current bid": 14
        }
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
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((
            By.XPATH, "//*[@name=\"serverSideDataTable_length\"]//option[3]")))
        self.driver.find_element_by_xpath("//*[@name=\"serverSideDataTable_length\"]//option[3]").click()
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((
            By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody/tr[100]")))

        # Create a way to count different types of data about the cars that are in the results on the first page
        def porsche_info_pull(desired_info):
            porsche_variable_types = {}
            total_porsche_variables = 0
            porsche_element_text = []
            porsche_element = self.driver.find_elements_by_xpath(
                "//*[@id=\"serverSideDataTable\"]/tbody//*/td["+str(desired_info)+"]/span")
            for x in porsche_element:
                porsche_element_text.append(x.text)
            for x in porsche_element_text:
                if x not in porsche_variable_types:
                    porsche_variable_types[x] = 1
                    total_porsche_variables += total_porsche_variables
                else:
                    porsche_variable_types[x] += 1
            # Return in the terminal how many of each type exists
            print(porsche_variable_types)

        print("PORSCHE MODELS")
        porsche_info_pull(porsche_data_columns["model"])
        print("PORSCHE MODEL DAMAGE")
        porsche_info_pull(porsche_data_columns["damage"])


if __name__ == '__main__':
    unittest.main()
