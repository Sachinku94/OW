from utilities.base_class import BaseClass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
imglink=[]
linksimg=[]
driver.get("https://oncweekly.com/?llldldldl")

time.sleep(5)
driver.maximize_window()
time.sleep(5)
    
wait=WebDriverWait(driver, 20)
am=By.XPATH,"//div[@class='full-mblog-img-box']"
    
img=wait.until(EC.presence_of_all_elements_located(am))
for im in img:
  
  a=im.get_dom_attribute("href") 
  imglink.append(a)
  vi=By.XPATH,"(//div[@class='et_pb_text_inner']/p/a)[3]"
  view=wait.until(EC.presence_of_element_located(vi))
  view.click()
  time.sleep(10)
  ln=By.XPATH,"//div[@class='post-media']/a"
  links=wait.until(EC.presence_of_all_elements_located(ln))
  for link in links:
     aa=link.get_dom_attribute("href")
     linksimg.append(aa)
        
print(imglink)
print(linksimg)
# Convert lists to sets and merge them
unique_set = set(linksimg).union(set(imglink))
# assert len(unique_set)==4
           