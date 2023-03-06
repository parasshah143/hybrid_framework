import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


def scope_class():
    print("class triggered")
    yield
    print("class end")


class TestLoginUI:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        self.driver.quit()

    def test_title(self):
        actual_title = self.driver.title
        print(actual_title)
        # assert actual_title == "OrangeHRM"
        assert_that("OrangeHRM").is_equal_to(actual_title)

    def test_header(self):
        header = self.driver.find_element(By.XPATH, "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']").text
        print(header)
        assert_that("Login").is_equal_to(header)

    def test_valid_login(self):
        self.driver.find_element(By.NAME, "username").send_keys("Admin")
        self.driver.find_element(By.NAME, "password").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        text12 = self.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']").text
        assert_that("Dashboard").is_equal_to(text12)


# class TestLogin(TestLoginUI):
#     def test_valid_login(self):
#         print("valid login")
#
#     def test_invalid_login(self):
#         print("Invalid login")
