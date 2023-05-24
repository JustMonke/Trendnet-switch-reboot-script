from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Start the browser in headless + silent mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('log-level=3')
driver = webdriver.Chrome(service_log_path='NUL', options=options)
#Fill in switch IP address
driver.get("http://192.168.18.91")

#Fill in username and password
Login = driver.find_element(By.NAME, "Login")
Login.send_keys("admin")
Password = driver.find_element(By.NAME, "Password")
Password.send_keys("password" + Keys.ENTER)

#Navigate to reboot tab
Tools = driver.find_element(By.CSS_SELECTOR, "div.menuheader:nth-child(27)")
Tools.click()
Reboot = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/table/tbody/tr/td[1]/div/div/div[1]/div/div/ul[14]/li[5]/a")
driver.execute_script("arguments[0].scrollIntoView();", Reboot)
Reboot.click()

#Switch to the correct frame
iframe = driver.find_element(By.XPATH, "//*[@id='myframe']")
driver.switch_to.frame(iframe)

#Reboot the switch (remove comment for Apply.click to enable)
Apply = driver.find_element(By.CSS_SELECTOR, ".button1")
#Apply.click()
driver.quit()
