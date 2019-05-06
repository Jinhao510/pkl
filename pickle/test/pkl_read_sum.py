# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:53:57 2019

@author: Administrator
"""
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:33:29 2019

@author: Administrator
"""


import os
import csv
import time
import pickle
import numpy as np
import pandas as pd
from multiprocessing import Pool
import multiprocessing as mp

start = time.time()
print("pro_start")


"""
將此PY資料夾內之PKL檔進入LIST
將此LIST 輸出至CSV以供檢查
"""


def pklincsv():
    items = os.listdir(".")  # uPath = unicode(cPath,'utf-8')如資料夾路徑有中文
    newlist = []  # 創建list
    for names in items:
        if names.endswith(".pickle"):  # 找出所有.pkl
            newlist.append(names)  # 加入list
    #print(newlist)
    pd.DataFrame(newlist).to_csv("test_store.csv", header=False, index=False)


"""
讀取CSV  將所有資料進入list
將資料 
"""
def csv_to_list():
    with open('test_store.csv', newline='') as csvfile:
        rows = csv.reader(csvfile)  # 讀取 CSV 檔案內容
        flist = []
        for i in rows:             # 以迴圈輸出每一列
            flist.append(i)
        #print(flist)
    return flist
"""
讀取將資料資料
TO datetime


def to_date_sum(reda):
    file_number = len(flist)
    print('file_val:', file_number)   #檢視個數
    for i in flist:
        # print(i)
        si = str(i)
        nsi = si[2:-2]        #['si']，去掉資料頭尾 以利讀檔案
        #print(nsi)

        with open(nsi, 'rb') as file:
            print(nsi,"start",)
            a_dict1 = pickle.load(file)
            a_dict1['date_time'] = pd.to_datetime(a_dict1['date_time'])
            a_dict1['total_amount'] = pd.to_numeric(a_dict1['total_amount'])
            a_dict1 = a_dict1.set_index('date_time')
    
            mon_sum = a_dict1.resample('MS').sum()
            C = mon_sum.iloc[:, 1]
            #print(nsi, C)
            C=mon_sum.iloc[:,1]
            D=np.append([nsi],C,axis=0)
            #print(D)
            pd.DataFrame(D).to_csv("allamount_sum.csv",header=False,mode='a',index=False)
            #先全丟CSV，問了之後確定處理成SQL，或PKL......


用while   較方便將i 不同起始點 做平行
未做:處理完刪除list 中第N個檔案、如何抓取檔案  雙核可用開頭結尾
#資料處理問題()，抓取即刪除/處理完後刪除，抓了未執行完將不利除錯/當A未執行完是否B重複處理此檔案
但是否有作法 只要 規定幾個執行序 直接多工供平行
"""




def to_date_sum_while(x):     
        si = str(x)
        nsi = si[2:-2]
        #print(nsi)
        with open(nsi, 'rb') as file:
            #flist.pop(0)if flist else False
            #file_number=len(flist)
            #pd.DataFrame(flist).to_csv("test_store.csv", header=False, index=False)
            print(nsi,"start")
            a_dict1 = pickle.load(file)
            a_dict1['date_time'] = pd.to_datetime(a_dict1['date_time'])
            a_dict1['total_amount'] = pd.to_numeric(a_dict1['total_amount'])
            a_dict1 = a_dict1.set_index('date_time')
    
            mon_sum = a_dict1.resample('MS').sum()
            C = mon_sum.iloc[:, 1]
            #print(nsi, C)
            C=mon_sum.iloc[:,1]
            D=np.append([nsi],C,axis=0)
            #print(D)
            pd.DataFrame(D).to_csv("allamount_sum.csv",header=False,mode='a',index=False)
            print(nsi,"--end")

            #先全丟CSV，問了之後確定處理成SQL，或PKL......
        #q.put(D) # queue
        return nsi
    
    
    
    
"""
平行處理 Queue
"""    
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=to_date_sum_while, args=(q,))
    p1.start()
    
    p2 = mp.Process(target=to_date_sum_while, args=(q,))
    p2.start()
    
    
    p3 = mp.Process(target=to_date_sum_while, args=(q,))
    p3.start()
    
    
      
    p1.join()
    p2.join()
    p3.join()

    #res1 = q.get()
    #res2 = q.get()
    #res3 = q.get()

    print('multicore  ok')
    
"""
平行處理 Pool
"""     
def multicore_pool(x):
    pool = mp.Pool()
    res = pool.map(to_date_sum_while,x)
    print(res)
    
    
"""   
先抓取所有檔案進CSV 當LIST再做處理   
"""   
#pklincsv()   
#csv_to_list()

#print(len(x))               
#to_date_sum_while()
#multicore()


if __name__ == '__main__':
    pklincsv()
    x=csv_to_list()
    print(x)
    #to_date_sum_while()
    multicore_pool(x)
    #multicore()
    end = time.time()
    elapsed = end - start
    print("Time taken: ", elapsed, "seconds.")



"""
# show plt
plt.legend()
#df.plot(kind='area')
mon_sum.iloc[:,1].plot(kind='area')
plt.show()
"""



