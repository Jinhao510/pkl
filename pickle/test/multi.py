# -*- coding: utf-8 -*-
"""
Created on Fri May  3 09:00:45 2019

@author: Administrator
"""
import multiprocessing as mp
import time

def job(q):
    res = 0
    for i in range(1000000):
        res += i+i**2+i**3
    q.put(res) # queue

def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:' , res1+res2)



if __name__ == '__main__':
    st = time.time()
    st2 = time.time()
    multicore()
    print('multicore time:', time.time()-st2)