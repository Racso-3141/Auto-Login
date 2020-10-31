from selenium import webdriver
from getpass import getpass

username = input("Enter your Email: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome('C:\\Users\\Oscar\\chromedriver.exe')
driver.get("https://discord.com/login")

username_textbox = driver.find_element_by_name("email")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
login_button.submit()