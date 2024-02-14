import time
from selenium.webdriver.common.by import By

def check_doctolib_registration(driver, email):
    driver.get("https://www.doctolib.fr/sessions/new?context=navbar")
    driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]').click()
    nowUrl = driver.current_url
    # if nowUrl == ""
    driver.find_element(By.CLASS_NAME,'.dl-button-primary').click()
    #driver.find_element(By.CSS_SELECTOR,'.dl-button-tertiary-primary > span:nth-child(1)').click()
   
    #phone
    phone_input = driver.find_element(By.ID, 'phone_number')
    phone_input.send_keys("0683042938") #phone factice
    
    #email
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys(email) #email factice
    
    #email confirmation
    email_confirmation_input = driver.find_element(By.ID, 'email_confirmation')
    email_confirmation_input.send_keys(email) #email confirmation factice

    #birthday
    birthday_date = driver.find_element(By.ID, 'birthdate')
    birthday_date.send_keys("19/10/2000")
    
    #password
    passsword = driver.find_element(By.ID,'password')
    passsword.send_keys("PFLIW296k5JI6mFLqjRKqzQA5YbOqJj9DoDR0")
    
    cbpgu = driver.find_element(By.NAME,'cgu')
    cbpgu.click()
    
    cbru = driver.find_element(By.NAME,'remember_username')
    cbru.click()
    
    driver.find_element(By.CLASS_NAME,'dl-button-label').click()

    
    time.sleep(1000000)
    
