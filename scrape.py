import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
from sqlalchemy import create_engine, text
import re
import sqlalchemy
from sqlalchemy.exc import IntegrityError
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

# Database connection setup
engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

# Webdriver setup
chrome_options = webdriver.ChromeOptions()

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the course overview page
url = 'https://uvt.osiris-student.nl/#/onderwijscatalogus/extern/cursussen'
driver.get(url)

time.sleep(5)

# Switch to the English version of the website
osi_language = driver.find_elements(By.CLASS_NAME, 'osi-language')[0]
actions = ActionChains(driver)
actions.move_to_element(osi_language).click().perform()

time.sleep(2)