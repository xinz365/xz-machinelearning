import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.info('This app builds a machine learning model!')

with st.expander('BLT Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('blt_sample_steamlit.csv')
  df
  
  st.write('**X**')
  X = df.drop('blt', axis=1)
  X

  st.write('**y**')
  y = df.blt
  y
  
with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='dispenserpressure_ecro', y='blt', color='dispensepatternclassselection_ecro')

#Data Preparation
with st.sidebar():
  st.header('Input Features')
  dispenserpressure_ecro = st.number_input('Dispenser Pressure')
  st.write("The current Dispenser Pressure is ", dispenserpressure_ecro)
