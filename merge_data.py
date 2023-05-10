# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:29:53 2023

@author: alvar
"""
import numpy as np
import pandas as pd
import json
import os
import pickle
import matplotlib.pyplot as plt


# load the JSON file
with open('C:/Users/alvar/Desktop/PDB/times.json', 'r') as f:
    data = json.load(f)
# create a DataFrame from the data
df = pd.DataFrame.from_dict(data, orient='index')

#load the csv file
df2 = pd.read_csv('C:/Users/alvar/Desktop/PDB/OpenFold-benchmark/ids_final.csv',
                  delimiter=',',index_col = 'ID')
#merge both DataFrames
result = df2.merge(df, left_index=True, right_index=True)
result['pLDDT']=pd.Series(dtype='object')
result['Inference']=pd.to_numeric(result['Inference'], errors='coerce')
result['Relaxation']=pd.to_numeric(result['Relaxation'], errors='coerce')


#Test while I don't have all the data
result = result.rename(index={'1an8_A': '1tlt_A'})

#load pickle files and add pLT,pLDDT,pAE to the DataFrame
root_directory = "C:/Users/alvar/Desktop/PDB/predictions2"
for subdir, _, files in os.walk(root_directory):
    for file in files:
        if file.endswith(".pkl"):
            file_path = os.path.join(subdir, file)
            with open(file_path, "rb") as f:
                name = file.split('-')[0]
                pickle_data = pickle.load(f)
                try:
                    result.loc[name,'symmetry']
                    result.loc[name,'pTM'] = pickle_data['predicted_tm_score']
                    result.loc[name,'max_pAE'] = pickle_data['max_predicted_aligned_error']
                    result.at[name,'pLDDT'] = pickle_data['plddt']
                    
                except:
                    pass
                
fig, ax = plt.subplots()
ax.scatter(result['seq_length'],result['Inference'])

# define the function
def f(x):
    return (x/100)**2.75

# generate x-values
x = np.linspace(0, 1200, 1000)

# generate y-values using the function
y = f(x)

ax.plot(x,y,color='red')

plt.show()