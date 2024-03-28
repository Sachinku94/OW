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
    def test_logo(self):
        logonav="https://oncweekly.com/"

        logo=self.driver.find_element(By.XPATH,"//div[@id='ow-header-logo']/a")
        logolink=logo.get_attribute('href')
        logo.click()
        assert logolink==logonav
        logosource='https://oncweekly.com/wp-content/uploads/2023/02/OncWeekly-Logo_Final.svg'
        logoimg=self.driver.find_element(By.XPATH,"(//span[@class='et_pb_image_wrap ']/img)[1]")
        logosrc=logoimg.get_attribute('src')
        
        assert logoimg.is_displayed  
        assert logosource==logosrc
    def test_navbar(self):    

        navbar= self.driver.find_element(By.XPATH,"(//span[@class='mobile_menu_bar'])[1]")
        navbar.is_displayed
        navbar.click()

    def test_sociallink(self):
        sociallinks=[]
        
        allsociallinks=[]
        sociallinks.append('https://oncweekly.com/?llldldldl')
        pw=self.driver.find_element(By.XPATH,"//div/figure/a")
        assert pw.is_displayed
        pwlink=pw.get_attribute('href')
        sociallinks.append(pwlink)
        AC=ActionChains(self.driver)
        AC.key_down(Keys.CONTROL).click(pw).key_up(Keys.CONTROL).perform()
        

        social_links=self.driver.find_elements(By.XPATH,"//div[@class='social-icons']/ul/li/a")
        for lik in social_links:
            assert lik.is_displayed
            li=lik.get_attribute('href')

            sociallinks.append(li)
            AC.key_down(Keys.CONTROL).click(lik).key_up(Keys.CONTROL).perform()
        sub=self.driver.find_element(By.XPATH,"//a[@id='top-subscribe']")
        assert sub.is_displayed
        subhr=sub.get_attribute('href')
        sociallinks.append(subhr)
        AC.key_down(Keys.CONTROL).click(sub).key_up(Keys.CONTROL).perform()
        
        
        
        handles =self.driver.window_handles

        for windows in handles:
            self.driver.switch_to.window(windows)
            alllinks=self.driver.current_url
            allsociallinks.append(alllinks)
        

        assert set(sociallinks)==set(allsociallinks)



        

