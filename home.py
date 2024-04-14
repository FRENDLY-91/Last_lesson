from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
time.sleep(1)
driver.execute_script("window.scrollBy(0,600);")
btn_sel_ruby = driver.find_element_by_css_selector('[title="Selenium Ruby"]')
btn_sel_ruby.click()
time.sleep(1)
tab_rev = driver.find_element_by_css_selector('[href="#tab-reviews"]')
tab_rev.click()
time.sleep(1)
driver.execute_script("window.scrollBy(0,800);")
five_stars = driver.find_element_by_class_name('star-5')
five_stars.click()
time.sleep(1)
rev_text = driver.find_element_by_id('comment')
rev_text.send_keys('Nice book!')
name_text = driver.find_element_by_id('author')
name_text.send_keys('Alex')
email_text = driver.find_element_by_id('email')
email_text.send_keys('example_Alex@email.com')
time.sleep(2)
submit_btn = driver.find_element_by_id('submit')
submit_btn.click()
time.sleep(2)
driver.quit()