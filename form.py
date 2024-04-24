import time
import threading
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep


# Initialize the driver
driver = webdriver.Chrome()  # Substitute with the driver of your choice
driver.maximize_window()

# Open the webpage
driver.get(
    "https://statechampsnetwork.com/michigan-high-school-lacrosse-player-of-the-year-award/"
)

input_class_name = "input_11_2"
choice_id = "choice_11_1_8"
choice_class = "gchoice gchoice_11_1_8"
choice_css = "input[type='radio'][value='gpoll1e1de16d4']"
choice_xpath = "//input[@value='gpoll1e1de16d4']"
submit_id = "gform_submit_button_11"

# # Find the input field using the class name
# input_field = driver.find_element(By.ID, 'input_11_2')

# # Fill up the input field
# input_field.send_keys('azizulraihan19@gmail.com')

# choice = driver.find_element(By.CLASS_NAME, choice_class)

# # Click on the choice
# choice.click()


# submit = driver.find_element_by_id('gform_submit_button_11')
with open("personal_emails.txt", "r") as file:
    emails = [line.rstrip() for line in file]

print(len(emails))

count = 0
for email in emails:
    print(count)
    count += 1
    for _ in range(90):
        # Find the input field using the class name
        input_field = driver.find_element(By.ID, input_class_name)

        # Fill up the input field
        input_field.send_keys(email)

        # Find the choice using its ID
        # choice = WebDriverWait(driver, 500).until(
        #     EC.presence_of_element_located((By.ID, choice_id)))

        # sleep(2)
        choice = driver.find_element(By.XPATH, choice_xpath)
        driver.execute_script("arguments[0].click();", choice)
        # Click on the choice
        # choice.click()

        # Wait for the page to load after clicking
        # sleep(1)

        # submit = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, submit_id)))

        submit = driver.find_element(By.ID, submit_id)
        driver.execute_script("arguments[0].click();", submit)
        # submit.click()

        # Reload the page
        driver.refresh()

        # Wait for the page to load after refreshing
        sleep(1)  # Adjust this value based on your page's load time
