import unittest
from selenium import webdriver
from utils.seleniumtools import find_element
class TestCaseLogin(unittest.TestCase):
    #每个成员方法就是固定的测试用例
    def test_01_login_success(self):
        driver = webdriver.Chrome(executable_path = "drivers\\chromedriver.exe")
        driver.get("http://132.232.44.158:8080/ljindex/")
        login1 = ("xpath",'//*[@id="unlogin"]/div[1]/a')
        user = ("id","username")
        password = ("id","password")
        userlogin = ("id","userLogin")
        find_element(driver,login1).click()
        find_element(driver,user).send_keys("yangyang12")
        find_element(driver,password).send_keys("12345678")
        find_element(driver,userlogin).click()
        try:
            assert driver.title == "测谈网"
            print("成功！")
        except:
            print("失败！")


        