from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def findByXPATH(driver: any, Xpath: str) -> WebDriverWait:
    return driver.find_element(By.XPATH, Xpath)
    
def findByCSS(driver: any, CSS: str) -> WebDriverWait:
    return driver.find_element(By.CSS_SELECTOR, CSS)