
import csv
import os #pathing
from selenium import webdriver
from selenium.webdriver import *
from selenium.webdriver.common.by import By #find element from by
import time #slow down time
import re #search through strings


#relative file paths
userprofile = os.environ['USERPROFILE']

#chrome driver prerequesites
driverpath = os.path.join(userprofile, 'Documents', 'GitHub', 'ExtraCodingThings', 'chromedriver_win32', 'chromedriver.exe')
print("chrome driver path is " + str(driverpath))

opts = webdriver.ChromeOptions()
opts.add_argument("--window-size=800,600")
opts.add_argument('--ignore-certificate-errors')
opts.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(driverpath, options=opts)

driver.get('https://quizlet.com/590483974/list-43-flash-cards/')

time.sleep(5)



def_and_word = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/div[2]/div/div[1]/div[3]/div[2]/div/div[2]/div/div/section/div/section/div[1]/div/div/div[1]/div/div[1]/div/a/spa.getText()
print(def_and_word)
#class="SetPageTerms-termsList"
#TermText notranslate lang-en


