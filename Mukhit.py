#!/usr/bin/env python
# coding: utf-8

# In[119]:


import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
from datetime import date,datetime,time,timezone
import folium
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# In[120]:


url='https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
data = pd.read_csv(r"C:\Users\Timing\Downloads\owid-covid-data.csv") #vzyal csv file and prochital ego s pomoshu' metoda
data.head() # Вывожу на экран первые 5 рядов


# In[121]:


data.tail() # Вывожу на экран последние 5 рядов


# In[122]:


data.columns #vyvel na ekran vse stolbcy


# In[123]:


data.isnull().sum() #vyvel na ekram summu elementov so znacheniem 0 


# In[124]:


data #vyvel na ekhan dataset


# In[125]:


data['total_cases'].mean()
# srednyaa total cases 


# In[126]:



df_country = data[data["iso_code"].str.contains("OWID")==False]
df_country['iso_code'].unique() #vyvel na ecran unikalniye elemente po stolbcu iso_code


# In[127]:


data_india = data.loc[data['location'] == 'India']
data_india #vyzval vse dannye po "location" sovpadayushie s India


# In[128]:


data_india=data.loc[data['location']=='India'] 
data_india=data_india.reset_index()
del data_india['index'] #


# In[129]:


data_india["date"] = pd.to_datetime(data_india["date"])
data_india["month"] = data_india["date"].dt.month
data_india


# In[130]:


data_india["date"] = pd.to_datetime(data_india["date"])
data_india["month"] = data_india["date"].dt.month
data_india


# In[131]:


data_ind=data_india.groupby('date').agg('mean')
data_ind
data_ind=data_india.set_index('date').resample('M').sum()
data_ind


# In[132]:


plt.figure(figsize=(16,8))
data_ind=data_ind.reset_index()
plt.bar(data_ind['date'],data_ind['total_cases'], color ='blue',
        width = 20)
plt.xlabel("date", size = 20)
plt.ylabel("Total Cases", size = 20) 
plt.title("Cases of Covid in India")
plt.show() # s pomoshu index vyvel diagrammu vse sluchai i po date

#

plt.figure(figsize=(16,10))
plt.bar(data_ind['date'],data_ind['total_deaths'], color ='red',
        width = 20)
plt.xlabel("date", size = 20)
plt.ylabel("Total Cases", size = 20)
plt.title("Deaths by Covid in India")
plt.show() # s pomoshu index vyvel diagrammu po smertnosti i po date




plt.figure(figsize=(16,10))
plt.bar(data_ind['date'],data_ind['people_vaccinated'], color ='orange',
        width = 20)
# plt.xticks(rotation = 'vertical', size = 15)

plt.xlabel("date", size = 20)
plt.ylabel("Total Cases", size = 20)
plt.title("People Vactinated in India")
plt.show() # s pomoshu index vyvel diagrammu vactinirovannykh i po date




plt.figure(figsize=(16,10))
plt.bar(data_ind['date'],data_ind['total_vaccinations'], color ='orange',
        width = 20)

plt.xlabel("DATE", size = 15)
plt.ylabel("Total Cases", size = 20)
plt.title("Vaccinated")
plt.show()




ind = df_country[df_country['location']=='India']
ind.head()



#sluchai zarazhenia v den (india)'''
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=ind['date'], y = ind['new_cases'],
    fill='toself',
    fillcolor='rgba(231,119,243,0.5)',
    line_color='rgba(255,255,255,0)',
    showlegend=False,
    
))
fig.add_trace(go.Scatter(
    x=ind['date'], y=ind['new_cases'],
    
    line_color='rgb(0,200,180)',
    
))

fig.show()




fig = px.line(ind, x="date", y="new_tests", title='Test of coronovirus in India')
fig.show()




map = folium.Map(location = [22.902453694490138, 79.51270254657462],
                zoom_start = 7, tiles = 'stamenterrain')

folium.Marker(location = [22.902453694490138, 79.51270254657462], popup = 'Индия').add_to(map)


folium.TileLayer('OpenStreetMap',
                 attr = 'OpenStreetMap').add_to(map)
folium.TileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', name='CartoDB.DarkMatter', attr="CartoDB.DarkMatter").add_to(map)
folium.LayerControl().add_to(map)

map




df = pd.read_csv(r"C:\Users\Timing\Downloads\owid-covid-data.csv")
covid_c = df.groupby(['location'])
total_df = covid_c.sum()
total_df.head()
center = [35.762887375145795, 84.08313219586536]

m = folium.Map(location = center, zoom_start = 2,
    max_bounds = True,
    min_zoom = 1, min_lat = -84,
    max_lat = 84, min_lon = -175, max_lon = 187,
   )

url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
country_geo = f"{url}/world-countries.json"


folium.Choropleth(
    geo_data = country_geo,
    data = total_df,
    columns = (total_df.index, 'total_vaccinations_per_hundred'),
    key_on = 'properties.name',
    fill_color = "RdYlGn",
    fill_opacity = 0.7,
    line_opacity = 0.5,
   ).add_to(m)

folium.LayerControl().add_to(m)

m


# In[95]:


dataset = pd.read_excel(r"C:\Users\Timing\Downloads\covid-19 India state cases.xlsx")
dataset.head()


# In[92]:


place=dataset[['Latitude','Longitude']]
place=place.values.tolist() 


# In[138]:


def mark(i,color):
    # Function to create marker
    folium.Marker(
        location=point, # To give Latitude and Longitude stored in point
        popup=dataset["State"][i] + " " + str(dataset["Confirmed Cases"][i]),  # Assigning label to the marker as State_name Confirmed covid cases
        icon=folium.Icon(
            color=color,  # Assigning color
            icon='tint',
            icon_color='white'
        )
    ).add_to(map)




i=0
for point in place:
    if dataset['Confirmed Cases'][i]>2000:
        # Alert
        mark(i,'darkred')
    elif dataset['Confirmed Cases'][i]>1000 and dataset['Confirmed Cases'][i]<=2000:
        # High Risk
        mark(i,'red')
    elif dataset['Confirmed Cases'][i]>500 and dataset['Confirmed Cases'][i]<=1000:
        # Risk
        mark(i,'lightred')
    elif dataset['Confirmed Cases'][i]>100 and dataset['Confirmed Cases'][i]<=500:
        # Average
        mark(i,'orange')
    elif dataset['Confirmed Cases'][i]>0 and dataset['Confirmed Cases'][i]<=100:
        # Below average
        mark(i,'green')
    i+=1
map


# In[112]:





# In[ ]:





# In[ ]:




