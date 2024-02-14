from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import csv 
# from sites.amazon import check_amazon_registration
from sites.doctolib import check_doctolib_registration


def setup_driver():
    opt = Options()
    # opt.add_argument('-headless')
    s = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=s, options=opt)
    return driver

def main(email_list):
    driver = setup_driver()
    results = []

    for email in email_list:
    
        
        # Vérifiez l'inscription sur Doctolib
        doctolib_registered = check_doctolib_registration(driver, email)
        
        # Ajouter le résultat à la liste
        results.append([email, doctolib_registered])

    driver.quit()
    
    # Exporter les résultats en CSV
    with open('resultats_inscription.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Email','Doctolib'])
        writer.writerows(results)

if __name__ == "__main__":
    email_list = ["exemple1@email.com", "exemple2@email.com", "exemple3@email.com"]
    main(email_list)
