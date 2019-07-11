'''
Created on Jun 13, 2019

@author: latikamehra
'''

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



username = "latika.mehra@gmail.com"
passwd = "Nitwit22"

'''
#adBlockExten = '~/Library/Application\ Support/Google/Chrome/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/3.48.0_0'

adBlockExten = '/Users/latikamehra/Work/3.48.0_0.zip'


# Configure the necessary command-line option.
options = webdriver.ChromeOptions()
options.add_argument('--load-extension='+adBlockExten)
driver = webdriver.Chrome("/Users/latikamehra/Work/chromedriver", chrome_options=options)
'''

driver = webdriver.Chrome("/Users/latikamehra/Work/chromedriver")

driver.get("https://tickets.cricketworldcup.com/ticketingInfo.html")

time.sleep(2)

login = driver.find_element_by_name('login')

login.send_keys(username)

time.sleep(2)

psw = driver.find_element_by_name('password')

psw.send_keys(passwd)

# Wait for reCaptcha to be manually circumvented

wait = WebDriverWait(driver, 200)
men_menu = wait.until(ec.visibility_of_element_located((By.NAME, "doUpdateSegmentInfo")))
ActionChains(driver).move_to_element(men_menu).perform()


nxt = driver.find_element_by_name('doUpdateSegmentInfo')
nxt.click()

time.sleep(2)

driver.get("https://tickets.cricketworldcup.com/showProduct.html?idProduct=410")

time.sleep(2)


def addTicketsToBasket():
    bronze = driver.find_element_by_xpath('//*[@id="showProductForm"]/div[1]/div[2]/div[11]/div/span[2]')
    bronze.click()
    bronze.click()
    
    basketAdd = driver.find_element_by_name('doAddToBasket')
    basketAdd.click()
    
    time.sleep(2)
    

counter = 0
while 1>0 :
    try :
        counter = counter+1
        print "Attempt #"+counter
        addTicketsToBasket()       
    except :
        try :
            driver.get("https://tickets.cricketworldcup.com/showProduct.html?idProduct=410")
            time.sleep(2)
            addTicketsToBasket()
            counter = counter+1      
        except :
            print "Tried getting the tickets following number of times : "+str(counter)
            break
    
    
    




