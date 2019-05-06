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
        #print(flist) 
        file_number=len(flist)
        
        
 
       
while (file_number !=0):
    try:
        WF=flist[0]
        si = str(WF)
        nsi = si[2:-2]
    except ValueError:
        break
    #print(nsi)
    with open(nsi, 'rb') as file:
        x=flist.pop(0)if flist else False
        file_number=len(flist)
        print(nsi,"start")
                   
       
        
        
        #print(rows,i)
        #flist.pop(range(i))
        #print(flist)
        







#pd.DataFrame(flist).to_csv("te123.csv",header=False,mode='a',index=False)

