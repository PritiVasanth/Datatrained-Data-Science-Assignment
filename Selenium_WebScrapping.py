#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[162]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium .webdriver.common.by import By
import time


# In[56]:


driver=webdriver.Chrome()
driver.get("https://www.shine.com/")


# In[61]:


designation=driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
designation.send_keys("Data Analyst")


# In[62]:


Location=driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input " )
Location.send_keys('Bangalore')


# In[63]:


search=driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button" )
search.click()


# In[71]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[72]:


#providing range to get first 10 data only
Title=driver.find_elements(By.XPATH,'//div[@class="parentClass position-relative"]/div/div[1]/div[1]/h2/a')
for i in Title[0:10]:
    title=i.text
    job_title.append(title)
print(job_title)


# In[74]:


Location=driver.find_elements(By.XPATH,'//div[@class="parentClass position-relative"]/div/div[1]/div[1]/div[3]/div[2]')
for i in Location[0:10]:
    location=i.text
    job_location.append(location)
print(job_location)


# In[75]:


Company=driver.find_elements(By.XPATH,'//div[@class="parentClass position-relative"]/div/div[1]/div[1]/div[2]/span')
for i in Company[0:10]:
    company=i.text
    company_name.append(company)
print(company_name)


# In[76]:


Experience=driver.find_elements(By.XPATH,'//div[@class="parentClass position-relative"]/div/div[1]/div[1]/div[3]/div[1]')
for i in Experience[0:10]:
    exp=i.text
    experience_required.append(exp)
print(experience_required)


# In[77]:


print(len(job_title),len(job_location),len(company_name),len(experience_required))


# In[78]:


df=pd.DataFrame({'Designation':job_title,'Location':job_location,'Company':company_name,'Experience':experience_required})
df


# In[79]:


driver=webdriver.Chrome()
driver.get("https://www.naukri.com/")


# In[80]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input  " )
designation.send_keys('Data Analyst')


# In[81]:


Location=driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
Location.send_keys('Bangalore')


# In[82]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit" )
search.click()


# In[95]:


job_title_n=[]
job_location_n=[]
company_name_n=[]
experience_required_n=[]


# In[96]:


# Scrape job data for the first 10 jobs using XPath
Title=driver.find_elements(By.XPATH,'//div[@class="styles_jlc__main__VdwtF"]/div/div[1]/div[1]/a')
for i in Title[0:10]:
    title=i.text
    job_title_n.append(title)
print(job_title_n)


# In[97]:


Location=driver.find_elements(By.XPATH,'//div[@class="styles_jlc__main__VdwtF"]/div/div[1]/div[3]/div/span[3]/span/span')
for i in Location[0:10]:
    location=i.text
    job_location_n.append(location)
print(job_location_n)


# In[98]:


Company=driver.find_elements(By.XPATH,'//div[@class="styles_jlc__main__VdwtF"]/div/div[1]/div[2]/span/a[1]')
for i in Company[0:10]:
    company=i.text
    company_name_n.append(company)
print(company_name_n)


# In[99]:


Experience=driver.find_elements(By.XPATH,'//div[@class="styles_jlc__main__VdwtF"]/div/div[1]/div[3]/div/span[1]/span/span' )
for i in Experience[0:10]:
    exp=i.text
    experience_required_n.append(exp)
print(experience_required_n)


# In[100]:


print(len(job_title_n),len(job_location_n),len(company_name_n),len(experience_required_n))


# In[101]:


df=pd.DataFrame({'Designation':job_title_n,'Location':job_location_n,'Company':company_name_n,'Experience':experience_required_n})
df


# In[186]:


driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")


# In[187]:


products=driver.find_element(By.CLASS_NAME,"Pke_EE" )
products.send_keys('sunglasses')


# In[188]:


search=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button" )
search.click()


# In[147]:


Sunglass_brand=[]
product_description=[]
Price=[]


# In[148]:


brand_name=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
for i in brand_name:
    brand=i.text
    Sunglass_brand.append(brand)
print(Sunglass_brand)


# In[149]:


Product_price=driver.find_elements(By.XPATH,'//a[@class="_3bPFwb"]/div[@class="_25b18c"]/div[1]')
for i in Product_price:
    price=i.text
    Price.append(price)
print(Price)


# In[150]:


Product_description=driver.find_elements(By.XPATH,'//div[@class="_1YokD2 _3Mn1Gg"]/div[@class="_1AtVbE col-12-12"]/div/div/div/div[1]/a[1]')

for i in Product_description:
    description=i.text
    product_description.append(description)
print(product_description)
print(len(product_description))


# In[151]:


print(len(Sunglass_brand),len(Product_description),len(Product_price))


# In[152]:


df=pd.DataFrame({'Brand_Name':Sunglass_brand,'Description':product_description,'Price':Price})
df


# In[211]:


start=0
end=3
Sunglass_brand=[]
product_description=[]
Price=[]
for page in range(start,end):
    brand_name=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in brand_name:
        brand=i.text
        Sunglass_brand.append(brand)  
    
    Product_price=driver.find_elements(By.XPATH,'//a[@class="_3bPFwb"]/div[@class="_25b18c"]/div[1]')
    
    for i in Product_price:
        price=i.text
        Price.append(price)  
    
    
    Product_description=driver.find_elements(By.XPATH,'//div[@class="_1YokD2 _3Mn1Gg"]/div[@class="_1AtVbE col-12-12"]/div/div/div/div[1]/a[1]')
    
    
    for i in Product_description:
        description=i.text
        product_description.append(description)
    
    next_button= driver.find_elements(By.XPATH,'//a[@class="_1LKTO3"]');
    
     
    if len(next_button)>1 :
        next_button[1].click()
    else:
        next_button[0].click()
     
    time.sleep(10)

        
    
    
    
print(len(Sunglass_brand),len(product_description),len(Price))
    
    


# In[212]:


df=pd.DataFrame({'Brand_Name':Sunglass_brand,'Description':product_description,'Product_Price':Price})
df


# In[ ]:




