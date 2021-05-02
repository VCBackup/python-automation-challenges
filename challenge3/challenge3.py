import unittest
from selenium import webdriver


class challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3_for_loop(self):
        # Navigate to Copart
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        print("Landed on Copart")
        # Print a list of all "Popular Items > Makes/Models" & the URL/href for each type
        for x in self.driver.find_elements_by_xpath("//*[@id=\"tabMakes\"]//span/span/a"):
            print(x.text+" - "+self.driver.find_element_by_link_text(x.text).get_attribute("href"))

    def test_challenge3_while_loop(self):
        # Navigate to Copart
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)
        print("Landed on Copart")
        # Print a list of all "Popular Items > Makes/Models" & the URL/href for each type
        for x in self.driver.find_elements_by_xpath("//*[@id=\"tabMakes\"]//span/span/a"):
            print(x.text+" - "+self.driver.find_element_by_link_text(x.text).get_attribute("href"))


if __name__ == '__main__':
    unittest.main()
