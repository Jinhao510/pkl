# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:52:19 2019

@author: Administrator
讀取pickle，檔案 將特定時間 之amount 進行加總

1.讀數多數個pickle檔，同資料夾，同規則。
2.抓取出時間 與 amount。
3.計算出特定時間區間 amount。
4.平行處理 將 資料抓取  排序日期加總amount 

將資料 date_time 前10   2018-01-03 抓出，
列出

sum total_amount

"""
import csv
import time
import pickle
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime
import matplotlib.pyplot as plt
from multiprocessing import Pool  #多工處理

start = time.time()
print("@@time start@@")  
# reload a file to a variable



for i in range(2):
    filen='test_store'+str(i)+'.pickle'
    with open(filen, 'rb') as file:
        a_dict1 =pickle.load(file)
        print(filen,'------start')

        a_dict1['date_time'] = pd.to_datetime(a_dict1['date_time'])
        a_dict1['total_amount'] = pd.to_numeric(a_dict1['total_amount'])
        a_dict1 = a_dict1.set_index('date_time')
        
        mon_sum=a_dict1.resample('MS').sum()
        C=mon_sum.iloc[:,1]
        D=np.append([filen],C,axis=0)
        #print(D)
        D=np.array(D)
        #E=D.transpose()
     
        print(filen,'------end')
        pd.DataFrame(D).to_csv("test_store.csv",header=False,mode='a',index=False,line_terminator="\n")
        
    
        
        #D.to_csv("test_store.csv",index=False)
    
            
            #pd.DataFrame(D).to_csv("test_store.csv",index=False)

    





"""
# show plt
plt.legend()
#df.plot(kind='area')
mon_sum.iloc[:,1].plot(kind='area')
plt.show()
"""

end = time.time()
elapsed = end - start
print ("all Time taken: ", elapsed, "seconds.")