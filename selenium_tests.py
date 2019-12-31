import unittest

from selenium.webdriver import Chrome
from time import sleep

class SearchText(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        # create a new Firefox session
        # If the version of Chromedriver you are using is in your path you don't need to include the path.
        inst.driver = Chrome('/Users/matthewrampey/Downloads/chromedriver')
        inst.driver.implicitly_wait(10)
        inst.driver.maximize_window()
        # navigate to the application home page
        inst.driver.get("https://www.hilton.com/en/hilton-honors/")
        inst.driver.title

    def test_search_by_virginia(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id("search-input-box")
        # enter search keyword and submit
        self.search_field.click()
        sleep(1)
        self.search_field.send_keys("Virginia")
        sleep(2)
        self.find_hotel = self.driver.find_element_by_css_selector("button[data-e2e='findHotel']")
        self.find_hotel.click()
        sleep(2)
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        lists = self.driver.find_elements_by_class_name("sResult.clear")
        self.assertEqual(20, len(lists))

    def test_search_by_west_virginia(self):
        self.home_link = self.driver.find_element_by_id("hhonors_logo_link")
        self.home_link.click()
        sleep(2)
        # get the search textbox
        self.search_field = self.driver.find_element_by_id("search-input-box")
        self.search_field.click()
        sleep(1)
        # enter search keyword and submit
        self.search_field.send_keys("West Virginia")
        sleep(3)
        self.find_hotel = self.driver.find_element_by_css_selector("button[data-e2e='findHotel']")
        self.find_hotel.click()
        #forces browser to wait
        sleep(2)
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        list_new = self.driver.find_elements_by_class_name("sResult.clear")
        self.assertEqual(20, len(list_new))

    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()