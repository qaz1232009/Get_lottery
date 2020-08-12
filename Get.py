#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[125]:


from bs4 import BeautifulSoup
url = 'https://www.taiwanlottery.com.tw/'
html = requests.get(url)
html.encoding='UTF-8'
sp = BeautifulSoup(html.text,'lxml')

wali = sp.select('.contents_box02')
print("威力彩日期"+wali[0].find_all('span')[0].text)
num_a = wali[0].find_all('div',class_='ball_tx ball_green')
num_sp = wali[0].find_all('div',class_='ball_red')

print('開出順序')
for i in num_a[:6]:
    print(i.text,end=' ')
print('\n大小順序')
for i in num_a[6:]:
    print(i.text,end=' ')
print()
print('特別號:'+num_sp[0].text)


# In[ ]:





# In[ ]:





# In[ ]:




