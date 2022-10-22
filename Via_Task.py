from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(executable_path="C://chrom-driver/chromedriver.exe")
driver.get("https://www.demoblaze.com/")
driver.maximize_window()

#Log In
def LogIn():
    time.sleep(5)
    LogIn="Log in"
    Nav_Items=driver.find_elements(By.XPATH,'//li[@class="nav-item"]//a')
    Filtered_Nav_Item=[ item for item in Nav_Items  if item.text==LogIn][0]
    print(Filtered_Nav_Item)
    Filtered_Nav_Item.click()
    time.sleep(5)
    Log_In_User_Name=driver.find_element(By.XPATH,'//input[@id="loginusername"]').send_keys('riki m ')
    Log_In_Password=driver.find_element(By.XPATH,'//input[@id="loginpassword"]').send_keys('17032002')
    time.sleep(5)
    Save_Log_In=driver.find_elements(By.XPATH,'//button[@class="btn btn-primary"]')
    print(Save_Log_In)
    time.sleep(5)
    Filtered_Save_Log_In_Item=[ item for item in Save_Log_In  if item.text==LogIn][0]
    Filtered_Save_Log_In_Item.click()
    time.sleep(4)


LogIn()


def GetNexus():
    time.sleep(4)
    #check id = 3
    try:
        Find_Elem = driver.find_element(By.XPATH, '//a[contains(@href,"prod.html?idp_=3")]')
    except:
       print("The Product Not Exist")
       return
    time.sleep(2)
    Href=Find_Elem.get_attribute('href')
    driver.get(Href)
    time.sleep(5)
    Add_To_Cart=driver.find_elements(By.XPATH,'//a[@class="btn btn-success btn-lg"]')[0]
    print(Add_To_Cart)
    time.sleep(2)
    Add_To_Cart.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    cart=driver.find_elements(By.XPATH,'//a[@id="cartur"]')[0]
    cart.click()

GetNexus()

def CheckCart():
    time.sleep(5)
    Item = driver.find_elements(By.XPATH, '//tr[@class ="success"]')
    print(len(Item))

    if len(Item)!=1:
       raise Exception("Sorry, There Is More Than 1 Item In The Cart")

    Price=driver.find_elements(By.XPATH, '//tr[@class ="success"]//td')[2].get_attribute('innerHTML')
    print(Price)

    if Price!="650":
        raise Exception("Sorry, The Price Is Not Correct")

    Title=driver.find_elements(By.XPATH, '//tr[@class ="success"]//td')[1].get_attribute('innerHTML')
    print(Title)

    if Title!="Nexus 6":
        raise Exception("Sorry, The Title Is Not Correct")




CheckCart()