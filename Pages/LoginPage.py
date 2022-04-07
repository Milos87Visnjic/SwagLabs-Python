import unittest
from selenium import webdriver
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Locators.Lokatori import Lokator, Elementi


class SwagLabs(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.set_page_load_timeout(10)
        cls.driver.implicitly_wait(10)

    def test_is_page_up(self):

        # if page loads within load timeout verifies title and link
        # asserts page status at the end
        pagestatus = "page loaded"
        try:
            self.driver.get("https://www.saucedemo.com/")
            self.assertIn('Swag Labs', self.driver.title)
            self.assertIn('https://www.saucedemo.com/', self.driver.current_url)
        except TimeoutException as ex:
            pagestatus = ex.msg

        self.assertEqual("page loaded", pagestatus)

    def test_login(self):

        self.driver.find_element(By.XPATH, Lokator.userName).send_keys(Elementi.userName_text)
        self.driver.find_element(By.XPATH, Lokator.password).send_keys(Elementi.pass_text)
        self.driver.find_element(By.XPATH, Lokator.LoginButton).click()
        rew = self.driver.find_element(By.XPATH, Lokator.textaaa).text
        print(rew)

        assert rew == Elementi.textic

        print(Elementi.textic)
