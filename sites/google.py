import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import random

def generate_random_series_formatted():
    # Define the format: 10 digits, colon, 16 digits
    format_pattern = [10, 16]
    # Generate random series according to the specified format
    random_series = ':'.join(''.join(str(random.randint(0, 9)) for _ in range(length)) for length in format_pattern)
    return random_series


def check_google_registration(driver, email):
    url = f"https://accounts.google.com/lifecycle/steps/signup/unknownerror?dsh=S-{generate_random_series_formatted()}&flowEntry=SignUp&flowName=GlifWebSignIn&theme=glif&TL=ADg0xR14TI4Zw5QpeErF8QUMAxMdoDKLMKmn8rdqjhRfdghfpclzpuhugh1bYwWMNul8"
    driver.get(url)
    time.sleep(2)
    
    # driver.find_element(By.CSS_SELECTOR, 'button.FliLIb > div:nth-child(3)').click()
    #Pour accepter les conditions
    driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()
    #Pour cliquer sur le bouton suivant
    driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()
    
    time.sleep(1)
    firstname = driver.find_element(By.ID, 'firstName')
    firstname.send_keys("John")
    
    lastname = driver.find_element(By.ID, 'lastName')
    lastname.send_keys("Smith")
    
    driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()
    
    time.sleep(1)
    
    day = driver.find_element(By.ID, 'day')
    day.send_keys("14")
    
    
    select_element = driver.find_element(By.ID, "month")
    selectm = Select(select_element)
    selectm.select_by_visible_text("Janvier")
    

    year = driver.find_element(By.ID, 'year')
    year.send_keys("2000")
    
    select_gender = driver.find_element(By.ID, "gender")
    selectg = Select(select_gender)
    selectg.select_by_visible_text("Homme")
    
    driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()

    time.sleep(1)
    test_email = driver.find_element(By.NAME, "Username")
    test_email.send_keys(email)
    time.sleep(1)
    driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()
    
   
    result= ""
    time.sleep(1)
    try:
        error_message_element = driver.find_element(By.CLASS_NAME, "jibhHc")
        error_text = error_message_element.text
    except NoSuchElementException:
        error_text = ""  
        
    if error_text:
        result = "True"
    else:
        result = "False"
    
    
    return result
    
    