#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing Libraries
import numpy as np   
import pandas as pd 
import matplotlib.pyplot as plt


# In[2]:


#Loading data 
world_population_dataframe = pd.read_csv("D:\\Datasets\\Book1.csv")


# In[3]:


#DataFrame
world_population_dataframe


# In[4]:


#Grouping Individual country
uk_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
uk_data = uk_grouped.get_group("United Kingdom")
uk_data.head(100)
us_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
us_data = uk_grouped.get_group("United States")
us_data.head(100)
ru_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
ru_data = uk_grouped.get_group("Russia")
ru_data.head(100)


# In[7]:


# Generating Line plot
plt.plot(uk_data['Year'], uk_data['Population'] , color='red', linewidth=1.0,  label="United Kingdom")
plt.plot(us_data['Year'], us_data['Population'] , color='blue', linewidth=1.0,  label="United States")
plt.plot(ru_data['Year'], ru_data['Population'] , color='green', linewidth=1.0, label="Russia")
plt.title('Population')         
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.show()


# In[8]:


#Importing Libraries
import numpy as np   
import pandas as pd 
import matplotlib.pyplot as plt


# In[9]:


#Loading data
world_population_dataframe = pd.read_csv("D:\\Datasets\\Book1.csv")
#DataFrame
world_population_dataframe
#Grouping Individual country
uk_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
uk_data = uk_grouped.get_group("United Kingdom")
uk_data.head(100)
us_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
us_data = uk_grouped.get_group("United States")
us_data.head(100)
ru_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
ru_data = uk_grouped.get_group("Russia")
ru_data.head(100)


# In[13]:


#Generating Bar plot
plt.figure()
plt.bar(us_data['Year'], us_data['Population of children under the age of 1'] , color='yellow', width=0.7,  label="United States")
plt.bar(ru_data['Year'], ru_data['Population of children under the age of 1'] , color='black', width=0.7, label="Russia")
plt.bar(uk_data['Year'], uk_data['Population of children under the age of 1'] , color='red', width=0.7,  label="United Kingdom")
plt.xlabel("Year")   #x-axis 
plt.ylabel("under the age of 1")  #y-axis
plt.title("Population of children under the age of 1 based on country wise and year wise") #Title
plt.legend()
plt.show()


# In[16]:


#Generating Scatter plot
fig = plt.subplots(figsize =(8, 5))
plt.scatter(us_data['Year'], us_data['Population aged 90 to 99 years'] , color='Yellow', label="United States")
plt.scatter(ru_data['Year'], ru_data['Population aged 90 to 99 years'] , color='Blue',  label="Russia")
plt.scatter(uk_data['Year'], uk_data['Population aged 90 to 99 years'] , color='red',  label="United Kingdom")
plt.xlabel("Year")  #x-axis
plt.ylabel("Population aged 90 to 99 years")   #y-axis
plt.title("Population aged 90 to 99 years")    #Title
plt.legend()
plt.show()


# In[ ]:




