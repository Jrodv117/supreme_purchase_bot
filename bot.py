from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from configkeys import keys

def order(key):
    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.get(key['product_url'])

if __name__ == '__main__':
    order(keys)