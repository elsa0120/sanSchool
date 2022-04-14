#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第二個作業
55555
4444
333
22
1
"""

for i in range(5,0,-1):
    for j in range(i):  
            print(i,sep='',end='')
    print()
    
# i = 5    
#  for j in range(5):  => range(0,5)
#      print(i) [0,1,2,3,4] 5個j,印出5個i(i=5)          
    
# i = 4
#  for j in range(4):  => range(0,4)
#      print(i) [0,1,2,3] 4個j,印出4個i(i=4)

# i = 3
#  for x in range(3):  => range(0,3)
#      print(i) [0,1,2] 3個j,印出3個i(i=3),依此類推