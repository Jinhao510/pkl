# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:05:01 2019

@author: Administrator
抓取 所有.pickle
進入CSV當LIST
        
file_name_walk("./")
"""
import pandas as pd
import os


items = os.listdir(".")
newlist = []
for names in items:
    if names.endswith(".pickle"):
        newlist.append(names)
        
print (newlist)
pd.DataFrame(newlist).to_csv("test_store.csv",index=False)
