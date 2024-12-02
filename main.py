from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import re 

website = 'https://shikshan.org/colleges-courses/colleges-engineering/1/'
driver = webdriver.Chrome()

name = []
address = []
contact_no =[]
email = []

for i in range(252):
  try:
      driver.get(f'https://shikshan.org/colleges-courses/colleges-engineering/{i+1}/')
      elements = driver.find_elements(By.XPATH,'//div[@class="ebl"]')
      for element in elements:
        college_name = element.find_element(By.XPATH,'./a').text
        name.append(college_name)
        college_address = element.find_element(By.XPATH,'./div[2]').text
        address.append(college_address)
        if len(element.find_elements(By.XPATH,'./div/span[@class="crlist"]')) >1:          
          college_contact_number = element.find_element(By.XPATH,'./div/span[@class="crlist"][1]').text
          college_contact_number = college_contact_number.split(":")[1].strip()
          college_email = element.find_element(By.XPATH,'./div/span[@class="crlist"][2]').text
          college_email  = college_email .split(":")[1].strip()
        else:
          college_contact_number = 'NA'
          college_email = element.find_element(By.XPATH,'./div/span[@class="crlist"][1]').text
          college_email  = college_email .split(":")[1].strip()
        contact_no.append(college_contact_number)
        email.append(college_email)
        print(college_contact_number,college_email)
        #print(college_email)
        #college_contact_number = element.find_element(By.XPATH,'./div[3]/span[@class="crlist"][1]')         
        #print(college_contact_number)
      time.sleep(5)
  except Exception as e:
      print("An error occurred:", e)

df = pd.DataFrame({'Name':name,'Address':address,'Contact no.':contact_no,'Email':email})
df.to_csv('shikshan.csv',index=False)

driver.quit()