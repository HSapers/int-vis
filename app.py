import streamlit as st
import pandas as pd
import plotly.express as px

#set up
st.set_page_config(layout='wide')
st.title("Interact with Gapminder Data")

df = pd.read_csv("gapminder_tidy.csv")

#get lists of continents and metrics
continent_list = list(df['continent'].unique())
metric_list = list(df['metric'].unique())

#variables
#continent = 'Europe'
#metric = 'pop'

#widgets
with st.sidebar: #implements side bar function and do that with these things
    st.subheader("Configure the plot")
    continent = st.selectbox(label='Choose a continent', options=continent_list)
    metric = st.selectbox(label='Choose a metric', options=metric_list)

#query
query = f"continent=='{continent}' & metric=='{metric}'"                        

#df_gdp_o = df.query("continent=='Oceania' & metric=='gdpPercap'") hardcoded
#df_gdp_o = df.query(f"continent=='{continent}' & metric=='{metric}'") #use variables

df_gdp = df.query(query) #use more variables
metric_labels = {'gdpPercap' : 'GDP Per Capita', 'lifeExp' : 'Average Life Expectancy', 'pop' : 'Population'} #make the metric labels nice
#title = 'GDP for countries in Oceania' #hard coded
title = f"{metric_labels[metric]} for countries in {continent}"



fig = px.line(df_gdp, x = "year", y = "value", color = 'country', title=title)

st.plotly_chart(fig, use_container_width=True)
