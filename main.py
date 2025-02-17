from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


option = webdriver.ChromeOptions()
option.add_argument("--force-device-scale-factor=0.25")  
option.add_argument("--high-dpi-support=1")
driver = webdriver.Chrome(options=option)
driver.get("https://monlycee.net/")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id= \"container\"]/app-header/header/p[3]/a"))).click()

username =""
mdp = ""

username_field = driver.find_element(By.ID, "username")
password_field = driver.find_element(By.ID, "password")
username_field.send_keys(username)
password_field.send_keys(mdp)
password_field.send_keys(Keys.ENTER)
time.sleep(2)

pronote_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="services"]/ul/li[4]/div/a'))) 
pronote_link.click() 

time.sleep(2)

window_handles = driver.window_handles
driver.switch_to.window(window_handles[-1])
pronote_note = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'GInterface.Instances[0].Instances[1]_Combo2')))
pronote_note.click()

time.sleep(5)
saucecurry = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//span[text() = "Par matière"]')))
saucecurry.click()

def fairemoyenne():
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    results = soup.find_all('div',{"class":"ie-titre-gros"})
    if len(results) != 0: 
        total = 0
        for result in results : 
            note_text = result.get_text().strip()
            if note_text != "Abs":
                notes =float(result.get_text().replace(",","."))
                total = total + notes
        moyenne = total/(len(results))
        new_moy = round(moyenne,2)
        print("Votre moyenne est de",new_moy)
        driver.quit()
    else: 
        print('Le trimestre ne contient aucune note...')
        driver.quit()


get_trimestre = int(input('Veuillez entrez un trimestre(1,2,3) : '))
if get_trimestre == 2:
    triangle = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,'ocb_bouton')))
    triangle.click()
    trimestre2 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'GInterface.Instances[2].Instances[0]_1')))
    trimestre2.click()
    time.sleep(0.5)
    fairemoyenne()
elif get_trimestre == 1:
    triangle = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,'ocb_bouton')))
    triangle.click()
    time.sleep(2)
    trimestre1 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'GInterface.Instances[2].Instances[0]_0')))
    trimestre1.click()
    time.sleep(0.5)
    fairemoyenne()
elif get_trimestre == 3:
    triangle = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,'ocb_bouton')))
    triangle.click()
    time.sleep(0.5)
    trimestre3 = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.ID,'GInterface.Instances[2].Instances[0]_2')))
    trimestre3.click()
    time.sleep(0.5)
    fairemoyenne()



