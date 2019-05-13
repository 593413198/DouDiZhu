#!/usr/bin/python3
# @brief:  斗地主AI的实现，通过价值评估函数和记牌猜牌达到更佳的出牌效果
# @envir:  linux + python3
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
a = []
B = []
b = []
C = []
X = [3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,
        11,11,11,11,12,12,12,12,13,13,13,13,
        14,14,14,14,15,15,15,15,
        16,17] 

# 定义牌组的种类
'''
bomb 炸弹
rocket 王炸
_3_1 三拖一
_3_2 三拖二


'''

class Card(): # 一手可以打出去的牌，称作一个Card类（如对，顺子，三带二）
    def __init__(self):
        self._card = []    # 这手牌的组成  
        self._type = 0     # 这手牌的类型 （如单，对，顺子，炸弹）
        self._behalf  = 0  # 这手牌的代表牌 （如KKK33三带二的代表牌是K）

    def bomb(self,x):
        # 炸弹
        self._card = [x,x,x,x]
        self._type = 'bomb'
        self._behalf = x
        return self

    def rocket(self):
        # 王炸，2张
        self._card = [16,17]
        self._type = 'rocket'
        return self

    def _3_1(self,x,y):
        # 三拖一
        self._card = [x,x,x,y]
        self._type = '3_1'
        self._behalf = x
        return self
    
    def _3_2(self,x,y):
        # 三拖二
        self._card = [x,x,x,y,y]
        self._type = '3_2'
        self._behalf = x
        return self

    def _3_0(self,x):
        # 三不拖
        self._card = [x,x,x]
        self._type = '3_0'
        self.behalf = x
        return self
    
    def pair(self,x):
        # 单对
        self._card = [x,x]
        self._type = 'pair'
        self._behalf = x
        return self

    def single(self,x):
        self._card = [x]
        self._type = 'single'
        self._behalf = x
        return self

    

def split(x):
    '''
    拆牌：拆成尽可能少的Card()类'''
    ans = []
    single = []
    pair = []
    if 16 in x and 17 in x: # 王炸
        ans.append(Card().rocket())
        x.remove(16)
        x.remove(17)
    for i in x:
        if x.count(i) == 1:
            single.append(i)
        if x.count(i) == 2 and i not in pair:
            pair.append(i)
    for i in x:
        if x.count(i)==4: # 4张凑炸，目前不考虑拆炸弹
            ans.append(Card().bomb(i))
            for j in range(4):
                x.remove(i)
        if x.count(i)==3: # 3张
            if single: # 凑3拖1
                ans.append(Card()._3_1(i,single[0]))
                single.pop(0)
            elif pair: # 凑3拖2
                ans.append(Card()._3_2(i,pair[0]))
                pair.pop(0)
            else: # 3不拖
                ans.append(Card()._3_0(i))
            for j in range(3):
                x.remove(i)
    # 单牌单独走掉
    if single:
        for i in single:
            ans.append(Card().single(i))
    if pair:
        for i in pair:
            ans.append(Card().pair(i))
    return ans
        


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
            y.append(str(i))
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
    A.sort()
    B.sort()
    C.sort()

if __name__ == "__main__":
    GiveCard()
    print (A)
    print (B)
    print (C)
    print ('\n')
    for i in split(A):
        print (i._card,end=' ')
    print ('\n')
    for i in split(B):
        print (i._card,end=' ')
    print ('\n')
    for i in split(C):
        print (i._card,end=' ')


