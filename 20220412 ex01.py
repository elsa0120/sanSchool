#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
第一個作業
1
22
333
4444
55555
"""

for i in range(1,6):
    for j in range(i):  
            print(i,sep='',end='')
    print()

# i = 1    
#  for j in range(1):  => range(0,1)
#      print(i) [0] 1個j,印出1個i(i=1)          
    
# i = 2
#  for j in range(2):  => range(0,2)
#      print(i) [0,1] 2個j,印出2個i(i=2)

# i = 3
#  for x in range(3):  => range(0,3)
#      print(i) [0,1,2] 3個j,印出3個i(i=3),依此類推
