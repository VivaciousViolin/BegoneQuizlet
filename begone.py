

#this file is retired because I rage quit and restarted but it is here for reference sooooo

##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################
##########################################################################################

#import selenium
import csv
import os #pathing
from selenium import webdriver
from selenium.webdriver import *
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait #downloading and clicking
"""
import time #slow down time
import re #search through strings


#relative file paths
userprofile = os.environ['USERPROFILE']

#chrome driver prerequesites
driverpath = os.path.join(userprofile, 'Documents', 'GitHub', 'ExtraCodingThings', 'chromedriver_win32', 'chromedriver.exe')
print("chrome driver path is " + str(driverpath))

opts = webdriver.ChromeOptions()
opts.add_argument('--disable-extensions')
driver = webdriver.Chrome(options=opts)

"""
chrome_options = Options()
chrome_options.add_argument("--window-size=800,600")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=chrome_options)
"""


driver.get('https://quizlet.com/590483974/list-43-flash-cards/')

time.sleep(456)










































"""
import requests
import browser_cookie3 #grab cookie, mmm mmm
from fake_useragent import UserAgent #mmm much user agent

#user agent prerequesites
ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
print(header)

#get cookies to the site to login
def get_cookie():

    url = "https://quizlet.com/590483974/list-43-flash-cards/"
    cj = browser_cookie3.chrome(domain_name='https://quizlet.com/')
    response = requests.get(url, headers=header)
    print(response)

get_cookie()
"""