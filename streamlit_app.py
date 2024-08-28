import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This app builds a machine learning model!')

with st.expander('BLT Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('blt_sample_steamlit.csv')
  df
