import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


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
