
import pytest
import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

        
        
def test_film():
    f_api="https://api.kinopoisk.dev/v1.4/movie/968031"
    headers={"accept": "application/json", 
                      'X-API-KEY': 'Q2307CQ-8Z941Y0-MBABRX0-YAC4QQD'}
    resp=requests.get(f_api, headers=headers)
    assert resp.status_code==200

