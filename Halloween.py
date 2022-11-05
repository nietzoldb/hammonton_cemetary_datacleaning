# Program to read in from three data source files in comma-seperated value format
# Read in and combine unique values 


import pandas as pd
import numpy as np
import os



df_lst = []
fileNames = os.listdir('.\hammonton_cemetary_datacleaning\Data')
num_files = len(fileNames)
i = 1
for f in fileNames:
    df = pd.read_csv("C:/Users/bniet/github-classroom/hammonton_cemetary_datacleaning/Data/"+f,sep=',')
    
    print(type(df))
    print(df.size)
    print(df.shape)
    globals()[f"df_{i}"] = df

    i +=1

print(df_1.head())
print(df_2.head())
print(df_3.head())    
print(df_4.head())
df_3['FirstName'] = 'N/A'
df_3['LastName']= 'N/A'
print(df.shape)
print(df.head())
j=0
m = df_3.shape[0]
while j < m:
    #print(len(df_3.iloc[j,0].split(' ')))
    if len(df_3.iloc[j,0].split(' '))==3:
        #print(df_3['Name'][j])
        df_3['FirstName'][j] = df_3['Name'][j].split(' ')[0]
        df_3['LastName'][j] = df_3.Name[j].split(' ')[2]        
        #print(df_3['Name'][j].split(' ')[0])
        
        #print(df_3['FirstName'])
        #print(df_3['LastName'])
    elif len(df_3.iloc[j,0].split(' '))==2:
        df_3['FirstName'][j] = df_3['Name'][j].split(' ')[0]
        df_3['LastName'][j] = df_3.Name[j].split(' ')[1] 
    
    elif len(df_3.iloc[j,0].split(' '))==1:    
        
        j +=1
        continue
    else:
        j +=1
        continue
         
    j +=1
df_chck=df_3[['FirstName','LastName']]
print(df_chck)      






