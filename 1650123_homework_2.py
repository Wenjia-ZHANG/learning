#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:16:44 2019

@author: wenjiazhang
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 13:32:39 2019

@author: wenjiazh
"""
import matplotlib.pyplot as plt   ##import matplotlib instead of pylab 
# from pylab import *

def lossF(x,y,a,b):  # x 是2维列表，每行一个样本, y是样本分类符，
    temp=[]
    for one in x:
        temp1=[one[i]*a[i] for i in range(len(one))]
        temp1=sum(temp1)+b   # 每个样本的 a1x1+a2x2+b的取值
        temp.append(temp1)
    temp2=[]
    for i in range(len(temp)):
        temp2.append(temp[i]*y[i])   # 每个样本函数值与真值的乘积
    s=0   ##loss[0]=0
    for i in temp2:
        s += max(0,-i)   # 计算损失函数，每项取负值，即误判样本
    return s,temp2  # temp2返回有用，用于找误判，调节系数

#数据准备
x1=[[5.1, 3.5 ],  [4.9, 3. ],  [4.7, 3.2], [4.6, 3.1], [5. , 3.6], [5.4, 3.9],
       [4.6, 3.4], [5. , 3.4 ], [4.4, 2.9], [4.9, 3.1]]   ##flower
x2=[[5.5, 2.6 ],  [6.1, 3. ],  [5.8, 2.6], [5. , 2.3], [5.6, 2.7],
       [5.7, 3. ],  [5.7, 2.9],  [6.2, 2.9], [5.1, 2.5],  [5.7, 2.8]]  ##flower
x1.extend(x2)
x=x1

y1=[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]  #define flower type1
y2=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]   #define flower type2
y1.extend(y2)
y=y1

#算法å
a=[1,1]
b=1
rate=0.1
for i in range(100):
    loss,temp=lossF(x,y,a,b)
    print(loss)         #enlarge range, personally think it unnecessary to print output of function loss()
    for j in range(len(temp)):
        if temp[j] <0:
            a[0] +=rate*y[j]*x[j][0]  #根据导数修正直线参数
            a[1] +=rate*y[j]*x[j][1]
            b +=rate*y[j]
print("model is {:10.3f}x1+{:10.3f}x2+{:10.3f}".format(a[0],a[1],b))   #output function of distinguish line

#制图，后面有讲解
xvalue=[x[i][0] for i in range(len(x))]
xmin=min(xvalue)
xmax=max(xvalue)
xp=[xmin,xmax]
yp=[-a[0]/a[1]*xmin-b/a[1],-a[0]/a[1]*xmax-b/a[1]]

cls1x=[x[i][0] for i in range(len(x)) if y[i]==-1]
cls2x=[x[i][0] for i in range(len(x)) if y[i]==1]
cls1y=[x[i][1] for i in range(len(x)) if y[i]==-1]
cls2y=[x[i][1] for i in range(len(x)) if y[i]==1]

plt.plot(cls1x,cls1y,'b^')   #import matplotlib, same as below
plt.plot(cls2x,cls2y,'r^')
plt.plot(xp,yp)
plt.show()