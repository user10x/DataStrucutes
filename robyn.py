from selenium import webdriver

from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://cgifederal.secure.force.com'
driver.get(url)


def delay_text(element,text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.4)


email = driver.find_element(By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:username')
email.click()
email_text = 'kashksahfds@gmail.com'

delay_text(email, email_text)

password = driver.find_element(By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password')
password.click()
password_text = 'kahdskfdsahdkfhsa'
delay_text(password,password_text)

# privacy_policy = driver.find_element(By.XPATH,'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:j_id167')
privacy_policy = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div/div/div/span/form/div[2]/div[2]/table/tbody/tr[3]/td/label/input')
privacy_policy.click()

recaptcha = driver.find_element(By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:theId')
image = recaptcha.get_attribute('src')

import base64

imgdata = base64.b64decode(image.split(",")[-1])

from io import BytesIO
from PIL import Image

file_like = BytesIO(imgdata)
img = Image.open(file_like)

import pytesseract

img.save('captcha_original.png')

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

gray = img.convert('L')
gray.save('captcha_gray.png')
bw = gray.point(lambda x: 0 if x < 1 else 255, '1')
bw.save('captcha_thresholded.png')

text = pytesseract.image_to_string(bw)
print(text)

# filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
# with open(filename, 'wb') as f:
#   f.write(imgdata)

# translated recaptcha
word = text

key = "6LdRlMASAAAAAA0JYgUgTmkVnjxMzBcw19B0PLSL"
api_key = "5c7419472ef3544abf45984ead498302"

entry = driver.find_element(By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:recaptcha_response_field')
entry.click()
entry.send_keys(word)

login = driver.find_element(By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:loginButton')
# login.click()
