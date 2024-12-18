import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from allure_commons.types import AttachmentType
import time

def setup_function():
    global driver
    path=Service(r"C:\AI Operations\DevOps\Python Selenium\Drivers\firefoxdriver-win64\geckodriver.exe")
    firefox_options=Options()
    driver=webdriver.Firefox(service=path,options=firefox_options)
    driver.get("https://www.alnafi.com/auth/sign-in")
    driver.maximize_window()
    driver.implicitly_wait(20)

def teardown_function():
    driver.quit()

def my_cred():
    return [
        ('ali@gmail.com','ali2004'),
        ('umar@gmail.com','umar2004'),
        ('usman@gmail.com','usman2004'),
        ('hamid@gmail.com','hamid2004')
    ]

@pytest.mark.parametrize("username,password",my_cred())
def test_login(username,password):
    print("My Login...")
    driver.find_element(By.NAME,"email").send_keys(username)
    time.sleep(1.5)
    driver.find_element(By.NAME,"password").send_keys(password)
    time.sleep(1.5)
    allure.attach(driver.get_full_page_screenshot_as_png(),name="myalnafi_ss",attachment_type=AttachmentType.PNG)