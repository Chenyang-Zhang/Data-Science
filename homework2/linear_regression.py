import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

raw_data = pd.read_csv('PRSA_Data_Tiantan_20130301-20170228.csv')
data = raw_data.drop(['No', 'hour', 'wd', 'station'], axis = 1)
data = data.dropna(axis = 0)
print(data)
