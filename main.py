from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import json
from sites.doctolib import check_doctolib_registration
from sites.google import check_google_registration

def setup_driver():
    opt = Options()
    s = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=s, options=opt)
    return driver

def main(email_list, marque):
    # Initialisation du dictionnaire de résultats avec la marque comme clé principale
    results = {marque: {}}

    for email in email_list:
        driver = setup_driver()
        doctolib_registered = check_doctolib_registration(driver, email)
        google_registered = check_google_registration(driver, email)
        
        driver.quit()

        # Simuler les résultats pour les autres services, ici on ne fait que Doctolib
        results[marque][email] = {
            #"Doctolib": doctolib_registered == "True",
            "Google":  google_registered == "True"
            # Ajouter ici les autres services si nécessaire
        }

    # Exporter les résultats en JSON
    with open('resultats_inscription.json', 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    email_list = ["lenono132@gmail.com", "adresse2@gmail.com"]
    marque = "Logitech" # Entreprise du contrat
    main(email_list, marque)
