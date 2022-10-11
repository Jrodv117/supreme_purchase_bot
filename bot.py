from selenium import webdriver
from configkeys import keys

def order(key):
    driver = webdriver.Chrome('./chromedriver')
    driver.get(key['product_url'])

if __name__ == '__main__':
    order(keys)