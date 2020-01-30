# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 11:45:53 2020

@author: Dragon
"""
import pandas as pd
import numpy as np


#filepath="D:\\work\\github\\Coursera_Capstone\\"
file_in="Toronto.xlsx"

df=pd.read_excel(file_in)
df.columns.values
print("Start count:",len(df))
df.replace("Not assigned",np.nan,inplace=True)
df.dropna(subset=["Borough"],axis=0,inplace=True)
print("After drop Borough=Not assigned:",len(df))
df['Neighbourhood'].replace(np.nan,df['Borough'],inplace=True)
df.sort_values("Postcode",inplace=True)
df.reset_index(drop=True, inplace=True)
df2=pd.DataFrame(columns=["PostalCode","Borough",'Neighbourhood'])
#x=df.loc[1,"Postcode"]
Postcode=""
Nb=""
Br=""
for i in df.index:
    if df.loc[i,"Postcode"]==Postcode:
        Nb=Nb+", "+str(df.loc[i,"Neighbourhood"])
    else:
        if Nb!="":
            df2=df2.append({"PostalCode":Postcode,"Borough":Br,'Neighbourhood':Nb}, ignore_index=True)
        Nb=str(df.loc[i,"Neighbourhood"])
        Br=str(df.loc[i,"Borough"])
        Postcode=str(df.loc[i,"Postcode"])
print(df2.head())
print("After summarizing PostalCode:",df2.shape)        
df2.to_csv("Toronto_PostalCode.csv")
geo_df=pd.read_csv("Geospatial_Coordinates.csv") 
print(geo_df.head())
geo_df.set_index("Postal Code",inplace=True)
La = np.array([])
Lo = np.array([])
for i in df2.index:    
    La=np.append(La,[geo_df.loc[df2.loc[i,"PostalCode"],"Latitude"]])
    Lo=np.append(Lo,[geo_df.loc[df2.loc[i,"PostalCode"],"Longitude"]])
df2["Latitude"]=La
df2["Longitude"]=Lo
print(df2.head())
print(len(df["Neighbourhood"].unique()))
