#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np   
import pandas as pd 
import matplotlib.pyplot as plt
world_population_dataframe = pd.read_csv("D:\\Datasets\\Book1.csv")
uk_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
uk_data = uk_grouped.get_group("United Kingdom")
uk_data.head(100)
us_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
us_data = uk_grouped.get_group("United States")
us_data.head(100)
ru_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
ru_data = uk_grouped.get_group("Russia")
ru_data.head(100)
plt.plot(uk_data['Year'], uk_data['Population'] , color='red', linewidth=1.0,  label="United Kingdom")
plt.plot(us_data['Year'], us_data['Population'] , color='blue', linewidth=1.0,  label="United States")
plt.plot(ru_data['Year'], ru_data['Population'] , color='green', linewidth=1.0, label="Russia")
plt.title('Growth of Population')
plt.xlabel('x_axis Year')
plt.ylabel('y_axis Billion')
#plt.grid(True)
plt.legend()
plt.show()


# In[3]:


import numpy as np   
import pandas as pd 
import matplotlib.pyplot as plt
world_population_dataframe = pd.read_csv("D:\\Datasets\\Book1.csv")
uk_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
uk_data = uk_grouped.get_group("United Kingdom")
uk_data.head(100)
us_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
us_data = uk_grouped.get_group("United States")
us_data.head(100)
ru_grouped = world_population_dataframe.groupby(world_population_dataframe['Country name'])
ru_data = uk_grouped.get_group("Russia")
ru_data.head(100)
plt.figure()
plt.bar(us_data['Year'], us_data['Population of children under the age of 1'] , color='yellow', width=0.7,  label="United States")
plt.bar(ru_data['Year'], ru_data['Population of children under the age of 1'] , color='black', width=0.7, label="Russia")
plt.bar(uk_data['Year'], uk_data['Population of children under the age of 1'] , color='red', width=0.7,  label="United Kingdom")
plt.xlabel("Year")
plt.ylabel("under the age of 1")
plt.title("Population of children under the age of 1 based on country wise and year wise")
plt.legend()
plt.show()
fig = plt.subplots(figsize =(8, 5))
plt.scatter(us_data['Year'], us_data['Population aged 90 to 99 years'] , color='Yellow', label="United States")
plt.scatter(ru_data['Year'], ru_data['Population aged 90 to 99 years'] , color='Blue',  label="Russia")
plt.scatter(uk_data['Year'], uk_data['Population aged 90 to 99 years'] , color='red',  label="United Kingdom")
plt.xlabel("Year")
plt.ylabel("Population aged 90 to 99 years")
plt.title("Population aged 90 to 99 years")
plt.legend()
# depict illustration
plt.show()


# In[ ]:




