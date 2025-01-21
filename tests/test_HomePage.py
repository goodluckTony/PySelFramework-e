import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()

        homepage = HomePage(self.driver) # driver.find_element(By.CSS_SELECTOR, "[name='name']").send_keys("Rahul")

        log.info("Firstname is "+getData["firstname"])

        homepage.getName().send_keys(getData["firstname"])
        # time.sleep(5)
        homepage.getEmail().send_keys(getData["lastname"]) # driver.find_element(By.NAME, "email").send_keys("shetty")
        homepage.getCheckBox().click() # driver.find_element(By.ID, "exampleCheck1").click()

        self.selectOptionByText(homepage.getGender(), getData["gender"])
        # sel = Select(homepage.getGender()) # sel = Select(driver.find_element(By.XPATH, "exampleFormControlSelect1"))
        # sel.select_by_visible_text("Male")

        homepage.submitForm().click() # driver.find_element(By.XPATH, "//input[@value='Submit']").click()

        alertText = homepage.getSuccessMessage().text # alertText = driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param