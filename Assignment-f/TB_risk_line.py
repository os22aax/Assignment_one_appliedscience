# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 17:53:29 2022

@author: Omesha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import the csv file
df_sick = pd.read_csv("TB_use.csv")
print(df_sick)
df_sick = df_sick[df_sick['country'] == "India"]


plt.figure(figsize= (8,5))
plt.plot(df_sick["age_group"], df_sick["best"], label="best level of risk" )
plt.plot(df_sick["age_group"], df_sick["lo"], label="low risk level")
plt.plot(df_sick["age_group"], df_sick["hi"], label="high risk level")

plt.xlabel('age_group')
plt.ylabel('Frequency')

plt.title("TB Patients Risk Ratio")
plt.legend()
plt.savefig("TB_Line_New.png")
plt.show()

#extract some special coloums from the data set
df_sick_one = df_sick[['country','age_group','best','lo','hi']]
print(df_sick_one)

#change the datatype to the float
df_sick['best'] = df_sick['best'].astype(float)
df_sick['lo'] = df_sick['lo'].astype(float)
df_sick['hi'] = df_sick['hi'].astype(float)

#pass coloum values to calculate the sum
df_list = ['best','lo','hi']
df_sick_one['Results'] = df_sick_one[df_list].sum(axis=1)
print("df_sick_one")
#change the data type to float
df_sick_one['Results'] = df_sick_one['Results'].astype(float)

#calculate the precentage values
df_sick_one['precentage_best'] = (df_sick['best']/df_sick_one['Results'])*100
df_sick_one['precentage_low'] = (df_sick['lo']/df_sick_one['Results'])*100
df_sick_one['precentage_high'] = (df_sick['hi']/df_sick_one['Results'])*100

plt.figure()
plt.plot(df_sick_one["age_group"], df_sick_one["precentage_best"], label="Precentage_best")
plt.plot(df_sick_one["age_group"], df_sick_one["precentage_low"], label="Precentage_low")
plt.plot(df_sick_one["age_group"], df_sick_one["precentage_high"], label="Precentage_high")
plt.xticks(rotation=45)

plt.xlabel("age group")
plt.ylabel("precentage")

plt.title("Precentage of risk")
plt.legend()
plt.savefig("TB_Line_precentage_New.png")
plt.show()
