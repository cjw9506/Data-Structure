#!/usr/bin/env python
# coding: utf-8

# ## 객체지향
# 1. 객체지향의 핵심(class 와 object)
#  - 속성(attribute)와 동작(method)을 갖는 데이터 타입
#  - 속성(attribute)는 변수와 유사
#  - 동작(method)는 함수와 유사
#  

# In[1]:


# class 선언하기
class Quadrangle:
    pass
dir(Quadrangle)


# In[2]:


#클래스명(object)로도 쓸 수 있음
class Quadrangle(object):
    pass
dir(Quadrangle)


# In[3]:


square = Quadrangle()
dir(square)


# In[4]:


type(square)


# In[7]:


#attribute 넣어보기
class Quadrangle:
    width  = 0
    height = 0
    color = 'black'
square = Quadrangle()
print(square.width)
print(square.height)
print(square.color)


# In[12]:


# method 넣어보기
class Quadrangle:
    width = 0
    hieght = 0
    color = 'black'
    
    def get_area(self):
        return self.width * self.height
    def set_area(self, data1, data2):
        self.width = data1
        self.height = data2
        


# In[14]:


square = Quadrangle()
square.set_area(5,5)


# In[16]:


square.width


# In[18]:


#생성자와 소멸자
class Quadrangle:
    def __init__(self, width, height, color):
        self.width= width
        self.height = height
        self.color = color
    def __del__(self):
        print("Quadrangle object is deleted")
square = Quadrangle(5, 5, "black")


# In[19]:


del square


# In[24]:


#정삼각형 클래스, 너비 출력
import math
class Quadrangle:
    def __init__(self, length):
        self.length = length
    def get_area(self):
        return (math.sqrt(3) / 2) * self.length**2  # (math.sqrt(3) / 2) * math.pow(self.length, 2)
square = Quadrangle(10)
square.get_area()


# * 깨알지식
#   -  _(method name) 하면 protected 가 된다.
#   -  __(method name) 하면 pritvate 가 된다.

# ## 데코레이터 사용해보기

# In[34]:


import datetime
def datetime_decorator(func):
    def wrapper(): #호출할 함수를 감싸는 함수
        print('time' + str(datetime.datetime.now()))
        func()
        print(datetime.datetime.now())
    return wrapper
        


# In[35]:


@datetime_decorator
def logger_login_david():
    print("David login")
logger_login_david()


# In[ ]:




