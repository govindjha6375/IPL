import streamlit as st
import pandas as pd

def show(name,df):
    
    req_df = df[df['PLAYERS'] == name]
    req_df = req_df.reset_index()
    
    st.write("Player Name: ",req_df['PLAYERS'][0])
    st.write("Nationality: ",req_df['NATIONALITY'][0])
    st.write("Type: ",req_df['TYPE'][0])
    st.write("Team: ",req_df['TEAM'][0])
    st.write("Price: ",req_df['PRICE'][0])