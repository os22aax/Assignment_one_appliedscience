# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 20:48:45 2022

@author: Omesha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import the csv file
df_inflection = pd.read_csv("TB_use.csv")
#extract details of country India
df_inflection = df_inflection[df_inflection['country'] == "India"]

plt.figure(figsize= (8,5))
#up the level of y axis
plt.ylim(0.0, 35.0)
#use alpha to make transparancy
plt.hist(df_inflection["best"],label="best level of risk", bins=12,alpha=0.7)
plt.hist(df_inflection["lo"],label="low level of risk", bins=12,alpha=0.7)
plt.hist(df_inflection["hi"],label="high level of risk", bins=12,alpha=0.7)
plt.xlabel('Age_range')
plt.ylabel('Frequency')
plt.title("Risk level")
plt.legend()

#plot subplots to take more clear idea
plt.figure(figsize=(15,8))
plt.subplot(2,2,1)
plt.hist(df_inflection["best"], label="best level of risk", bins=12)
plt.ylim(0.0,30.0)
plt.xlabel('age_range')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(2,2,2)
plt.hist(df_inflection["lo"], label="low level of risk", bins=12)
plt.ylim(0.0, 30.0)
#plt.xlim(0.0,3.0)
plt.xlabel('age_range')
plt.ylabel('Frequency')
plt.legend()

plt.subplot(2,2,3)
plt.hist(df_inflection["hi"], label="low level of risk", bins=12)
plt.ylim(0.0,30.0)
plt.xlabel('age_range')
plt.ylabel('Frequency')
plt.legend()


plt.show()