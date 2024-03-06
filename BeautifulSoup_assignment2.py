#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[2]:


from bs4 import BeautifulSoup
import requests


# In[18]:


page=requests.get('https://www.imdb.com/list/ls056092300/')
page


# In[21]:


soup=BeautifulSoup(page.content)
soup


# In[23]:


name=soup.find('h3', class_='lister-item-header')
print(name.a.text)


# In[27]:


rating=soup.find('span', class_="ipl-rating-star__rating")
rating.text


# In[7]:


year_of_release=soup.find('span', class_="lister-item-year text-muted unbold")
year_of_release.text


# In[24]:


Name= []
for i in soup.find_all('h3',class_="lister-item-header"):
    Name.append(i.a.text)
Name


# In[41]:


Rating= []
for rating_div in soup.find_all('div', class_="ipl-rating-star small"):
    Rating.append(rating_div.find_next('span').find_next('span').text)

Rating

    
    


# In[42]:


Year_of_release= []
for i in soup.find_all('span', class_="lister-item-year text-muted unbold"):
    Year_of_release.append(i.text)
Year_of_release


# In[43]:


print(len(Name),len(Rating), len(Year_of_release))


# In[44]:


import pandas as pd


# In[45]:


df=pd.DataFrame({'Name':Name,'Rating':Rating,'Year_of_release':Year_of_release})
df


# In[50]:


page=requests.get(' https://www.keaipublishing.com/en/journals/artificial-intelligence-in-agriculture/most-downloaded-articles/')
page


# In[51]:


soup=BeautifulSoup(page.content)
soup


# In[53]:


Paper_title=soup.find('h2',class_="h5 article-title")
Paper_title.text


# In[54]:


Date=soup.find('p',class_="article-date")
Date.text


# In[55]:


Author=soup.find('p',class_="article-authors")
Author.text


# In[69]:


Paper_title= []
for i in soup.find_all('h2',class_="h5 article-title"):
    Paper_title.append(i.a.text.replace("\n","").replace("\r","").strip())
Paper_title


# In[58]:


Date=[]
for i in soup.find_all('p',class_="article-date"):
    Date.append(i.text)
Date


# In[59]:


Author=[]
for i in soup.find_all('p',class_="article-authors"):
    Author.append(i.text)
Author


# In[70]:


print(len(Paper_title),len(Date),len(Author))


# In[71]:


df=pd.DataFrame({'Paper_Title':Paper_title,'Date':Date,'Author':Author })
df


# In[81]:


page=requests.get('https://www.nobroker.in/property/sale/bangalore/multiple?searchParam=W3sibGF0IjoxMi45NzgzNjkyLCJsb24iOjc3LjY0MDgzNTYsInBsYWNlSWQiOiJDaElKa1FOM0dLUVdyanNSTmhCUUpyaEdEN1UiLCJwbGFjZU5hbWUiOiJJbmRpcmFuYWdhciJ9LHsibGF0IjoxMi45MzA3NzM1LCJsb24iOjc3LjU4MzgzMDIsInBsYWNlSWQiOiJDaElKMmRkbFo1Z1ZyanNSaDFCT0FhZi1vcnMiLCJwbGFjZU5hbWUiOiJKYXlhbmFnYXIifSx7ImxhdCI6MTIuOTk4MTczMiwibG9uIjo3Ny41NTMwNDQ1OTk5OTk5OSwicGxhY2VJZCI6IkNoSUp4Zlc0RFBNOXJqc1JLc05URy01cF9RUSIsInBsYWNlTmFtZSI6IlJhamFqaW5hZ2FyIn1d&radius=2.0&city=bangalore&locality=Indiranagar,Jayanagar,Rajajinagar')
page


# In[82]:


soup=BeautifulSoup(page.content)
soup


# In[104]:


House_Title=soup.find('h2', class_="heading-6 flex items-center font-semi-bold m-0")
House_Title.a.text


# In[105]:


Location=soup.find('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95")
Location.text


# In[106]:


Price=soup.find('div',class_="font-semi-bold heading-6")
Price.span.text


# In[116]:


Estimated_EMI=soup.find('div',class_="font-semi-bold heading-6")
Estimated_EMI.text


# In[167]:


House_Title=[]
for i in soup.find_all('h2', class_="heading-6 flex items-center font-semi-bold m-0"):
    House_Title.append(i.text)
House_Title


# In[166]:


Location=[]
for i in soup.find_all('div',class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95"):
    Location.append(i.text)
Location


# In[168]:


Price=[]
for i in soup.find_all('div',class_="flex flex-col w-33pe items-center bo tp:w-half po:w-full border-r border-r-solid border-card-overview-border-color last:border-r-1"):
    if i.get("id") == "minDeposit":
        Price.append(i.div.text)
    
Price     
   


# In[169]:


emi_Price=[]
for i in soup.find_all('div',class_="font-semi-bold heading-6"):
    if i.get("id") == "roomType":
        emi_Price.append(i.text)
emi_Price


# In[170]:


print(len(House_Title),len(Location),len(Price),len(emi_Price))


# In[171]:


df=pd.DataFrame({"House Title" : House_Title, "Location" : Location, "Price" : Price, "Estimated Monthly Installment":emi_Price})
df


# In[ ]:




