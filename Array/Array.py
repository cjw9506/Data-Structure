#!/usr/bin/env python
# coding: utf-8

# ## 꼭 알아둬야 할 자료구조: 배열(Arrray)
# - 데이터를 나열하고, 각 데이터를 인덱스에 대응하도록 구성한 데이터 구조
# - 파이썬에서는 리스트 타입이 배열 기능을 제공하고 있음
# 

# 배열의 장점
# - 빠른 접근 가능
# 배열의 단점
# - 추가, 삭제가 쉽지 않음.
# - 미리 최대 길이를 지정해야 함(최대 길이를 모르면 추가/삭제 어려움)
# 

# In[5]:


country = 'US'
print(country)
country += 'A'
print(country)


# ### 파이썬과 배열
# -파이썬 리스트 활용

# In[7]:


#1차원 배열: 리스트로 구현시
data = [1,2,3,4,5]
print(data)


# In[9]:


#2차원 배열: 리스트로 구현시
data = [[1,2,3],[4,5,6],[7,8,9]]
print(data)


# In[11]:


print(data[0])


# In[12]:


print(data[0][0])


# In[13]:


print(data[2][2],data[2][1],data[2][0])


# In[15]:


dataset = ['Braund, Mr. Owen Harris',
'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
'Heikkinen, Miss. Laina',
'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
'Allen, Mr. William Henry',
'Moran, Mr. James',
'McCarthy, Mr. Timothy J',
'Palsson, Master. Gosta Leonard',
'Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg)',
'Nasser, Mrs. Nicholas (Adele Achem)',
'Sandstrom, Miss. Marguerite Rut',
'Bonnell, Miss. Elizabeth',
'Saundercock, Mr. William Henry',
'Andersson, Mr. Anders Johan',
'Vestrom, Miss. Hulda Amanda Adolfina',
'Hewlett, Mrs. (Mary D Kingcome) ',
'Rice, Master. Eugene',
'Williams, Mr. Charles Eugene',
'Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)',
'Masselmani, Mrs. Fatima',
'Fynney, Mr. Joseph J',
'Beesley, Mr. Lawrence',
'McGowan, Miss. Anna "Annie"',
'Sloper, Mr. William Thompson',
'Palsson, Miss. Torborg Danira',
'Asplund, Mrs. Carl Oscar (Selma Augusta Emilia Johansson)',
'Emir, Mr. Farred Chehab',
'Fortune, Mr. Charles Alexander',
'Dwyer, Miss. Ellen "Nellie"',
'Todoroff, Mr. Lalio']
#array 안에 M의 갯수 찾기
m_count = 0
for i in range(len(dataset)):
    m_count += dataset[i].count('M')
print(m_count)

