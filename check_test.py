
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

        

def test_cat_rus_search():
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://goldapple.ru/")
    driver.implicitly_wait(20)
    
    driver.find_element(By.XPATH, "//*[@id='__layout']/div/header/div[2]/div[2]/button[2]").click()
    driver.find_element(By.XPATH, "//input[@placeholder='хочу купить']").send_keys("шампунь")
    sleep(2)

    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/aside[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[1]/ul/li[1]/button').click()
    assert driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/header/div/div/span').text == 'результаты по запросу'

def test_cat_rusoneng_search():

    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://goldapple.ru/")
    driver.implicitly_wait(20)
    
    driver.find_element(By.XPATH, "//*[@id='__layout']/div/header/div[2]/div[2]/button[2]").click()
    driver.find_element(By.XPATH, "//input[@placeholder='хочу купить']").send_keys("ifvgeym")
    sleep(2)

    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/aside[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[1]/ul/li[1]/button').click()
    assert driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/header/div/div/span').text == 'результаты по запросу'

def test_brend_eng_serch():

    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://goldapple.ru/")
    driver.implicitly_wait(20)
    
    driver.find_element(By.XPATH, "//*[@id='__layout']/div/header/div[2]/div[2]/button[2]").click()
    driver.find_element(By.XPATH, "//input[@placeholder='хочу купить']").send_keys("dolce gabbana")
    sleep(2)

    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/aside[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[1]/ul/li[1]/button').click()
    assert driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/header/div/div/span').text == 'результаты по запросу'

def test_brend_engonrus_serch():

    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://goldapple.ru/")
    driver.implicitly_wait(20)
    
    driver.find_element(By.XPATH, "//*[@id='__layout']/div/header/div[2]/div[2]/button[2]").click()
    driver.find_element(By.XPATH, "//input[@placeholder='хочу купить']").send_keys("вщдсу пфиифтф")
    sleep(2)

    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/aside[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[1]/ul/li[1]/button').click()
    assert driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/header/div/div/span').text == 'результаты по запросу'

def test_error_serch():

    driver = webdriver.Chrome()
    driver.maximize_window()
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://goldapple.ru/")
    driver.implicitly_wait(20)
    
    driver.find_element(By.XPATH, "//*[@id='__layout']/div/header/div[2]/div[2]/button[2]").click()
    driver.find_element(By.XPATH, "//input[@placeholder='хочу купить']").send_keys("!!!")
    driver.find_element(By.XPATH, '//*[@id="__layout"]/div/aside[1]/div[2]/div/div/div/div/div/div[1]/div/div/div/form/div[2]/button[1]').click()

    #driver.find_element(By.XPATH, '//*[@id="__layout"]/div/aside[1]/div[2]/div/div/div/div/div/div[3]/div/div[2]/div[2]/div/div[1]/ul/li[1]/button').click()
    assert driver.find_element(By.XPATH, '//*[@id="__layout"]/div/main/header/div/div[2]/p').text == 'Ничего не найдено. Попробуйте изменить запрос и мы поищем ещё раз.'