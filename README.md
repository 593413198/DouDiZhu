## 三人斗地主的AI实现

**创建时间：**
`2019/5/10`

**搭建环境：**
`Ubuntu 18.04   python 2.7`

**代码架构：**
```python
Play.py #主代码文件

class Card #定义牌类
```

## 思路分析：

**阶段1.0 牌的定义，存储和随机发牌**

- 一共54张牌，三方个17张，留3张作地主底牌
- 3~13表示3到K，14表示A，15表示2，16\17分别是小王和大王;(这种表示正好符合牌的大小关系)
- 可以一次性打出的牌组，称作一个Card类
```python
A = []; B = []; C = []; # 分别存三人的牌
X = []; # 所有牌的汇总，一共54张，随机发51张，剩余3张作地主底牌
class Card: 
# 定义一个Card类，可以一次性打出去的一个组合，称作一个Card类

GiveCard()  # 随机发牌
split(A)  # 把A的牌分成Card类
```

