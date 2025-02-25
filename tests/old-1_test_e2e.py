# import pytest
# from selenium import webdriver
# import time
import pytest
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class TestOne:

    def test_e2e(self, setup):
        # service_obj = Service("J:/TestBrowserDrivers/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        # driver = webdriver.Chrome(service=service_obj)
        # driver.get("https://qaclickacademy.github.io/protocommerce/")
        # driver.maximize_window()

        setup.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        # cards = checkoutpage.getCardTitles()
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        confirmpage = checkoutpage.checkOutItems()
        log.info("Entering country name as ind")
        self.driver.find_element_by_id("country").send_keys("ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")

        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text
        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)
