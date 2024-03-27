from utilities.base_class import BaseClass

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class TestOne(BaseClass):
    def test_Storiestowatch(self):
        imglink=[]
        linksimg=[]
        wait=WebDriverWait(self.driver, 20)
        am=By.XPATH,'//h4[@class="meeting-view-header"]/a'
    
        img=wait.until(EC.presence_of_all_elements_located(am))
        for im in img:
         a=im.get_attribute("href")
         imglink.append(a)
        view=self.driver.find_element(By.XPATH,"(//div[@class='et_pb_text_inner']/p/a)[3]")
        view.click()
        time.sleep(10)
        ln=By.XPATH,'//h2[@class="entry-title"]/a'
        links=wait.until(EC.presence_of_all_elements_located(ln))
        for link in links:
           aa=link.get_attribute("href")
           linksimg.append(aa)
        

# Convert lists to sets and merge them
        unique_set = set(linksimg).union(set(imglink))


        assert len(unique_set)==8
    def test_mostrecent(self): 
        articles=[]
        article_1=[]
        wait=WebDriverWait(self.driver, 20)
        recent=By.XPATH,"//div/h2/a"
        recearticle=wait.until(EC.presence_of_all_elements_located(recent))
        
        for rec in  recearticle[:4]:
           r=rec.get_attribute("href")
           articles.append(r)
        view=self.driver.find_element(By.XPATH,"(//div[@class='et_pb_text_inner']/p/a)[3]")
        view.click()
        time.sleep(10)
        ln=By.XPATH,'//h2[@class="entry-title"]/a'
        links_1=wait.until(EC.presence_of_all_elements_located(ln))
        for lin in links_1:
           aa=lin.get_attribute("href")
           article_1.append(aa)
        

# Convert lists to sets and merge them
        unique = set(article_1).union(set(articles))


        assert len(unique)==9
        
    def test_Studies(self):
       all_studies=[]
       original_study=["LUNG CANCER","BREAST CANCER","GENITOURINARY CANCER","MELANOMA"]
       wait=WebDriverWait(self.driver, 20)
       study=By.XPATH,"//div[@class='post-categories']"
       studies=wait.until(EC.presence_of_all_elements_located(study))
       for stud in studies[4:8]:
          st=stud.text
          all_studies.append(st)
       assert all_studies==original_study

    def test_studiesarticles(self):
       mat=[]
       studies=[]
       canc=["https://oncweekly.com/oncweekly-content/?p=lung-cancer&type=research","https://oncweekly.com/oncweekly-content/?p=breast-cancer&type=research","https://oncweekly.com/oncweekly-content/?p=genitourinary-cancer&type=research"]
       wait=WebDriverWait(self.driver, 20)
       catarticle=By.XPATH,"//h2[@class='entry-title']/a"
       categ=wait.until(EC.presence_of_all_elements_located(catarticle))
       for cat in categ[8:11]:
          ca=cat.get_attribute("href")
          studies.append(ca)
       for stt in canc:
        self.driver.get(stt)
        time.sleep(5)
        atc=By.XPATH,"(//h2[@class='entry-title']/a)[1]"
        atrc=wait.until(EC.presence_of_element_located(atc))
        atrcc=atrc.get_attribute("href")
        mat.append(atrcc)
       assert studies==mat

    def test_Navigationbar(self):
       Navlink=[]
       windowslink=[]
       AC=ActionChains(self.driver)
       DropDown=self.driver.find_element(By.XPATH,"(//ul/li/a)[20]")
       Navigation=self.driver.find_elements(By.XPATH,"//ul/li/a")
       for Nav in Navigation[19:30]:
        AC.move_to_element(DropDown)

        AC.key_down(Keys.CONTROL).click(Nav).key_up(Keys.CONTROL).perform()

       for tab in Navigation[30:33]:
        AC.key_down(Keys.CONTROL).click(tab).key_up(Keys.CONTROL).perform()

       for all in Navigation[19:33] :
          al=all.get_attribute("href")
          Navlink.append(al)

      
       handles =self.driver.window_handles

       for windows in handles:
         self.driver.switch_to.window(windows)
         alllinks=self.driver.current_url
         windowslink.append(alllinks)
       for wind in windowslink:
         assert wind.__contains__("https://oncweekly.com/")


       assert len(windowslink)== 15

    

        


      



      
        



       

       

       

              
       
            


       
        
    
        
        

        
