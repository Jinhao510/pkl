# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:33:29 2019

@author: Administrator
"""
import time
import pickle
import numpy as np
import pandas as pd

with open('test_store.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  # 以迴圈輸出每一列

  for i in rows:
      si=str(i)
      nsi=si[2:-2]
      with open(nsi, 'rb') as file:
        a_dict1 =pickle.load(file)
    
        a_dict1['date_time'] = pd.to_datetime(a_dict1['date_time'])
        a_dict1['total_amount'] = pd.to_numeric(a_dict1['total_amount'])
        a_dict1 = a_dict1.set_index('date_time')
        
        mon_sum=a_dict1.resample('MS').sum()
        C=mon_sum.iloc[:,1]
        print(C)
       