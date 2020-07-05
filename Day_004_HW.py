import csv
import os
import numpy as np
import pandas as pd
dir_data = './data/'
f_app = os.path.join(dir_data, 'netflix_titles.csv')
print('Path of read in data: %s' % (f_app))
app_train = pd.read_csv(f_app)
TOP=app_train.head(2)
print("Get the data of top2: ", TOP)
print("Data raws and clumns : ", app_train.shape)
print("Name of all clumns : ", app_train.columns)
print("Data index : ", app_train.index)
print("Get the second raw : ", app_train.iloc[1],sep="\n")
print("Get all titles : ", app_train["title"],sep="\n")
