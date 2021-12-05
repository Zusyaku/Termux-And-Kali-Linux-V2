from selenium import webdriver	 
#author : Sayyed Viquar Ahmed 
# For using sleep function because selenium 
# works only when the all the elements of the 
# page is loaded. 
import time 
import schedule as sc
from selenium.webdriver.common.keys import Keys 

# Creating an instance webdriver 
def hetcollegeconnected():
    browser = webdriver.Chrome() 
    for i in range(0,10):
        print("Connecting with the COllege Server...")
   ## Replace it with your collge website    // replace it with your college 😅😅

# Let's the user see and also load the element 
    time.sleep(2) 

    print("Successfully COnnected with College Server")
    username=str(input("Enter your username"))
    password=str(input("Enter your password"))
    browser .find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div[2]/p[1]/form/div/input").send_keys(username)
    browser .find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div[2]/p[1]/form/div/di        v[2]/input").send_keys(password)
    browser .find_element_by_xpath("/html/body/div/div[1]/div/div/div[2]/div/div[2]/p[1]/form/button").click()  
        ans=str(input("Do you want to close th browser ?"))

    if ans =="yes" or ans=="YES":
        browser.close()

    
if __name__ == '__main__':
    sc.every().day.at("21:00").do(hetcollegeconnected())
