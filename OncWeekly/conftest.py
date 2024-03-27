import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

import time

@pytest.fixture(scope="class")
def setup(request):
    driver= webdriver.Chrome()
    request.cls.driver=driver
    
    driver.get("https://oncweekly.com/?llldldldl")

    time.sleep(5)

    driver.maximize_window()
    time.sleep(5)
    # try:
    #   driver.find_element(By.XPATH,"//button[@class='align-right secondary slidedown-button']").click()
    # except NoSuchElementException:
    #    ()
    yield
    driver.close()