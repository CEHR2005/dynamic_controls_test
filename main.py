import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestWebPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create a new instance of the Chrome driver
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        # Close the driver
        cls.driver.quit()

    def setUp(self):
        # Go to the webpage
        self.driver.get("http://the-internet.herokuapp.com/dynamic_controls")

    def test_remove_add_checkbox(self):
        # Click on the "Remove" button
        self.driver.find_element(By.CSS_SELECTOR, "#checkbox-example button").click()
        # Wait for 3 seconds (the duration of setTimeout in your script)
        time.sleep(3)

        # Assert that the button now says "Add"
        self.assertEqual("Add", self.driver.find_element(By.CSS_SELECTOR, "#checkbox-example button").text)
        # Assert that the checkbox is not present
        self.assertEqual(0, len(self.driver.find_elements(By.CSS_SELECTOR, "#checkbox")))

    def test_enable_disable_input(self):
        # Click on the "Enable" button
        self.driver.find_element(By.CSS_SELECTOR, "#input-example button").click()
        # Wait for 3 seconds (the duration of setTimeout in your script)
        time.sleep(3)

        # Assert that the button now says "Disable"
        self.assertEqual("Disable", self.driver.find_element(By.CSS_SELECTOR, "#input-example button").text)
        # Assert that the input is enabled
        self.assertIsNone(self.driver.find_element(By.CSS_SELECTOR, "#input-example input").get_attribute("disabled"))


if __name__ == "__main__":
    unittest.main()
