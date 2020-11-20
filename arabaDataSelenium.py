from selenium import webdriver
import time
from  openpyxl import *

arabaData = Workbook()
araba = arabaData.active
araba.append(["Model","Yıl","Km","Renk","Fiyat"])

browser = webdriver.Chrome("C://Users//Burak//Desktop//chromedriver")

for k in range(50,701,50):
    browser.get(f"https://www.sahibinden.com/bmw-5-serisi-520d/dizel/sahibinden?pagingOffset={k}&a3=33611&a3=33612&a3=33616&pagingSize=50&unpaintedParts=true&viewType=Classic&unchangingTracks=true")

    for i in range(1,52,1):
        if i == 5 or i == 4 or i==12:
            i +=1
            continue

        model=browser.find_element_by_class_name("searchResultsTagAttributeValue").text
        yil=browser.find_element_by_xpath(f"//*[@id='searchResultsTable']/tbody/tr[{i}]/td[4]").text
        km=browser.find_element_by_xpath(f"//*[@id='searchResultsTable']/tbody/tr[{i}]/td[5]").text
        renk=browser.find_element_by_xpath(f"//*[@id='searchResultsTable']/tbody/tr[{i}]/td[6]").text
        fiyat=browser.find_element_by_xpath(f"//*[@id='searchResultsTable']/tbody/tr[{i}]/td[7]/div").text
        araba.append([model,yil,km,renk,fiyat])
        
arabaData.save("araba.xlsx")
arabaData.close()

time.sleep(1)
browser.quit()



