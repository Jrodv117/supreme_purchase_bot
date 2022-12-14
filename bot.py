from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
from configkeys import keys
import time

def order(key):
    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.get(key['product_url'])
    driver.find_element('xpath', '/html/body/div/div/div[2]/div/form/fieldset[2]/input').click()
    driver.find_element('xpath', '//*[@id="cart"]/a[2]').click()
    driver.find_element('xpath', '//*[@id="order_billing_name"]').send_keys(key['name'])
    driver.find_element('xpath', '//*[@id="order_email"]').send_keys(key['email'])
    driver.find_element('xpath', '//*[@id="order_tel"]').send_keys(key['tel'])
if __name__ == '__main__':
    order(keys)