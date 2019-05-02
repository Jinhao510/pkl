# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:40:03 2019

@author: Administrator
http://paulfun.net/wordpress/?p=195
"""

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from time import time

from multiprocessing import freeze_support


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

if __name__ == '__main__':
    freeze_support()

    
    start = time()
    pool = ProcessPoolExecutor( max_workers=4)    ##########差異
    result = list( pool.map( gcd, numbers ) )
    end = time()
    print( result )
    print( '花費 %.3f 秒' % (end - start) )
    
    start = time()
    pool = ThreadPoolExecutor( max_workers=4 )############
    result = list( pool.map( gcd, numbers ) )
    end = time()
    print( result )
    print( '花費 %.3f 秒' % (end - start) )