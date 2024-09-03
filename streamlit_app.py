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
  bondprocessbondztouchheight_ecro = st.number_input('Bond Z Touch Height')
  st.write("The current Bond Z Touch Height is ", bondprocessbondztouchheight_ecro)
  dvipostdispenseshapecheckdatainner = st.number_input('Post Dispenser Shape Check Inner')
  st.write("The current Post Dispenser Shape Check Inner is ", dvipostdispenseshapecheckdatainner)
  dvipostdispenseshapecheckdataouter = st.number_input('Post Dispenser Shape Check Outer')
  st.write("The current Post Dispenser Shape Check Outer is ", dvipostdispenseshapecheckdataouter)
  pbiepoxycoverage_left = st.number_input('Epoxy Coverage Left')
  st.write("The current Epoxy Coverage Left is ", pbiepoxycoverage_left)
  pbiepoxycoverage_top = st.number_input('Epoxy Coverage Top')
  st.write("The current Epoxy Coverage Top is ", pbiepoxycoverage_top)
  pbiepoxycoverage_right = st.number_input('Epoxy Coverage Right')
  st.write("The current Epoxy Coverage Right is ", pbiepoxycoverage_right)
  pbiepoxycoverage_bottom = st.number_input('Epoxy Coverage Bottom')
  st.write("The current Epoxy Coverage Bottom is ", pbiepoxycoverage_bottom)
  bondtimenothighforcearray_ecro = st.slider('Bond Time Not High Force Array',50, 300, 150)
  st.write("The current Bond Time Not High Force Array is ", bondtimenothighforcearray_ecro)
  dispensepatternclassselection_ecro = st.selectbox('Dispense Pattern Class Selection',('20','40'))
  st.write("The current Dispense Pattern Class Selection is ", dispensepatternclassselection_ecro)
  dispenseprinttime_ecro = st.selectbox('Dispense Print Time','30')
  st.write("The current Dispense Print Time is ", dispenseprinttime_ecro)
  dispenseprocessspeed_ecro = st.selectbox('Dispense Process Speed',('0.7','0.75','0.8'))
  st.write("The current Dispense Process Speed is ", dispenseprocessspeed_ecro)
  dispensewaittime_ecro = st.slider('Dispense Wait Time',50, 200, 100)
  st.write("The current Dispense Wait Time is ", dispensewaittime_ecro)
  dispenseheighttostrip_ecro = st.selectbox('Dispense Height to Strip',('120','130','140'))
  st.write("The current Dispense Height to Strip is ", dispenseheighttostrip_ecro)

  data = {'dispenserpressure_ecro': dispenserpressure_ecro,
          'bondtimenothighforcearray_ecro': bondtimenothighforcearray_ecro,
          'dispensepatternclassselection_ecro': dispensepatternclassselection_ecro,
          'dispenseprinttime_ecro': dispenseprinttime_ecro,
          'dispenseprocessspeed_ecro': dispenseprocessspeed_ecro,
          'dispensewaittime_ecro': dispensewaittime_ecro,
          'dispenseheighttostrip_ecro': dispenseheighttostrip_ecro,
          'dvipostdispenseshapecheckdatainner': dvipostdispenseshapecheckdatainner,
          'dvipostdispenseshapecheckdataouter': dvipostdispenseshapecheckdataouter,
          'pbiepoxycoverage_left': pbiepoxycoverage_left,
          'pbiepoxycoverage_top': pbiepoxycoverage_top,
          'pbiepoxycoverage_right': pbiepoxycoverage_right,
          'pbiepoxycoverage_bottom': pbiepoxycoverage_bottom,
          'bondprocessbondztouchheight_ecro': bondprocessbondztouchheight_ecro}
  input_df = pd.DataFrame(data, index=[0])
  input_sample = pd.concat([input_df, X], axis=0)

input_df
  
