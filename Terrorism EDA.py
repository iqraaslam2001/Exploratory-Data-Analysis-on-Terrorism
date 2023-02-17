#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import warnings
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.offline as py
import plotly.graph_objs as go
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')


# In[2]:


terror=pd.read_csv("C:\\Users\\IQRA\\Desktop\\Projects\\globalterrorismdb_0718dist.csv")


# In[3]:


terror.head()


# In[4]:


terror.columns


# In[5]:


#renaming the columns
terror.rename(columns={'iyear':'Year','imonth':'Month','iday':'Day','country_txt':'Country','provstate':'state',
                       'region_txt':'Region','attacktype1_txt':'AttackType','target1':'Target','nkill':'Killed',
                       'nwound':'Wounded','summary':'Summary','gname':'Group','targtype1_txt':'Target_type',
                       'weaptype1_txt':'Weapon_type','motive':'Motive'},inplace=True)


# In[6]:


terror1=terror[['Year','Month','Day','Country','state','Region','city','latitude','longitude','AttackType','Killed',
               'Wounded','Target','Summary','Group','Target_type','Weapon_type','Motive']]


# In[7]:


terror1.isnull().sum()


# In[8]:


terror1.info()


# In[10]:


print("Country with the most attacks:",terror1['Country'].value_counts().idxmax())
print("City with the most attacks:",terror1['city'].value_counts().index[1]) #since first entry is 'unknown'
print("Region with the most attacks:",terror1['Region'].value_counts().idxmax())
print("Year with the most attacks:",terror1['Year'].value_counts().idxmax())
print("Month with the most attacks:",terror1['Month'].value_counts().idxmax())
print("Group with the most attacks:",terror1['Group'].value_counts().index[1]) #since first entry is 'unknown'
print("Most Attack Types:",terror1['AttackType'].value_counts().idxmax())


# In[11]:


from wordcloud import WordCloud
from scipy import signal
cities = terror1.state.dropna(False)
plt.subplots(figsize=(10,10))
wordcloud = WordCloud(background_color = 'white',
                     width = 512,
                     height = 384).generate(' '.join(cities))
plt.axis('off')
plt.imshow(wordcloud)
plt.show()


# In[12]:


terror1['Year'].value_counts(dropna = False).sort_index()


# In[27]:


x_year = terror1['Year'].unique()
y_count_years = terror1['Year'].value_counts(dropna = False).sort_index()
plt.figure(figsize = (18,10))
sns.barplot(x = x_year,
           y = y_count_years,
           palette = 'rocket')
plt.xticks(rotation = 45)
plt.xlabel('Attack Year')
plt.ylabel('Number of Attacks each year')
plt.title('Yearly attacks')
plt.show()


# In[17]:


plt.subplots(figsize=(15,6))
sns.countplot('Year',data=terror1,palette='rainbow')
plt.xticks(rotation=45)
plt.title('Number Of Terrorist Activities Each Year')
plt.show()


# In[18]:


pd.crosstab(terror1.Year, terror1.Region).plot(kind='area',figsize=(15,6))
plt.title('Terrorist Activities by Region in each Year')
plt.ylabel('Number of Attacks')
plt.show()


# In[19]:


terror1['Wounded'] = terror1['Wounded'].fillna(0).astype(int)
terror1['Killed'] = terror1['Killed'].fillna(0).astype(int)
terror1['casualities'] = terror1['Killed'] + terror1['Wounded']


# In[20]:


terror2 = terror1.sort_values(by='casualities',ascending=False)[:40]


# In[21]:


heat=terror2.pivot_table(index='Country',columns='Year',values='casualities')
heat.fillna(0,inplace=True)


# In[22]:


heat.head()


# In[23]:


import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
colorscale = [[0, '#edf8fb'], [.3, '#00BFFF'],  [.6, '#8856a7'],  [1, '#810f7c']]
heatmap = go.Heatmap(z=heat.values, x=heat.columns, y=heat.index, colorscale=colorscale)
data = [heatmap]
layout = go.Layout(
    title='Top 40 Worst Terror Attacks in History from 1982 to 2016',
    xaxis = dict(ticks='', nticks=20),
    yaxis = dict(ticks='')
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='heatmap',show_link=False)


# In[24]:


terror1.Country.value_counts()[:15]


# In[28]:


plt.subplots(figsize=(15,6))
sns.barplot(terror1['Country'].value_counts()[:15].index,terror1['Country'].value_counts()[:15].values,palette='rocket')
plt.title('Top Countries Affected')
plt.xlabel('Countries')
plt.ylabel('Count')
plt.xticks(rotation= 90)
plt.show()


# In[ ]:




