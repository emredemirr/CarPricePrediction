# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:40:27 2020

@author: Emre Demir
"""

# Gerekli olan kutuphanelerin import edilmesi
import time
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from  openpyxl import Workbook, load_workbook

# Request atilirken gerekli olan parametreler
headers_param = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36"}

# Özelliklerin Tutulduğu Dizilerin tanımlanması
modelDizi = []
fiyatDizi = []
uretimyiliDizi = []
kmDizi = []
renkDizi=[]

# veri dosyasi 
dosya = Workbook()
sayfa = dosya.active
sayfa.title="Ön İşleme Öncesi Veri Seti"
sayfa.append(["Model","Renk","Yıl","Kilometre","Fiyat"])

# Sayfalara request atıp parse edilmesi
for paging in range(0, 951, 50):
    time.sleep(2)
    sahibinden = requests.get(f"https://www.sahibinden.com/hyundai-accent-blue-1.6-crdi/sahibinden?pagingOffset={paging}&a3=33611&a3=33612&a3=33616&pagingSize=50", headers=headers_param)
    araba = sahibinden.content
    soup = BeautifulSoup(araba,"html.parser")
    
#Model verisinin çekilip diziye aktarılması
    modeller = soup.find_all("td",{"class":"searchResultsTagAttributeValue"})
    for model in modeller:
        modelDizi.append(model.text.replace(" ",""))
        
#Üretim yılı, km ve renk verilerinin dizilere aktarılması
    ozellikler= soup.find_all("td",{"class":"searchResultsAttributeValue"})
    for ozellik in range(0, len(ozellikler), 3):
        uretimyiliDizi.append(ozellikler[0+ozellik].text.replace(" ", ""))
        kmDizi.append(ozellikler[1+ozellik].text.replace(" ", ""))
        renkDizi.append(ozellikler[2+ozellik].text.replace(" ", ""))
        
# Fiyat verisinin çekilip diziye aktarılması        
    fiyatlar= soup.find_all("td",{"class":"searchResultsPriceValue"})
    for fiyat in fiyatlar:
        fiyatDizi.append(fiyat.text.replace(" ", ""))

# Verilerin dosyaya yazdırılması
for modeli,renk,yil,km,fiyat in zip(modelDizi,renkDizi,uretimyiliDizi,kmDizi,fiyatDizi):
    sayfa.append([modeli,renk,yil,km,fiyat])

dosya.save("arabaDataset.xlsx")
dosya.close()