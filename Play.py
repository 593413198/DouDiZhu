#!/usr/bin/python3
# @brief:  斗地主AI的实现，通过价值评估函数和记牌猜牌达到更佳的出牌效果
# @envir:  linux + python
# @date:   2019,5,10
# @author: luhao

"""
牌面定义
3~13： 3到10,J,Q,K
14: A
15: 2
16: 小王
17: 大王

一共54张牌，三人斗地主不用分花色，ABC一人17张，留3张作地主底牌
"""
from random import *

A = []
B = []
C = []
X = [3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
        11,11,11,11,12,12,12,12,13,13,13,13,
        14,14,14,14,15,15,15,15,
        16,17] 

class Card(): # 一手可以打出去的牌，称作一个Card类（如对，顺子，三带二）
    def __init__(self):
        self._size = 0  # 这手牌的牌数 （如KKK33 由5张组成）
        self._card = [] # 这手牌的组成  
        self._type = 0  # 这手牌的类型 （如单，对，顺子，炸弹）
        self._key  = 0  # 这手牌的代表牌 （如KKK33三带二的代表牌是K）

def Show(x):
    x.sort()
    y = []
    for i in x:
        if i==11:
            y.append('J')
        elif i==12:
            y.append('Q')
        elif i==13:
            y.append('K')
        elif i==14:
            y.append('A')
        elif i==15:
            y.append('2')
        elif i==16:
            y.append('&') # 小王
        elif i==17:
            y.append('$') # 大王
        else:
            y.append(i)
    print (y)

def GiveCard(): #随机发牌，一人17张，剩余3张是地主底牌
    while len(X)!=3:
        rand = randint(0,len(X)-1)
        A.append(X[rand])
        X.remove(X[rand])
        
        rand = randint(0,len(X)-1)
        B.append(X[rand])
        X.remove(X[rand])
        
        rand = randint(0,len(X)-1)
        C.append(X[rand])
        X.remove(X[rand])

if __name__ == "__main__":
    GiveCard()
    Show(A)
    Show(B)
    Show(C)
    Show(X)
