# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:25:16 2019

@author: Administrator
"""
import csv


with open('test_store.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)# 讀取 CSV 檔案內容
    flist=[]
    for i in rows:             # 以迴圈輸出每一列
        #si=str(i)
        #nsi=si[2:-2]
        flist.append(i)
        
print(flist)



