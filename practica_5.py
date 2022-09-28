import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path="D:\Documents\chromedriver.exe")


  ###  REGISTRO ##
driver.get("https://www.demoblaze.com/index.html")

driver.maximize_window()
time.sleep(1)
driver.find_element(By.ID, "signin2").click()
time.sleep(1)
usuario = driver.find_element(By.ID, "sign-username")
time.sleep(1)
contra = driver.find_element(By.ID, "sign-password")
time.sleep(1)

usuario.send_keys("Fumito10")
time.sleep(1)
contra.send_keys("Alucard-10")
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="signInModal"]/div/div/div[3]/button[2]').click()
time.sleep(1)

alert = Alert(driver)
alert.accept()
time.sleep(1)

driver.find_element(By.XPATH, ('//*[@id="signInModal"]/div/div/div[3]/button[1]')).click()
time.sleep(1)

### INGRESO  ##

driver.find_element(By.ID, "login2").click()
time.sleep(1)

usu = driver.find_element(By.ID, "loginusername")
time.sleep(1)
con = driver.find_element(By.ID, "loginpassword")
time.sleep(1)

usu.send_keys("Fumito10")
time.sleep(1)
con.send_keys("Alucard-10")
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]').click()
time.sleep(1)

### elegir dos productos de cada categoria ##

##driver.find_element(By.XPATH, "itemc").click()
##time.sleep(1)




#driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[1]/div/a').click()
#time.sleep(1)

#driver.find_element(By.XPATH, '//*[@id="tbodyid"]/div[2]/div/a').click()
#time.sleep(1)

#alert.accept()

#driver.back()