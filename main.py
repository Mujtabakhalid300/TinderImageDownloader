from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import *
from selenium.webdriver.common.action_chains import ActionChains
import requests
import os
import lxml
import urllib.request

# starting up selenium


ser = Service("chromedriver.exe")
driver = webdriver.Chrome(service=ser)
action = ActionChains(driver)


# opening tinder.com

driver.get("https://tinder.com/")
sleep(5)


# manually login here and enter y



# You will manually do the login
# this is because tinder changes its api every month
# it will be outdated if i setup an auth token bot

# manually login now
# if you have successfully logged in then enter y

LoginConfirm=input("Type y when done with login and you are on the main page: ")
i=1
links = []
if LoginConfirm=="y":
    while i<10:

        # rest of the script will be in here
        sleep(2)


        #taking page source and extracting the image element
        pagehtml = driver.page_source
        soup = BeautifulSoup(pagehtml, "lxml")

        # Getting the http from style attribute

        div = soup.find("div", {"class": "Bdrs(8px) Bgz(cv) Bgp(c) StretchedBox"})
        tag = div["style"]
        sleep(2)
        # getting link from the tag

        tag = tag.partition('"')
        tag = tag[2].partition('"')
        print(tag[0])
        links.append(tag[0])

        sleep(3)
        action.send_keys(Keys.ARROW_LEFT)
        action.perform()
        i+=1
        print(i)

    driver.quit()

    # using urllib to download images

    for i in range((len(links))):
        #using urllib.requests.urlretreive to download image into a file
        urllib.request.urlretrieve(links[i], f"image{links.index(i)}.jpeg")




















input("")