from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path = r"C:\dchrome\chromedriver.exe")

# Navega a la URL
driver.get("http://www.google.com")
time.sleep(3)
driver.find_element_by_name("q").send_keys("Hola")
time.sleep(3)
driver.quit()