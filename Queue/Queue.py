#!/usr/bin/env python
# coding: utf-8

# # Queue
# 1. 큐의 구조
#  * 큐는 가장 먼저 넣은 것을 가장 먼저 꺼낸다(FIFO)
#  * 가장 나중에 넣은 것을 가장 나중에 꺼낸다(LILO)
#  * 스택과 구조가 반대

# 2. 알아둘 용어
#  * enqueue: 큐에 데이터를 넣는 기능
#  * dequeue: 큐에 데이터를 꺼내는 기능

# 3. FIFO

# In[16]:


import queue

data_queue = queue.Queue() #queue라이브러리이름, Queue클래스
# data_queue 라는 이름으로 큐가 생성
data_queue.put("funcoding") #put = 데이터 집어넣기
data_queue.put(1)
data_queue.qsize() #queue의 사이즈
data_queue.get() #get = 가장 먼저 들어간 data 꺼내기 -> funcoding
data_queue.qsize()
data_queue.get() # -> 1
data_queue.qsize()


# 4.LIFO

# In[21]:


import queue
data_queue = queue.LifoQueue() #Lifo 큐 생성
data_queue.put("funcoding") 
data_queue.put(1)
data_queue.qsize()
data_queue.get() # 1
data_queue.get() # funcoding
data_queue.qsize() # 0


# 5.PriorityQueue

# In[23]:


#앞에 10, 5, 15 숫자 중 우선순위가 높은 순서대로 데이터 추출
# 숫자 낮을수록
import queue
data_queue = queue.PriorityQueue()
data_queue.put((10, "korea"))
data_queue.put((5,1)) 
data_queue.put((15,"china"))
data_queue.qsize()
data_queue.get()


# #### 큐는 운영체제에서 많이 쓰임
#  * 특별한 장단점이 없음

# 6. enqueue, dequeue 다뤄보기

# In[29]:


queue_list = list()
def enqueue(data):
    queue_list.append(data)
def dequeue():
    data= queue_list[0]
    del queue_list[0]
    return data


# In[30]:


for index in range(10):
    enqueue(index)


# In[31]:


len(queue_list)


# In[34]:


dequeue() #할때마다 맨 앞의 값이 삭제되기 때문에 값이 늘어남


# In[ ]:




