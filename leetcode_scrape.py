from selenium import webdriver

from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://leetcode.com'
driver.get(url)


def delay_text(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.4)


sign_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/div/a[5]/span')
sign_button.click()

sign_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/form/span[1]/input')
sign_input.click()
email_text = 'email'
delay_text(sign_input, email_text)

sign_input = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/div/div/form/span[2]/input')
sign_input.click()
password_text = 'password'
delay_text(sign_input, email_text)
