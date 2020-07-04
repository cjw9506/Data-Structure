#!/usr/bin/env python
# coding: utf-8

# ## 꼭 알아둬야 할 자료 구조 : 스택(Stack)
# * 데이터를 제한적으로 접근할 수 있는 구조
#  * 한쪽 끝에서만 자료를 넣거나 뺄 수 있는 구조
# * 가장 나중에 쌓은 데이터를 가장 먼저 빼낼 수 있는 구조
#  * 큐:FIFO
#  * 스택:LIFO

# 1.스택 구조
#  - LIFO와FILO가 있음
# * 대표적인 스택의 활용
#  - 컴퓨터 내부의 프로세스 구조의 함수 동작 방식
#  * 주요 기능
#   - push(): 데이터를 스택에 넣기
#   - pop(): 데이터를 스택에서 꺼내기
#  

# 2. 간단한 스택구조

# In[1]:


#재귀 함수
def recursive(data):
    if data < 0:
        print("ended")
    else:
        print(data)
        recursive(data - 1)
        print("returned", data)
recursive(4)


# 3.스택의 장단점
# * 장점
#  - 구조가 간단해서 구현이 쉽다.
#  - 데이터 저장/읽기 속도가 빠르다.
# * 단점
#  - 데이터 최대 갯수를 미리 정해야 한다.
#   - 파이썬의 경우 재귀 함수는 1000번까지만 호출이 가능함
#  - 저장 공간 낭비가 발생할 수 있다.
#   - 미리 최대 갯수만큼 저장 공간을 확보해야 한다.
#  

# 4. 파이썬 리스트 기능에서 제공하는 method로 스택 사용해보기
#  * append(push), pop 제공
# 

# In[3]:


data_stack = []
data_stack.append(1)
data_stack.append(2)


# In[4]:


data_stack


# In[5]:


data_stack.pop()


# 5. pop, push 만들어보기

# In[10]:


stack_list = []
def push(data):
    stack_list.append(data)
def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data
for index in range(10):
    push(index)


# In[11]:


pop()


# In[ ]:




