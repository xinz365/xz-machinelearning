import streamlit as st
import pandas as pd

st.title('🤖 Machine Learning App')

st.info('This app builds a machine learning model!')

with st.expander('BLT Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://github.com/xinz365/xz-machinelearning/blob/master/blt_sample_streamlit.csv')
  df
