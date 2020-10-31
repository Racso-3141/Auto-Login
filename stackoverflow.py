from selenium import webdriver
from getpass import getpass

username = input("Enter your Email: ")
password = getpass("Enter your password: ")

driver = webdriver.Chrome('C:\\Users\\Oscar\\chromedriver.exe')
driver.get("https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f")

username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_id('submit-button')
login_button.submit()