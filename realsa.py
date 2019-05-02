# -*- coding: utf-8 -*-
"""
Created on Thu May  2 09:14:15 2019

@author: Administrator
"""

from os import walk
import glob


print (glob.glob(r'D:\work\data_pro\0430\pickle\test\*.pickle'))
# 指定要列出所有檔案的目錄

"""
mypath = "D/work/data_pro/0430/pickle/test"

# 遞迴列出所有子目錄與檔案
for root, dirs, files in walk(mypath):
  print("路徑：", root)
  print("  目錄：", dirs)
  print("  檔案：", files)
  """