from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import csv 
from sites.doctolib import check_doctolib_registration

def setup_driver():
    opt = Options()
    # opt.add_argument('-headless')
    s = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=s, options=opt)
    return driver

def main(email_list):
    results = []

    for email in email_list:
        driver = setup_driver() # Créez une nouvelle instance du navigateur pour chaque email
        doctolib_registered = check_doctolib_registration(driver, email)
        print(doctolib_registered)
        driver.quit() # Fermez le navigateur après chaque vérification
        # Ajouter le résultat à la liste
        results.append([email, doctolib_registered])

    # Exporter les résultats en CSV
    with open('resultats_inscription.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Email','Doctolib'])
        writer.writerows(results)

if __name__ == "__main__":
    email_list = ["exemple1@email.com", "exemple2@email.com", "exemple3@email.com"] 
    main(email_list)
