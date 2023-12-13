from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

chrome_options = webdriver.ChromeOptions()
# path to Chrome browser executable
chrome_options.binary_location = 'C:/pathto/chrome.exe'

# path to ChromeDriver executable
driver_path = '/pathto/chromedriver'

# Set the path to the ChromeDriver using executable_path in ChromeOptions
chrome_options.add_argument(f"webdriver.chrome.driver={driver_path}")

# Initialize the Chrome driver with ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# driver.get(url)
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts,executable_path="/jenif/Documents/Projects/Python/chromedriver")

# Open the website
driver.get('https://dashboard.subsplash.com/-d/#/library/media')

# login
time.sleep(3)

driver.find_element(By.ID, "email").click()
# switch frames and login
#driver.switch_to.frame(0)

# Read username and password from file
with open("user.txt", "r") as file:
    user_data = file.readline().strip().split(";")

# enter login info
if len(user_data) == 2:  # Ensure the file format is correct
    username, password = user_data
    driver.find_element(By.ID, 'email').send_keys(username)
    driver.find_element(By.ID, 'password').send_keys(password)
else:
    print("Invalid format in user.txt. Please use 'username;password' format.")

# click login
driver.find_element(By.XPATH, "/html/body/div/main/div/form/button").click()
time.sleep(10)

# go to media page
driver.get('https://dashboard.subsplash.com/-d/#/library/media')
time.sleep(5)

# Find the file input element by its ID
file_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/label/input')

directory = "Sermons"
files = os.listdir(directory)

if files:  # Check if there are files in the directory
    file_path = os.path.abspath(os.path.join(directory, files[0]))
    # print("File path of the first file:", file_path)
else:
    print("The directory is empty.")
    
# check which file's currently being uploaded
print("File path of the first file:", file_path)

# Upload the file by sending keys with the file path
file_input.send_keys(file_path)

# let the browser wait 24 hours to avoid auto-closing before upload is completed
time.sleep(86400)
# # Close the browser
# # driver.quit()
