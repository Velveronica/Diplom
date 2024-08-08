
import json
import pytest
import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

        
        
def test_film_id():
    f_api="https://api.kinopoisk.dev/v1.4/movie/666"
    headers={"accept": "application/json", 
                      'X-API-KEY': 'Q2307CQ-8Z941Y0-MBABRX0-YAC4QQD'}
    resp=requests.get(f_api, headers=headers)
    assert resp.status_code==200
    assert resp.json()["name"]=="Форсаж"


def test_film_search():
    f_api="https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query=%D0%BB%D1%8E%D0%B1%D0%BE%D0%B2%D0%BD%D1%8B%D0%B9"
    headers={"accept": "application/json", 
                      'X-API-KEY': 'Q2307CQ-8Z941Y0-MBABRX0-YAC4QQD'}
    resp=requests.get(f_api, headers=headers)
    assert resp.status_code==200
    

def test_film_random():
    f_api="https://api.kinopoisk.dev/v1.4/movie/random?notNullFields=top10"
    headers={"accept": "application/json", 
                      'X-API-KEY': 'Q2307CQ-8Z941Y0-MBABRX0-YAC4QQD'}
    resp=requests.get(f_api, headers=headers)
    assert resp.status_code==200


def test_film_list():
    f_api="https://api.kinopoisk.dev/v1/movie/possible-values-by-field?field=genres.name"
    headers={"accept": "application/json", 
                      'X-API-KEY': 'Q2307CQ-8Z941Y0-MBABRX0-YAC4QQD'}
    resp=requests.get(f_api, headers=headers)
    assert resp.status_code==200


def test_person_id():
    f_api="https://api.kinopoisk.dev/v1.4/person/7640"
    headers={"accept": "application/json", 
                      'X-API-KEY': 'Q2307CQ-8Z941Y0-MBABRX0-YAC4QQD'}
    resp=requests.get(f_api, headers=headers)
    assert resp.status_code==200
    assert resp.json()["name"]=="Квентин Тарантино"
