# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 13:49:34 2020

@author: singh
"""
from functools import reduce

def f_fn(num):
    sum=0
    while num>0:
        sum += factorial(num%10)
        num = int(num/10)
    return sum

def factorial(num):
    if num>1:
        return num*factorial(num-1)
    else:
        return 1
    
def find_next_opt(p,bool_list):
    for i in range(p+2,len(bool_list),2):
        if bool_list[i]:
            return i
    return p+2

def s_fn(num):
    sum=0
    while num>0:
        sum += num%10
        num = int(num/10)
    num=sum
    return sum

def sf_fn(num):
    return s_fn(f_fn(num))

def g_fn(num):
    x = np.array(range(10000))
    vfunc = np.vectorize(sf_fn)
    list1=vfunc(x)
    try:
        return np.where(list1==num)[0][0]
    except:
        return -1
    
def rc1(num,x,k):
    if k==0:
        file1 = open("temp.txt","a")
        file1.write(str(num)+' ')
        file1.close()
        return
    for i in range(x,10):
        rc1(num*10+i,i,k-1)

def make_list(n):
    file1 = open("temp.txt","w")
    file1.close()   
    rc1(0,0,len(str(n)))

def get_list():
    file1 = open("temp.txt","r")
    list1=[int(x) for x in file1.read().split()]
    file1.close()
    return list1

def find_gi(i,list2):
    for j in list2:
        if j[1]==i:
            return j[0]
    return 0
def main_fn(n,m):       
    ans_sum=[0]*(n+1)
    make_list(n)
    list1=get_list()
    sf_list=[sf_fn(x) for x in list1]
    list2=sorted(list(zip(list1,sf_list)),key=lambda x: x[1])
    flag=True
    while flag:
        
        for i in range(1,n+1):
            ans_sum[i]=s_fn(find_gi(i,list2))
        if reduce((lambda x,y : x*y),ans_sum[1:])==0:
            make_list(n*10)
            list1=get_list()
            sf_list=[sf_fn(x) for x in list1]
            list2=sorted(list(zip(list1,sf_list)),key=lambda x: x[1])
        else:
            flag=False
        
    return sum(ans_sum)
    
aa= [main_fn(i,10000000) for i in range(1,100)]
