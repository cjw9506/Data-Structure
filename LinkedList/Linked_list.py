#!/usr/bin/env python
# coding: utf-8

# ## 링크드 리스트(linked list)
# 1. 링크드 리스트 구조
#  * 연결 리스트라고도 함
#  * 링크드 리스ㅡ는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 구조
#  * 파이썬은 리스트 타입이 링크드 리스트의 기능을 모두 지원
# 

# * 기본 구조와 용어
#  * 노드 : 데이터 저장단위(데이터값, 포인터)
#  * 포인터 : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

# In[2]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# In[3]:


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


# In[5]:


node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1


# In[6]:


class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
def add(data):
    node = head
    while node.next:#노드의 next가 있으면
        node = node.next
    node.next = Node(data)
    
        


# In[7]:


node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1
for index in range(3, 11):
    add(index)


# In[14]:


node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)


# 2. 링크드 리스트의 장단점
#  * 장점
#     - 미리 데이터 공간을 할당하지 않아도 된다.
#       - 배열은 미리 데이터 공간을 할당 해야 함
#  * 단점 
#     - 연결을 위한 별도 데이터 공간이 필요, 저장공간 효율 높지 않다.
#     - 연결 정보를 찾는 시간이 필요, 접근 속도 느림
#     - 중간 데이터 삭제시, 앞뒤 데이터 연결 재구성해야 함.

# In[15]:


node3 = Node(1.5)


# In[16]:


# 1 과 2 사이에 1.5를 삽입하는 경우
node = head 
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next
node_next = node.next
node.next = node3
node3.next = node_next


# 3. 객체지향으로 구현해보기
#  - 삽입
#  - 삭제

# In[30]:


# 혼자 다시 만들어보기
class Node: 
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

# 중간에 노드를 삽입하는 객체지향
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)
    def add(self, data): # 추가
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
############여기까지가 추가###################
    def delete(self,data):
        if self.head =='':
            print("해당 값을 가진 노드가 없습니다.")
            return
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
################### head 노드 삭제 #################
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
################### 마지막노드/중간노드 삭제################


# In[31]:


linkedlist1 = NodeMgmt(0)
linkedlist1.desc()


# In[32]:


for data in range(1, 10):
    linkedlist1.add(data)
linkedlist1.desc()


# In[33]:


linkedlist1.delete(4)


# ## 더블 링크드리스트(double linkedlist)

# * 기본 구조
#   - 이중 연결 리스트
#   - 양방향으로 연결되어 있어서 양방향 노드 탐색이 가능

# In[43]:


class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail =new
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
    


# In[44]:


double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()


# ### 검색기능추가

# In[64]:


class Node:
    def __init__(self, data, prev=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next
class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head
    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new
            new.prev = node
            self.tail =new
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
###############검색 ################
    def search_from_head(self, data):
        if self.head == None:
            return False
        while node:
            if node.data == data:
                return node
            else:
                node = node.next##넥스트
        return False
    def search_from_tail(self, data):
        if self.head == None:
            return False
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev##프리브
        return False
    def insert_before(self,data,before_data):
        if self.head == None:
            self.head = Node(data)
            return True
        else:
            node = self.tail
            while node.data != before_data:
                node = node.prev
                if node == None:
                    return False
            new = Node(data)
            before_new = node.prev
            before_new.next = new
            new.prev = before_new
            new.next = node
            node.prev = new
            return True


# In[65]:


double_linked_list = NodeMgmt(0)
for data in range(1, 10):
    double_linked_list.insert(data)
double_linked_list.desc()


# In[66]:


double_linked_list.insert_before(1.5,2)
double_linked_list.desc()


# In[67]:


node_3 = double_linked_list.search_from_tail(1.5)
node_3.data

