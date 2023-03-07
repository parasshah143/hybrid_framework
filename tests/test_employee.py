from selenium.webdriver.common.by import By
from assertpy import assert_that
from base.webdriver_listener import WebDriverWrapper
import time


class TestAddEmployee(WebDriverWrapper):
    def test_add_valid_employee(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, "//span[text()='PIM']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Add Employee']").click()
        self.driver.find_element(By.NAME, "firstName").send_keys("Paras")
        self.driver.find_element(By.NAME, "lastName").send_keys("Shah")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(20)
        actual_employee_name = self.driver.find_element(By.XPATH, "//div[contains(@class,'employee-name')]").text
        assert_that("Paras Shah").is_equal_to(actual_employee_name)
