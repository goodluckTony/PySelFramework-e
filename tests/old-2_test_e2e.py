# import pytest
# import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e(self, setup):

        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                self.driver.find_elements(By.CSS_SELECTOR, ".card-footer button")[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        self.driver.find_element(By.XPATH ,"//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID ,"country").send_keys("ind")
        # time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "India"))
        )

        self.driver.find_element(By.LINK_TEXT ,"India").click()
        self.driver.find_element(By.XPATH ,"//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR ,"[type='submit']").click()
        textMatch = self.driver.find_element(By.CSS_SELECTOR ,"[class*='alert-success']").text

        assert ("Success! Thank you!" in textMatch)
