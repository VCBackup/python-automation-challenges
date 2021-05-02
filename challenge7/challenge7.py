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
        make_text = []
        make_links = []
        model_text = []
        model_links = []

        # Navigate to Copart
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

        # Store all the Make values displayed on the page along w/ URLs for the links
        make_list = self.driver.find_elements_by_xpath("//*[@id=\"tabMakes\"]/div/div/div/span/span/a")
        for x in make_list:
            make_text.append(x.text)
            make_links.append(x.get_attribute("href"))
        t = 0
        print("Makes")
        while t < len(make_text):
            print(make_text[t] + " : " + make_links[t])
            t += 1
        print("")

        # Store all the Model values displayed on the page along w/ URLs for the links
        self.driver.find_element_by_xpath("//*[@href=\"#tabModels\"]").click()
        model_list = self.driver.find_elements_by_xpath("//*[@id=\"tabModels\"]/div/div/div/span/span/a")
        for y in model_list:
            model_text.append(y.text)
            model_links.append(y.get_attribute("href"))
        t = 0
        print("Models")
        while t < len(model_text):
            print(model_text[t] + " : " + model_links[t])
            t += 1

        # Verify all the Make elements in the array navigate to the correct page
        print("")
        for i in make_links:
            try:
                print("Opening Link for : " + str(i) + "")
                self.driver.get(i)
                print("Success!")
            except TimeoutError:
                print("A page didn't load properly - Test Failed")

        # Verify all the Model elements in the array navigate to the correct page
        print("")
        for i in model_links:
            try:
                print("Opening Link for : " + str(i) + "")
                self.driver.get(i)
                print("Success!")
            except TimeoutError:
                print("A page didn't load properly - Test Failed")


if __name__ == '__main__':
    unittest.main()
