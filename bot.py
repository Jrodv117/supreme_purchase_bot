from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from configkeys import keys

def order(key):
    s = Service('./chromedriver')
    driver = webdriver.Chrome(service=s)
    driver.get(key['product_url'])
    driver.find_elements(By.XPATH, '//*[@id="add-remove-buttons"]/input').click()
    
if __name__ == '__main__':
    order(keys)