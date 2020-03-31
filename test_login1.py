import unittest
from selenium import webdriver
from utils.seleniumtools import find_element
class TestCaseLogin1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path = "drivers\\chromedriver.exe")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("http://132.232.44.158:8080/ljindex/")
        
    def test_01_login1_success(self):
        login1 = ("xpath",'//*[@id="unlogin"]/div[1]/a')
        user = ("id","username")
        password = ("id","password")
        userlogin = ("id","userLogin")
        find_element(self.driver,login1).click()
        find_element(self.driver,user).send_keys("yangyang12")
        find_element(self.driver,password).send_keys("12345678")
        find_element(self.driver,userlogin).click()
        try:
            assert driver.title == "测谈网"
        except:
            return False
    def test_02_login1_fail(self): 
        login1 = ("xpath",'//*[@id="unlogin"]/div[1]/a')
        user = ("id","username")
        password = ("id","password")
        userlogin = ("id","userLogin")
        find_element(self.driver,login1).click()
        find_element(self.driver,user).send_keys("yangyng12")
        find_element(self.driver,password).send_keys("12345678")
        find_element(self.driver,userlogin).click()
        try:
            assertNotEqual(driver.title,"测谈网")
        except:
            return False