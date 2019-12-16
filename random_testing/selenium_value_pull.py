from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest

"""
Label of the button is: Google Search
Name of the button is:- btnK
Id of the button is:- gbqfba
Invalid Attribute status of the button is: null
Class of the button is: gbqfba
"""


class GetAttributes(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def find_button_names(self):
        button_names = self.driver.find_elements_by_class_name("")
        print("The button names are: " + button_names)

    def find_button_ids(self):
        button_ids = self.driver.find_elements_by_id("")
        print("The button ids are: " + button_ids)

    def find_button_classes(self):
        button_classes = self.driver.find_elements_by_class_name("")
        print("The button classes are: " + button_classes)

    def find_button_tags(self):
        button_tags = self.driver.find_element_by_tag_name("")
        print("The button tags are: " + button_tags)

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
        unittest.main()

    def page_source(self):
        html = self.driver.page_source
        print(html)
        self.assertIn("Google", html)

    # copy selector
    # tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input

    # copy xpath
    # // *[ @ id = "tsf"] / div[2] / div[1] / div[1] / div / div[2] / input

    def find_things(self):
        element = self.driver.find_element(By.XPATH, "//*[@name'q']")
        element = self.driver.find_element(By.ID, "foo")
        element = self.driver.find_element(By.ID, "input-search")

        search_button = self.driver.find_element(By.XPATH, "//button[@data-uname='homeFreeFormSearch'")
        search_button.click()

        # Potential look at XPATH "//*[@title 'Search']"
        # //*[@id="tabTrending"]//a
        # //*[@ng-if="popularSearches"]\\a
        # //*[@ng-if="popularSearches"]//div[3]//a
        # //*[@ng-if="popularSearches"]//../../..//a















