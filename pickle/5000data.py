# -*- coding: utf-8 -*-
"""
Created on Thu May  2 08:09:08 2019

@author: Administrator
"""
import pickle
import numpy as np
import pandas as pd




with open('test_store.pickle', 'rb') as file:
    dataset =pickle.load(file)

for i in range(5000):
    fw = open('test_store' + str(i) +'.pickle','wb')
    # Pickle the list using the highest protocol available.
    pickle.dump(dataset, fw)
    fw.close()
    print(i)
    