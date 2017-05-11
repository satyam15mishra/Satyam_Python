#This script is made by Satyam Mishra.
#This works on Mozilla Firefox

from selenium import webdriver
import time

count = int(raw_input("Enter the number of times the video must be played: "))
print "Enter the time duration of the video: "
minutes = int(raw_input("Minutes: "))
seconds = int(raw_input("Seconds: "))

url = raw_input("Enter the url (no https://): ")

refresh_rate = minutes * 60 + seconds

driver = webdriver.Firefox()
driver.get(url)

for i in range(count):
    time.sleep(refresh_rate)
    driver.refresh()
