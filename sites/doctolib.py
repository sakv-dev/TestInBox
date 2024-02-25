import time
from selenium.webdriver.common.by import By
import random
from selenium.common.exceptions import NoSuchElementException



number_list= ['0628436936','0611739434','0738168474','0754657472', '0613763374', '0699656374']

def check_doctolib_registration(driver, email):
    driver.get("https://www.doctolib.fr/sessions/new?context=navbar")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]').click()

    driver.find_element(By.CSS_SELECTOR,'.dl-button-tertiary-primary > span:nth-child(1)').click()

   
    #phone
    phone_input = driver.find_element(By.ID, 'phone_number')
    phone_input.send_keys(random.choice(number_list)) #phone factice
    
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
    
    # cbru = driver.find_element(By.NAME,'remember_username')
    # cbru.click()
    driver.find_element(By.CSS_SELECTOR,'.dl-button-primary > span:nth-child(1)').click()
    time.sleep(2)
    
    driver.find_element(By.CSS_SELECTOR, ".dl-modal-footer > button:nth-child(2)").click()
    
    time.sleep(1)
    result = ""
    current_url = driver.current_url
    if current_url == "https://www.doctolib.fr/account/marketing_consent/new":
        result = "False"
    else:
        span_element = driver.find_element(By.CSS_SELECTOR, "span.dl-text-body.dl-text-regular.dl-text-s")
        text_recup = span_element.text
        
        if text_recup == "Désolé, une erreur est survenue." or text_recup == "Un compte Doctolib a déjà été créé avec ce numéro de téléphone.":
            result = "False"
        elif text_recup == "Un compte Doctolib a déjà été créé avec cette adresse e-mail." or text_recup == "Un compte Doctolib a déjà été créé avec cette adresse e-mail. Un compte Doctolib a déjà été créé avec ce numéro de téléphone.":
            result = "True"
              
    return result
        
    
