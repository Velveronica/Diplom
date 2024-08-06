
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Product:
    def __init__(self, browser) -> None:
        
        self.browser=browser
        self.browser.get("https://goldapple.ru/")

    def search(self, task):

        self.browser.find_element(By.XPATH, '//*[@id="__layout"]/div/header/div[2]/div[2]/button[2]').click()
        self.browser.find_element(By.XPATH, '//*[@id="__layout"]/div/aside[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/form/div[1]/input[1]').keys(task)
        
def test():
    driver = webdriver.Chrome()
    driver.get("https://goldapple.ru/")
    driver.implicitly_wait(20)
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '#layout > div > header > div.ga-headertop > div.ga-header__tabs > button.SqaAT.eHARx.jKhBm.ga-header__tab.ga-header__tab_type_search.ga-header__action > i > svg').click()
    driver.find_element(By.XPATH, "//input[@placeholder='хочу купить']").send_keys("шампунь")
    driver.find_element(By.XPATH, '//[@id="__layout"]/div/aside[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[1]/ul/li[1]/button/span').click()
    assert driver.find_element(By.XPATH, '//[@id="__layout"]/div/main/header/div/div/span').text == 'результаты по запросу'