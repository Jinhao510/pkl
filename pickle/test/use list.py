# -*- coding: utf-8 -*-
"""
Created on Fri May  3 16:26:03 2019

@author: Administrator
"""



"""
讀取CSV  將所有資料進入list
"""

import csv
import pandas as pd


with open('test_store.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)  # 讀取 CSV 檔案內容
    flist = []
    for i in rows:             # 以迴圈輸出每一列
            # si=str(i)
            # nsi=si[2:-2]
        flist.append(i)
        i=0
        while i < 11:
            print (flist)
            i += 1
        #print(rows,i)
        #flist.pop(range(i))
        #print(flist)
        

print(flist)
print("-----------------------------")
print(flist.pop(0))
print(flist)



i = 0
   while i < file_number:
       WF=flist[i]
       si = str(WF)
       nsi = si[2:-2]
       i += 1 

#pd.DataFrame(flist).to_csv("te123.csv",header=False,mode='a',index=False)

