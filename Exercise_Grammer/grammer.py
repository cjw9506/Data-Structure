#!/usr/bin/env python
# coding: utf-8

# In[6]:


#소수점 출력
print("%0.0f"% 3.1415)
print("%0.1f"% 3.1415)
print("%0.2f"% 3.1415)
print("%0f"% 3.1415)
print("%1f"% 3.1415)


# In[7]:


#형변환
a = "720"
b = int(a)
print(b)


# In[10]:


#연산
data1 = 2
data2 = 4
print(data1+data2)
print(data1/data2)
print(data1%data2)
print(data1**data2)


# In[13]:


# \n은 한줄 아래로 \t는 space 한번
code = '000660\n0000102\t1212'
print(code)


# In[14]:


#문자열
mystr = "a man goes into the room..."
print(mystr.strip('.')) #strip 함수 유의


# In[15]:


#문자열 인덱싱
letters = "python"
print(letters[1])


# In[16]:


#split
letter = "Dave,David,Andy"
letter_list = letter.split(',')
print(letter_list)


# In[37]:


#리스트+반복문
num_list = [0, -11, 31, 22, -11, 33, -44, -55]
for index, num in enumerate(num_list): # 이 문법 잘 사용할 것
    if num < 0:
        del num_list[index]
print(num_list)

    


# In[40]:


#리스트+반복문2
list_data = ["fun-coding", "Dave", "Linux", "Python", "javascript", "front-end", "back-end", "dataengineering"]
for index, data in enumerate(list_data):
    print(len(data))


# In[50]:


#리스트+반복문+문자열다루기 
filelist = ['exercise01.docx', 'exercise02.docx', 'exercise03.docx', 'exercise04.docx', 'exercise05.docx']
for filename in filelist:
    print(filename.split('.')[0])
#split+인덱싱이 가능하다


# In[63]:


#튜플 
tuple_data = ("a","b","c","d","e")
print(tuple_data[0])
#소괄호로 만들고 대괄호로 인덱싱


# In[67]:


var1, var2 = 1, 2
var1, var2 = var2, var1
print(var1)


# In[70]:


tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3', 'fun-coding4', 'fun-coding5')

tupledata[1:]


# In[73]:


tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
listdata = list(tupledata)
listdata.append('fun-coding4')
tupledata = tuple(listdata)
tupledata


# In[74]:


tupledata = tuple()
listdata = list()
dictdata = dict()
print(type(tupledata),type(listdata),type(dictdata))


# In[84]:


#딕셔너리
dictdata = {'environment':'환경', 'company':'회사','government':'정부','face':'얼굴'}
dic_keys = [data for data in dictdata.keys()]
dic_values = [data for data in dictdata.values()]
print(dic_keys)
print(dic_values)
print(dictdata.keys())
print(dictdata.values())


# In[89]:


#딕셔너리 합치기
dict_all = {'environment': '환경', 'gonernment':'정부, 정치'}
dict2 = {'company': '회사', 'face':'얼굴'}
dict3 = {'apple': '사과'}
for data in dict2.keys():
    dict_all[data] = dict2[data]
for data in dict3.keys():
    dict_all[data] = dict3[data]
print(dict_all)


# In[93]:


#딕셔너리 원하는 데이터 출력
actor_info = {'actor_details': {'생년월일': '1971-03-01',
                   '성별': '남',
                   '직업': '배우',
                   '홈페이지': 'https://www.instagram.com/madongseok'},
 'actor_name': '마동석',
 'actor_rate': 59361,
 'date': '2017-10',
 'movie_list': ['범죄도시', '부라더', '부산행']}
print("배우이름 : "+ actor_info['actor_name'])


# In[94]:


#set ㅡ> 중복제거
number_list = [5, 1, 2, 2, 3, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10, 10]
set(number_list)


# In[ ]:




