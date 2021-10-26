from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from barnum import gen_data
from time import sleep

import names
import random
import string

#install smua modulnya
#python maple.py

def makeCode():
    pondev = webdriver.Chrome("D:/bot/chromedriver_win32/chromedriver")
    # set path ke dir spesifik file chromedriver anda 
    letters = string.ascii_lowercase
    mailRand = ''.join(random.choice(letters) for i in range(6))+'@mailsac.com'
    # membuat random mail 
    urlreg = 'https://www.maplesoft.com/products/maple/free-trial/'
    getlink = 'https://mailsac.com/inbox/'
    # untuk menerima link aktivasi maple

    pondev.get(urlreg)
    pondev.find_element_by_xpath("//input[@id='FirstName']").send_keys(names.get_first_name())
    pondev.find_element_by_xpath("//input[@id='LastName']").send_keys(names.get_last_name())
    pondev.find_element_by_xpath("//input[@id='EmailAddress']").send_keys(mailRand)
    pondev.find_element_by_xpath("//input[@id='Company']").send_keys(gen_data.create_company_name())
    pondev.find_element_by_xpath("//input[@id='JobTitle']").send_keys(gen_data.create_job_title())
    
    CountryDropDownList=Select(pondev.find_element_by_xpath("//*[@id='CountryDropDownList']"))
    CountryDropDownList.select_by_visible_text("United States")
    pondev.implicitly_wait(5) 
    # menunggu 4 detik untuk meload list region
    pondev.find_element_by_xpath("//option[@value='CA  ']").click() 
    pondev.find_element_by_xpath("//*[@id='SegmentRadioButtonList_3']").click() 
    pondev.find_element_by_xpath("//*[@id='chkAgreeToGDPR']").click() 
    pondev.find_element_by_xpath("//*[@id='txtInstructorName']").send_keys(names.get_full_name(gender='male'))
    pondev.find_element_by_xpath("//*[@id='txtCourse']").send_keys('Algebra')
    pondev.find_element_by_xpath("//*[@id='SubmitButton']").click()
    pondev.implicitly_wait(10) 
    
    pondev.get(getlink+mailRand)
    # membuka inbox email 
    pondev.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div/table/tbody/tr[2]/td[3]").click() 

    # membuka link yang berisi kode aktivasi dan mendapatkan code aktivasi 
    lastopen = pondev.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div/table/tbody/tr[2]/td[2]/div[2]/p[3]/a").get_attribute("innerHTML").splitlines()[0]
    pondev.get(lastopen)
    pondev.get(lastopen)
    sleep(3)
    exp = pondev.find_element_by_xpath("//*[@id='evaluationExpiry']").text
    Acode = pondev.find_element_by_xpath("//span[@id='evaluationPurchaseCode']").text
    print('\n')
    print('Activation code : '+Acode)
    print('Your evaluation will expire in '+str(exp))
    print('\n')


makeCode()
