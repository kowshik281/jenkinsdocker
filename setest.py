from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("C:\chromedriver")
action = ActionChains(driver)
driver.get("http://127.0.0.1:8000/")
import time
driver.find_element_by_id('1').click()

driver.find_element_by_name('pn').send_keys("koushik")
time.sleep(1)
driver.find_element_by_name('sn').send_keys("laddu")
time.sleep(1)
driver.find_element_by_name('num').send_keys("20")
time.sleep(1)
driver.find_element_by_id('3').click()
time.sleep(3)
driver.find_element_by_id('4').click()
time.sleep(3)

driver.find_element_by_id('2').click()


