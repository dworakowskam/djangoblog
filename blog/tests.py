from selenium import webdriver
import time


driver = webdriver.Firefox()
driver.get(url='http://127.0.0.1:8000/admin')

def element_is_clickable():
    driver.find_element_by_xpath('//*[@id="id_username"]').send_keys("md")
    driver.find_element_by_xpath('//*[@id="id_password"]').send_keys("kupa")
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div/form/div[3]/input').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/div[1]/div[2]/a[1]').click()
    driver.find_element_by_xpath('/html/body/nav/div/a/span').click()
    
#element_is_clickable()

def respons_check(w, file):
    height = 768
    driver.set_window_size(w, height)
    driver.save_screenshot(file)
    
respons_check(900, "test900.png")
respons_check(1200, "test1200.png")
respons_check(1800, "test1800.png")
respons_check(600, "test600.png")