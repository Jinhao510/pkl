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
    # print(newlist)
    pickle.dump(newlist, open("pkl_list.pkl", "wb"))
    #pd.DataFrame(newlist).to_csv("test_store.csv", header=False, index=False)


"""
讀取CSV  將所有資料進入list
將資料 
"""


def csv_to_list():
    with open("pkl_list.pkl", 'rb') as file:
        rows = pickle.load(file)
        # with open('test_store.csv', newline='') as csvfile:
        # rows = csv.reader(file)  # 讀取 CSV 檔案內容
        flist = []
        for i in rows:             # 以迴圈輸出每一列
            flist.append(i)
        # print(flist)
    return flist


"""
用while   較方便將i 不同起始點 做平行
"""



def to_date_sum_while(x):
    with open(x, 'rb') as file:
        a_dict1 = pickle.load(file)

            #flist.pop(0)if flist else False
            # file_number=len(flist)
        store_id = a_dict1.index[0]
        restaurant_id = a_dict1['restaurant_id'].head(1)

        a_dict1['date_time'] = pd.to_datetime(a_dict1['date_time'])
        a_dict1['total_amount'] = pd.to_numeric(a_dict1['total_amount'])
        a_dict1 = a_dict1.set_index('date_time')
        toam = a_dict1['total_amount'].resample('MS').sum()
        c = toam.index

        df2 = pd.DataFrame({'store_id': store_id,
                            'restaurant_id': int(restaurant_id),
                            'date_time': c,
                            'total_amount': ''})
        df2['total_amount'] = np.array(toam, dtype='int64')
        # print(D)
        
        pd.DataFrame(df2).to_csv("allamount_sum.csv",header=False, mode='a', index=False)
        print(x, "--end")

        # 先全丟CSV，問了之後確定處理成SQL，或PKL......
    # q.put(D) # queue
    return x


"""
平行處理 Queue  不去用他 指定核心  過於麻煩
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
    res = pool.map(to_date_sum_while, x)
    #print(res)
    print(len(res),"個檔案處理完畢")

"""   
先抓取所有檔案進CSV 當LIST再做處理   
"""
# pklincsv()
# csv_to_list()

# print(len(x))
# to_date_sum_while()
# multicore()


if __name__ == '__main__':
    pklincsv()
    x = csv_to_list()
    # to_date_sum_while(x)
    multicore_pool(x)
    # multicore()
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
