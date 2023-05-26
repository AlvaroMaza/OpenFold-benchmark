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
df2 = pd.read_csv('C:/Users/alvar/Desktop/PDB/OpenFold-benchmark/data.csv',
                  delimiter=',',index_col = 'ID')
#merge both DataFrames
result = df2.merge(df, left_index=True, right_index=True)
result['pLDDT']=pd.Series(dtype='object')
result['Inference']=pd.to_numeric(result['Inference'], errors='coerce')
result['Relaxation']=pd.to_numeric(result['Relaxation'], errors='coerce')



tsv_directory = "C:/Users/alvar/Desktop/PDB/OpenFold-benchmark/qsalign"
for subdir, _, files in os.walk(tsv_directory):
    for file in files:
        if file.endswith(".tsv"):
            try:
                file_path = os.path.join(subdir, file)
            
                # Read the TSV file into a DataFrame
                tsv_df = pd.read_csv(file_path, delimiter='\t')
            
                # Extract the tm-score from the TSV DataFrame
                tm_score = tsv_df['TM-score'].values[0]  # Assuming 'tm-score' is the column name
                
                # Update the 'result' DataFrame with the tm-score
                result.loc[file.split('.', 1)[0], 'tm-score'] = tm_score
            except:
                pass
            
#load pickle files and add pLT,pLDDT,pAE to the DataFrame
root_directory = "D:/output_directory_pkl"
i=1
for subdir, _, files in os.walk(root_directory):
    for file in files:
        if file.endswith(".pkl"):
            print(f"Progress: {round((i/3987)*100,2)} %")
            i+=1
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

result.to_pickle('result.pkl')
