
import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title('Welcome')

with dataset:
    st.header('Lost sales DS')

    ls_data = pd.read_csv('data/Monthly_lost_sales.csv')
    st.write(ls_data.head())

    tier_distribution = pd.DataFrame(ls_data['MONTH_START_DATE'].value_counts())
    st.bar_chart(tier_distribution)

with features:
    st.header('The features I created')

with model_training: 
    st.header('Time to traiin the model')