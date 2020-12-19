#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 11:16:40 2020

@author: konstantin.vinogrado
"""

import re
import numpy as np
file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
# Strips the newline character 
mat=[]
for line in Lines: 
    s = line.replace(".", "-1 ").replace("L","0 ")
    x = np.fromstring(s, dtype=int, sep=' ')
    mat.append(x)
seats=np.array(mat)
seats_a = np.copy(seats);
seats_b = np.copy(seats);
occupied_mat = np.zeros(seats.shape)


def f0(p,i):
    return (p[0] +i, p[1]+i)
def f1(p,i):
    return (p[0]   , p[1]+i)
def f2(p,i):
    return (p[0] -i, p[1]+i)

def f3(p,i):
    return (p[0] +i, p[1] )
def f4(p,i):
    return (p[0] -i, p[1] )

def f5(p,i):
    return (p[0] +i, p[1] - i)
def f6(p,i):
    return (p[0]   , p[1] - i)
def f7(p,i):
    return (p[0] -i, p[1] - i)


directions=[f0,f1,f2,f3,f4,f5,f6,f7]
L = max(seats.shape)
def valid_range(c):
    return (min(c)>=0) and (c[0]<seats.shape[0]) and (c[1]<seats.shape[1])
    return 

def search(fx,a,p):
    for i in range(1,L):
        c = fx(p,i)
        if valid_range(c):
            x=a[c]
            if (x==1):
                return 1
            elif (x==0):
                return 0
            else:
                pass;
        else:
            break;
    return 0

def calc_adj(a,p):
    cnt=0
    for f in directions:
        cnt+=search(f,a,p)
    return cnt

#%%

for l in range(1,400):
    print(f"==={l}")
    
    seats_b=np.copy(seats_a)
    for i in range(seats.shape[0]):
        for j in range(seats.shape[1]):
            if (seats_a[i,j]==0):
                occupied= calc_adj(seats_a,(i,j))
                if occupied == 0 :
                    seats_b[i,j] = 1;
    seats_a=np.copy(seats_b)
    for i in range(seats.shape[0]):
        for j in range(seats.shape[1]):
            if (seats_b[i,j]>0):
                occupied= calc_adj(seats_b,(i,j))
                
                occupied_mat[i,j]=occupied;
                if occupied >= 5 :
                    seats_a[i,j] = 0;
    if (seats_b==seats_a).all():
        print("Stable!!!");
        break
print(f"Rounds : {l}")        

print((seats_b == 1).sum())

#%%
t = calc_adj(seats_a,(0,0))
print(f"Result {t}")