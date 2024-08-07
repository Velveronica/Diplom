
import pytest
import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

        


sh_api="https://goldapple.ru/front/api/search/autocomplete?query=%D1%88%D0%B0%D0%BC%D0%BF%D1%83%D0%BD%D1%8C&cityId=8dea00e3-9aab-4d8e-887c-ef2aaa546456&geoPolygons[]=EKB-000000402&geoPolygons[]=EKB-000000400&geoPolygons[]=EKB-000000401&geoPolygons[]=EKB-000000399&customerGroupId=7"
resp=requests.get(sh_api)
print(resp.json())
