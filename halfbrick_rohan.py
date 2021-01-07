#!/usr/bin/env python
# coding: utf-8

# In[4]:


import argparse
import os
import pandas as pd
import csv
import json
from collections import OrderedDict

parser = argparse.ArgumentParser(description='Convert a .csv table to a corresponding .json.')
parser.add_argument('file', help='Name of the .csv file')

args = parser.parse_args()

# SELECT AND OPEN A CSV FILE
try:
    
    f = open(args.file, encoding='utf-8')
    data = list(csv.reader(f))
    print("CSV file loaded")
        
except Exception as e:
    # error loading file
    print("Error loading file ... exiting:",e)
    exit()
    
else:
    # CONVERT CSV TO JSON

    keys = data[0]
    converted = []

    for i in range(1, len(data)):
        obj = OrderedDict()
        for j in range(0,len(keys)):
            if len(data[i][j]) > 0:
                obj[keys[j]] = data[i][j]
            else:
                obj[keys[j]] = None
        converted.append(obj)
        

    # CREATE OUTPUT FILE

    try:  
        with open("output" + ".json", 'w') as outfile:
            json.dump(converted, outfile)
    except:
        print("Error creating file ... exiting")
    else:
        print("File created: output.json")


# In[122]: Generate Insights and Aggregations

# Convert data frame to pandas to apply describe() and info() functions for analyzing data

df=pd.read_csv(args.file)
summary_df=df.describe(include="O")
# summary_df


# In[119]:

print('---------------------------------------------------------------------------------------------------------------')
print("\n Key Insights: \n")
print("\nThe maximum installations for a " +str(summary_df.columns[14])+ " was by " + str(summary_df.iloc[2,14]) + " i.e approximately "+str(int(100*summary_df.iloc[3,14]/summary_df.iloc[0,14]))+'%' )
for i in range(1,12):
    print("The maximum installations for a " +str(summary_df.columns[i])+ " was by " + str(summary_df.iloc[2,i]) + " i.e approximately "+str(int(100*summary_df.iloc[3,i]/summary_df.iloc[0,i]))+'%' )


# In[ ]:





# In[120]:

print("\n \nAnalyzing the columns and data types: Meta data"+'\n')
print(df.info())


# In[65]: CREATING INSERT QUERY & Writing it to text file named sqlinsert.txt

print('---------------------------------------------------------------------------------------------------------------')
print("\nCREATING INSERT QUERY & Writing it to text file named sqlinsert.txt")
with open('./sqlinsert.txt','w', encoding='utf-8') as f1:
    insert="INSERT INTO Table_name"+str(tuple(keys))+" VALUES "
    f1.write(insert + os.linesep)
    for row in range(1,len(data)):
        if row<len(data)-1:
            content=str(tuple(data[row]))+','
        else:
            content=str(tuple(data[row]))    
        f1.write(content + os.linesep)
        f1.close
    
print('\nSQL insert Query is written in sqlinsert.txt file')

# f = open('sqlinsert.txt', 'r', encoding='utf-8')
# print(f.read())



