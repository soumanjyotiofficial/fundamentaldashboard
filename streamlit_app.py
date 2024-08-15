import  pandas as pd
import numpy as np
import streamlit as st
import requests as req
import plotly.express as xp
title = st.set_page_config(page_icon="", page_title="Dashboard", layout="wide")
st.markdown("""
            <style>
            #MainMenu{
            visibility:hidden
            }
            </style>
            
            """, unsafe_allow_html=True)


def extracting_date(name):
    url = f"https://www.screener.in/company/{name}/consolidated/"
    try:
        data=pd.read_html(url)
        return data
    except:
        return "No Such Company Data Found"
    

def sales_data(data):
    datatp = data[0].transpose()
    datatp_ = datatp.copy()
    new_cols = datatp_.iloc[0].to_dict()
    
        
    
    datatp.rename(columns=new_cols, inplace=True)
    datatp=datatp.iloc[1:]
    datatp.drop(columns="Raw PDF", inplace=True)
    
    sales =  {"years" : np.array(datatp.index),f"{list(new_cols.values())[0]}" : np.array(datatp[list(new_cols.values())[0]])}

    

    
    fig = xp.bar(sales,y=list(new_cols.values())[0],x="years", title="QOQ Sales")
    st.plotly_chart(fig)

def sales_data_line(data):
    datatp = data[0].transpose()
    datatp_ = datatp.copy()
    new_cols = datatp_.iloc[0].to_dict()
    
        
    
    datatp.rename(columns=new_cols, inplace=True)
    datatp=datatp.iloc[1:]
    datatp.drop(columns="Raw PDF", inplace=True)
    
    sales =  {"years" : np.array(datatp.index),f"{list(new_cols.values())[0]}" : np.array(datatp[list(new_cols.values())[0]])}

    

    
    fig = xp.line(sales,y=list(new_cols.values())[0],x="years", title="QOQ Sales")
    st.plotly_chart(fig)





header = st.title("Fundamanetal Dashboard")

col1, col2 = st.columns(2)
with col1:
    
    
    
    with st.form(key='my_form'):
        # Add form components (e.g., inputs)
        
        name = st.text_input('Enter your name')
        # Add the submit button inside the form
        submit_button = st.form_submit_button(label='Submit')
    
    
    


with col2:
    
    st.markdown("<h3> This is the Portfolio project on which I have worked. Tried to Create a Finacial Fundamantal Dashboard</h3>", unsafe_allow_html=True)

if submit_button:
    data = extracting_date(name)
    

    cols3, cols4 =st.columns(2)

    with cols3:
        st.title(f"{name.upper()}")
        sales_data(data)
        
