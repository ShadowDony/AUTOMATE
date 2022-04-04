
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions() 
options.add_argument("--disable-blink-features")
driver = webdriver.Chrome(
    executable_path= '/Users/Yaroslav/Downloads/test/chromedriver'
)


driver.get('https://tarasmysko89.wixsite.com/vectortesttask01') 
driver.find_element_by_name('full-name').send_keys('Yaroslav')
driver.find_element_by_xpath('//*[@id="input_comp-k5hb1d85"]').send_keys('tqa3525@gmail.com')
driver.find_element_by_xpath('//*[@id="comp-jxd8gccw"]/button').click()

time.sleep(10)
driver.close()
driver.quit()