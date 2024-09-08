import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import player_analysis,team_analysis

#setting page configuration
st.set_page_config(page_title="IPL Auction 2024 Data Report",page_icon="chart_with_upwards_trend",layout="wide")

final_df = pd.read_csv("IPL 2024 SOLD PLAYER DATA ANALYSIS.csv")

#Making the option menu at sidebar
with st.sidebar:
    selected = option_menu('IPL Auction 2024 Report',
                           ['Home', 'Player Analysis', 'Team Analysis'],
                           icons=['house', 'bi bi-7-square', 'bi bi-app-indicator'], default_index=0)
    
    
if selected == "Home":
    
    st.title("Welcome to IPL Auction 2024 Data Analysis")
    st.dataframe(final_df)
    
    
if selected == "Player Analysis":
    
    player_list = final_df['PLAYERS'].unique().tolist()
    name = st.selectbox("Select the Player:",player_list)
    
    if(st.button("Show Analysis")):
        player_analysis.show(name,final_df)

if selected == "Team Analysis":
    
    team_list = final_df['TEAM'].unique().tolist()
    team_name = st.selectbox("Select the Team:",team_list)
    
    if(st.button("Show Analysis")):
        team_analysis.show(team_name,final_df)

    