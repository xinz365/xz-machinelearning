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

with st.sidebar:
  st.header('Input Features')
  dispenserpressure_ecro = st.number_input('Dispenser Pressure')
  st.write("The current Dispenser Pressure is ", dispenserpressure_ecro)
  bondtimenothighforcearray_ecro = st.slider('Bond Time Not High Force Array',50, 300, 150)
  st.write("The current Bond Time Not High Force Array is ", bondtimenothighforcearray_ecro)
  dispensepatternclassselection_ecro = st.selectbox('Dispense Pattern Class Selection',('20','40'))
  st.write("The current Dispense Pattern Class Selection is ", dispensepatternclassselection_ecro)
  dispenseprinttime_ecro = st.selectbox('Dispense Print Time','30')
  st.write("The current Dispense Print Time is ", dispenseprinttime_ecro)
  dispenseprocessspeed_ecro = st.selectbox('Dispense Process Speed',('0.7','0.75','0.8'))
  st.write("The current Dispense Process Speed is ", dispenseprocessspeed_ecro)
  dispensewaittime_ecro
  dispenseheighttostrip_ecro
