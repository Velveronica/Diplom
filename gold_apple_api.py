
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Formtest:
    def __init__(self, browser) -> None:
        
        self.browser=browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")