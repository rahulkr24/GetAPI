import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests

chromeOptions = Options()
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--disable-dev-shm-usage')
chromeOptions.add_argument('window-size=1920x1080')

# options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
M_Friendly_Name = []
M_url = []
down_id = []
id_list = []
delay = 50
url = "https://uptimerobot.com/login?ref=website-header"

POD1 = "u1888140-d78498a229dc7d28d336bba6"
POD2 = "u1888143-ef8b448b33a1046d9f5349d1"
POD3 = "u1889112-324fdd3fc60eec0d78bc7606"
POD4 = "u1904758-7d33983157980c4adb55dff5"
api_key = [POD2, POD3, POD4]

username1 = "qa1@qikpod.com"
username2 = "qa2@qikpod.com"
username3 = "qa3@qikpod.com"
username4 = "qa4@qikpod.com"
username5 = "rahulkumar.rj24@gmail.com"
password4 = "Rahul@123"
password = "qikpod123"


def xpath_by_class(param):
    try:
        my_element = WebDriverWait(driver, delay).until(ec.element_to_be_clickable((By.CLASS_NAME, param)))
        my_element.click()
        time.sleep(1)
    except Exception as e:
        print(e, "------------failed----------------------")
        driver.quit()
        assert True


def xpath_click(param):
    try:
        time.sleep(1)
        my_element = WebDriverWait(driver, delay).until(ec.element_to_be_clickable((By.XPATH, param)))
        my_element.click()
    except Exception as e:
        print(e, "------------failed----------------------")
        driver.quit()
        assert True


def select_spot(param, key):
    try:
        time.sleep(2)
        select = Select(WebDriverWait(driver, delay).until(ec.element_to_be_clickable((By.XPATH, param))))
        select.select_by_visible_text(key)
    except Exception as e:
        print(e, "------------failed----------------------")
        driver.quit()
        assert True


def xpath_send_keys(param, key):
    try:
        my_element = WebDriverWait(driver, delay).until(ec.element_to_be_clickable((By.XPATH, param)))
        my_element.send_keys(key)
        time.sleep(1)
    except Exception as e:
        print(e, "------------failed----------------------")
        driver.quit()
        assert True


def delete_all_monitor1(username, password1):
    driver.get(url)
    driver.maximize_window()
    xpath_send_keys('//*[@id="userEmail"]', username)
    xpath_send_keys('//*[@id="userPassword"]', password1)
    xpath_by_class("uk-button.uk-button-primary.uk-button-large.uk-width-1-1")
    print("Login")
    time.sleep(3)
    xpath_by_class("bulkActions.text-grey.underlineLink")
    time.sleep(3)
    xpath_click('//*[@id="s2id_bulkActionType"]')
    time.sleep(3)
    xpath_click('//*[@id="select2-results-54"]/li[5]/div')
    print("ok")
    xpath_click('//*[@id="s2id_bulkType"]/a')
    time.sleep(3)
    xpath_click('//*[@id="select2-results-55"]/li[2]/div')
    xpath_send_keys('//*[@id="bulkActionApproveText"]', "DELETE MONITORS")
    time.sleep(3)
    xpath_click('//*[@id="bulkActionsForm"]/div[2]/button[2]')
    time.sleep(3)
    xpath_click('//*[@id="bulkActionsForm"]/div[2]/button[1]')
    print("All Monitors are Deleted")
    driver.close()


delete_all_monitor1(username5, password4)