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
    def test_Duimg(self):
        source=[]
        wait=WebDriverWait(self.driver, 20)
        self.driver.get("https://oncweekly.com/category/latest-research/?jfkdkdk")
        self.driver.find_element(By.XPATH,"(//h2[@class='entry-title']/a)[1]").click()
        img=By.XPATH,"//div/div/a/img"
        img=wait.until(EC.presence_of_all_elements_located(img))
        for im in img:
            src=im.get_attribute('src')
            source.append(src)

        sourceset=set(source)
        assert len(sourceset)==len(img)



