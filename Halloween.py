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
df_concat = []

'''The first part reads in the filenames in the directory and creates a variable df_* for each of the files.  
Each csv is read in as a pandas dataframe.  {Note: Need to check that the file ois a csv file.}   
'''
fileNames = os.listdir('.\hammonton_cemetary_datacleaning\Data')
num_files = len(fileNames)
i = 1
for f in fileNames:
    df = pd.read_csv("C:/Users/bniet/github-classroom/hammonton_cemetary_datacleaning/Data/"+f,sep=',')
    print('This is the column names for the df_%s:' %i)
    for col in df.columns:
     print(col)
    globals()[f"df_{i}"] = df
    i +=1

df_3['FirstName'] = 'NaN'
df_3['LastName']= 'NaN'

'''This loop parses the Name column in df_3 that has the full name combined in one column whereas the others
use seperate columns for first, Middle, and last names. This is to ensure all columns match in preparation 
to concatenate all dataframes.    
'''
j=0
m = df_3.shape[0]
while j < m:
    if len(df_3.iloc[j,0].split(' '))==3:
        df_3['FirstName'][j] = str(df_3['Name'][j]).split(' ')[0]
        df_3['LastName'][j] = str(df_3.Name[j]).split(' ')[2]        
    elif len(str(df_3.iloc[j,0]).split(' '))==2:
        df_3['FirstName'][j] = str(df_3['Name'][j]).split(' ')[0]
        df_3['LastName'][j] = str(df_3.Name[j]).split(' ')[1] 
    elif len(str(df_3.iloc[j,0]).split(' '))==1:    
        j +=1
        continue
    else:
        j +=1
        #Maybe there should be an error generated if there are not 2 or 3 elements of the list, this implies a name is missing
        continue
    j +=1
    
    
'''The next lines just drop unneeded columns and select the needed columns to
create the dataframes with all the same and correct columns.    
'''
df_1_NameClean = df_1.drop(columns='MiddleName')
df_2 = df_2.rename(columns = {' LastName':'LastName',' DOB':'DOB',' DOD':'DOD',' Sex':'Sex'})
df_2_NameClean = df_2[['FirstName','LastName','DOB','DOD']]
df_3_NameClean = df_3[['FirstName','LastName','DOB','DOD']]
df_4_NameClean = df_4[['FirstName','LastName','DOB','DOD']]
df_concat = pd.concat([df_1_NameClean,df_2_NameClean,df_3_NameClean,df_4_NameClean], axis=0, ignore_index=True)
df_concat.info()
#print(df_1_NameClean)
#print(df_2_NameClean)
#print(df_3_NameClean)
#print(df_4_NameClean)
print(df_concat)

'''This loop parses the DOB and DOD columns in df_concat keeping only the year for each.   
'''

j=0
m = df_concat.shape[0]
while j < m:
    k=len(str(df_concat.iloc[j,2]).split('/'))
    l=len(str(df_concat.iloc[j,2]).split(' '))
    print(df_concat.iloc[j,2])
    print(str(df_concat.iloc[j,2]).split('/'))
    print(str(df_concat.iloc[j,2]).split(' '))
    if k == 3:
        df_concat['DOB'][j] = str(df_concat['DOB'][j]).split('/')[2]
        print(df_concat['DOB'][j])
        
    elif k==2:
        df_concat['DOB'][j] = str(df_concat['DOB'][j]).split('/')[1]
        print(df_concat['DOB'][j])    
        
    elif k==1:    
        if l == 1:
            df_concat['DOB'][j] = str(df_concat['DOB'][j]).split(' ')[0]
            print(df_concat['DOB'][j])   
            
        elif l == 2:
            df_concat['DOB'][j] = str(df_concat['DOB'][j]).split(' ')[1]
            print('look at index:%s' %j)  
            print(df_concat['DOB'][j])
           
        else:
            df_concat['DOB'][j] = str(df_concat['DOB'][j]).split(' ')[(l-1)]
            print('look at index:%s' %j)  
            print(df_concat['DOB'][j])
            
    else:
        '''Maybe there should be an error generated if there are not 2 or 3 elements of the list,
        this implies a date is in some other format 
        '''
        print(' look at index:%s' %j)  
        
        continue
    j +=1
    
j=0
m = df_concat.shape[0]
while j < m:
    k=len(str(df_concat.iloc[j,3]).split('/'))
    l=len(str(df_concat.iloc[j,3]).split(' '))
    print(df_concat.iloc[j,3])
    print(str(df_concat.iloc[j,3]).split('/'))
    print(str(df_concat.iloc[j,3]).split(' '))
    if k == 3:
        df_concat['DOD'][j] = str(df_concat['DOD'][j]).split('/')[2]
        print(df_concat['DOD'][j])
        
    elif k==2:
        df_concat['DOD'][j] = str(df_concat['DOD'][j]).split('/')[1]
        print(df_concat['DOD'][j])    
        
    elif k==1:    
        if l == 1:
            df_concat['DOD'][j] = str(df_concat['DOD'][j]).split(' ')[0]
            print(df_concat['DOD'][j])   
            
        elif l == 2:
            df_concat['DOD'][j] = str(df_concat['DOD'][j]).split(' ')[1]
            print('look at index:%s' %j)  
            print(df_concat['DOD'][j])
           
        else:
            df_concat['DOD'][j] = str(df_concat['DOD'][j]).split(' ')[(l-1)]
            print('look at index:%s' %j)  
            print(df_concat['DOD'][j])
            
    else:
        '''Maybe there should be an error generated if there are not 2 or 3 elements of the list,
        this implies a date is in some other format 
        '''
        print(' look at index:%s' %j)  
        
        continue
    j +=1
#print(df_concat)
df_concat.isna()
df_concat_clean=df_concat.dropna()
print(df_concat.isna())
 