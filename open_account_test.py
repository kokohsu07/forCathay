from selenium.webdriver import Chrome
from general_function import (driver_fixture,
                              mobile_fixture,
                              click_element,
                              switch_window,
                              wait_element_visible,
                              wait_element_present,
                              take_screenshot)

expect_home_page_title='國泰世華銀行'
expect_create_account_page_title='開戶說明 - 存款 - 產品介紹 - 國泰世華銀行'
expect_qr_code_height=160
expect_qr_code_width=160

XPATH='xpath'
ID='id'
ele_android_version='android'
ele_ios_version='ios'
ele_open_account='//a[@href="/cathaybk/personal/product/deposit/open-account"]'
btn_download_app='//a[@href="https://www.cathaybk.com.tw/cathaybk/promo/event/ebanking/product/APP-WEB/index.html"]'
img_qr_code='//img[@src="Content/images/qrcode.png"]'

def test_cathay_home_page(driver: Chrome):
    assert driver.title.startswith(expect_home_page_title)
    take_screenshot(driver, 'Cathay_home_page')

def test_create_account_page(driver: Chrome):
    click_element(XPATH,ele_open_account,driver)
    assert driver.title.startswith(expect_create_account_page_title)
    take_screenshot(driver, 'open_account_page')


def test_download_app_page(driver: Chrome):
    click_element(XPATH,ele_open_account,driver)
    click_element(XPATH, btn_download_app,driver)
    switch_window(driver)

    android_version = wait_element_present(ID,ele_android_version ,driver).text.split("：")[-1]
    ios_version = wait_element_present(ID,ele_ios_version,driver).text.split("：")[-1]
    assert android_version==ios_version

    qr_code_img=wait_element_present(XPATH,img_qr_code,driver).size
    assert ([qr_code_img['height'],qr_code_img['width']]==[expect_qr_code_height,expect_qr_code_width])
    take_screenshot(driver, 'download_app_page')

def test_webview_download_app_page(mobile: Chrome):
    try:
        wait_element_visible(XPATH,img_qr_code,mobile)
        not_found=False
    except:
        not_found=True
    take_screenshot(mobile, 'webview_download_app_page')
    assert not_found






