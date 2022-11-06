# Program to read in from three data source files in comma-seperated value format
# Read in and combine unique values 


import pandas as pd
import numpy as np
import os

'''Initializing a set of variables for the dataframes and the manipulation of those into a single clean dataframe.  
df_concat_clean is the dataframe to be used for the analysis.  FirstName:str, LastName:str, DOB:dt, DOD:dt will be the four columns.

'''

df_lst = []
df_1 = []
df_2 = []
df_3 = []
df_4 = []
df_1_NameClean = []
df_2_NameClean = []
df_3_NameClean = []
df_4_NameClean = []
df_concat_clean = []

'''The first part reads in the filenames in the directory and creates a variable df_* for each of the files.  
Each csv is read in as a pandas dataframe.  {Note: Need to check that the file ois a csv file.}   
'''
fileNames = os.listdir('.\hammonton_cemetary_datacleaning\Data')
num_files = len(fileNames)
i = 1
for f in fileNames:
    df = pd.read_csv("C:/Users/bniet/github-classroom/hammonton_cemetary_datacleaning/Data/"+f,sep=',')
    #print(type(df))
    #print(df.size)
    #print(df.shape)
    print('This is the column names for the df_%s:' %i)
    for col in df.columns:
     print(col)
    globals()[f"df_{i}"] = df
    i +=1
'''This is just to check the structure of each data frame. 
{Note: Need to check that the file ois a csv file.}   
'''
#print(df_1.head())
#print(df_2.head())
#print(df_3.head())    
#print(df_4.head())
#print(df_1.info())
#print(df_2.info())
#print(df_3.info())    
#print(df_4.info())

df_3['FirstName'] = 'N/A'
df_3['LastName']= 'N/A'
#print(df.shape)
#print(df.head())

'''This loop parses the Name column in df_3 that has the full name combined in one column whereas the others
use seperate columns for first, Middle, and last names. This is to ensure all columns match in preparation 
to concatenate all dataframes.    
'''
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
        #Maybe there should be an error generated if there are not 2 or 3 elements of the list, this implies a name is missing
        continue
    j +=1


# iterating the columns



#print(df_1.head())
#print(df_2.head())
#print(df_3.head())    
#print(df_4.head())
#print(df_3)
#print(df_2)
df_1_NameClean = df_1.drop(columns='MiddleName')
#print(df_1_NameClean)
df_2 = df_2.rename(columns = {' LastName':'LastName',' DOB':'DOB',' DOD':'DOD',' Sex':'Sex'})
df_2_NameClean = df_2.drop(columns='Sex')
df_2_NameClean = df_2[['FirstName','LastName','DOB','DOD']]
df_3_NameClean = df_3[['FirstName','LastName','DOB','DOD']]
df_4_NameClean = df_4[['FirstName','LastName','DOB','DOD']]
i=1
while i <= num_files:
    print('This is the column names for the cleaned up df_%s_NameClean:' %i)
    for col in globals()[f"df_{i}_NameClean"].columns:
        print(col)
    i +=1

df_chck=df_3[['FirstName','LastName']]
print(df_chck)      

