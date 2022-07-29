from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def untilClickableXPATH(driver: any, Xpath: str, time = 3) -> WebDriverWait:
    return WebDriverWait(driver, time).until(expected_conditions.element_to_be_clickable((By.XPATH, Xpath)))

def untilSelectableXPATH(driver: any, Xpath: str, time =  3) -> WebDriverWait:
    return WebDriverWait(driver, time).until(expected_conditions.element_to_be_selected((By.XPATH, Xpath)))

def untilVisibleXPATH(driver: any, Xpath: str,  time = 3) -> WebDriverWait:
    return WebDriverWait(driver, time).until(expected_conditions.visibility_of_element_located((By.XPATH, Xpath)))

def untilClickableCSS(driver: any, CSS: str, time = 3) -> WebDriverWait:
    return WebDriverWait(driver, time).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, CSS)))