import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from datetime import datetime

now=datetime.now()
dt_string = now.strftime("%Y%m%d-%H%M%S")

url='https://www.cathaybk.com.tw/cathaybk'
url_download_app='https://www.cathaybk.com.tw/cathaybk/promo/event/ebanking/product/appdownload/index.html'
timeout='5'
mobile_device='Pixel 7'


@pytest.fixture(name="driver")
def driver_fixture() -> Chrome:
    driver_path = ChromeDriverManager().install()
    driver = webdriver.Chrome(service=Service(driver_path))
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture(name="mobile")
def mobile_fixture() -> Chrome:
    mobile_emulation = {"deviceName": mobile_device}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_experimental_option("windowTypes", ["webview"])
    chrome_options.add_argument('start-maximized')
    mobile = webdriver.Chrome(options=chrome_options)
    mobile.get(url_download_app)
    yield mobile


def click_element(method,value,driver: Chrome):
    element = wait_element_present(method,value,driver)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("arguments[0].click();", element)

def wait_element_present(method,value,driver):
    if method == 'xpath':
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, value)))
    elif method == 'id':
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, value)))
    return element

def wait_element_visible(method, value, driver):
    if method == 'xpath':
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, value)))
    elif method == 'id':
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, value)))

def switch_window(driver):
    handles = driver.window_handles
    driver.switch_to.window(handles[-1])

def take_screenshot(driver,filename):
    driver.save_screenshot('./screenshots/'+ filename +'_'+ dt_string + '.png')