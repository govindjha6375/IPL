import pandas as pd
import streamlit as st
import numpy as np

def show(team,df):
    
    req_df = df[df['TEAM'] ==  team]
    
    st.write("The player list which this team buy this year: ")
    st.dataframe(req_df[['PLAYERS','PRICE']])
    
    
    sum = 0
    for i in req_df['PRICE']:
        i  = i.split(",")
        i = "".join(i)
        sum = sum + int(i)
        
    st.write("Total Price spend by the team this year: ",sum)