from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

driver = webdriver.Edge()


def spam():
    while True:
        #True Line:driver.get('https://studip.uni-hannover.de/dispatch.php/course/statusgroups/join/a59f051eb2da38f164610a99da68038c?cid=2d6d18040920a5d8afd036242d1c9f8c')
        driver.get('https://studip.uni-hannover.de/dispatch.php/course/statusgroups/join/e8eb04c768a4b4ae920f6122314c156b?cid=0ee057761aa44f9e09a06d3bdbd802c1')
        time.sleep(0.25)




print("Welcome to the PayToDrin")
print("Input the time you need to sign in:")

hour = int(input("Hour:"))
minute = int(input("Minute:"))

now = datetime.datetime.now().time()
now_hour = now.hour
now_minute = now.minute
now_seconds = now.second

print('Now', now_hour)

ACTIVE = True

while ACTIVE:
    print(f"NowHour: {now_hour}, Hour: {hour}, Now_minute: {now_minute}, Minute: {minute}, Now_seconds: {now_seconds}")
    if now_hour == hour and now_minute == minute-1 and now_seconds >= 55:
        spam()
    else:
        now = datetime.datetime.now().time()
        now_hour = now.hour
        now_minute = now.minute
        now_seconds = now.second

    time.sleep(0.5)

# Etech: https://studip.uni-hannover.de/dispatch.php/course/statusgroups?cid=2d6d18040920a5d8afd036242d1c9f8c&contentbox_open=a59f051eb2da38f164610a99da68038c#a59f051eb2da38f164610a99da68038c

#https://studip.uni-hannover.de/dispatch.php/course/statusgroups/join/a59f051eb2da38f164610a99da68038c?cid=2d6d18040920a5d8afd036242d1c9f8c
