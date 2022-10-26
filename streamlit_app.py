
import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Lost Sales Dashboard')

with dataset:
    st.header('Data set by month')

    ls_data = pd.read_csv('data/Monthly_lost_sales.csv')
    st.write(ls_data.head())

    tier_distribution = pd.DataFrame(ls_data['TIER'].value_counts())
    st.bar_chart(tier_distribution)

with features:
    st.header('Reserved')

with model_training: 
    st.header('Reserved')