# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:40:27 2020

@author: Emre Demir
"""
# Gerekli olan kutuphanelerin import edilmesi.
import pandas as pd
from  openpyxl import *
from sklearn.preprocessing import LabelEncoder,OneHotEncoder



dosya=load_workbook("arabaDataset.xlsx")
sayfa2 = dosya.active
dataset = pd.read_excel("arabaDataset.xlsx")

#Fiyat verisinin sonundaki gereksiz veriyi siler.
dataset.dropna(inplace = True)  
basla, dur, adim = 0, -4, 1
dataset["Fiyat"]= dataset["Fiyat"].astype(str) 
dataset["Fiyat"]=dataset["Fiyat"].str.slice(basla, dur, adim)

# Fiyat verisini string türünden float türüne çevirir.
fiyat=pd.DataFrame(data=dataset["Fiyat"])
fiyat = fiyat.astype(float)
dataset["Fiyat"]=fiyat


#Renk ve Model sütunundaki verilerin seçilmesi
renkC = dataset.iloc[:,1:2].values
modelC = dataset.iloc[:,0:1].values


renkdf=pd.DataFrame(renkC)
modeldf=pd.DataFrame(modelC)

#Sayısal verilere dönüştürür.
lblencoder= LabelEncoder()
renkC[:,0]=lblencoder.fit_transform(renkC[:,0])
modelC[:,0]=lblencoder.fit_transform(modelC[:,0])
dosya.save("arabaDataset.xlsx")
dosya.close()
#Kategorik verilere dönüştürülür.
onehotencoder = OneHotEncoder()
renkCat = onehotencoder.fit_transform(renkC).toarray()
modelCat = onehotencoder.fit_transform(modelC).toarray()
dosya.save("arabaDataset.xlsx")
dosya.close()

sayfa = dosya.active
sheet=dosya.create_sheet("Ön İşleme Sonrası Veri Seti")
sheet.append(['Model1','Model2','Model3','Model4','Renk1','Renk2','Renk3','Yil','Kilometre','Fiyat'])

for k in range(0,len(modelCat)):
        sheet.append([modelCat[k,0],modelCat[k,1],modelCat[k,2],modelCat[k,3],renkCat[k,0],renkCat[k,1],renkCat[k,2],dataset["Yıl"][k],dataset["Kilometre"][k],dataset["Fiyat"][k]]) 

# Dosyanın kaydedilip kapatılması.
dosya.save("arabaDataset.xlsx")
dosya.close()















