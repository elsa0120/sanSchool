#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第三個作業
999999999
7777777
55555
333
1
"""

for i in range(9,0,-2):
    for j in range(i):  
            print(i,sep='',end='')
    print()

# i = 9    
#  for j in range(9):  => range(0,9)
#      print(i) [0,1,2,3,4,5,6,7,8] 9個j,印出9個i(i=9)          
    
# i = 7
#  for j in range(7):  => range(0,7)
#      print(i) [0,1,2,3,4,5,6] 7個j,印出7個i(i=7)

# i = 5
#  for x in range(5):  => range(0,5)
#      print(i) [0,1,2,3,4] 5個j,印出5個i(i=5),依此類推