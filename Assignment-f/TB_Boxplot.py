# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:57:44 2022

@author: Omesha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_sick = pd.read_csv("TB_use.csv")
print(df_sick)
df_sick = df_sick[df_sick['country'] == "India"]
#convert the data type to the float
df_sick['best'] = df_sick['best'].astype(float)
df_sick['lo'] = df_sick['lo'].astype(float)
df_sick['lo'] = df_sick['lo'].astype(float)

#define three different variables from the datasheet
df_best = df_sick['best']
print(df_best)

df_low = df_sick['lo']
print(df_low)

df_high = df_sick['hi']
print(df_high)

plt.figure(figsize=(10,5))
plt.boxplot([df_best, df_low, df_high], labels=["best","low","high"])
plt.title("Quartile Regions of TB patients")
plt.xlabel('Risk Range')
plt.ylabel('Frequency')

plt.show()
