import streamlit as st
import pandas as pd

st.title('Die Bond BLT Prediction App')
st.header("_Designed_ _for_ :blue[PCU12] _Only_")

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
  equipment_id = st.selectbox('EquipmentID', ('ES-161','ES-162'))
  st.write("Equipment_ID is ", equipment_id)
  date = st.selectbox('Date', ('2024-11-26','2024-11-27','2024-11-28','2024-11-29','2024-11-30'))
  st.write("Date is ", date)
  lot_id = st.selectbox('Lot_ID', ('SUPD35DNV000','SUPD35DNW000','SUPD35DNZ000','SUPD35DQR000','SUPD35EM0000'))
  st.write("Lot_ID is ", lot_id)
  strip_id = st.selectbox('Strip_ID', ('P131584725_0014','P131584725_0015','P131584725_0016','P131584725_0017','P131584725_0018'))
  st.write("Strip_ID is ", strip_id)
  die_position_x = st.selectbox('X', ('1','2','3','4','5'))
  st.write("Die Position X is ", die_position_x)
  die_position_y = st.selectbox('Y', ('1','2','3','4','5'))
  st.write("Die Position Y is ", die_position_y)
  
  data = {'equipment_id': equipment_id,
          'date': date,
          'lot_id': lot_id,
          'strip_id': strip_id,
          'die_position_x': die_position_x,
          'die_position_y': die_position_y}
  input_df = pd.DataFrame(data, index=[0])
  input_sample = pd.concat([input_df, X], axis=1)

st.info('**Please Confirm Your Input**')
input_df

st.info('**The BLT Model Prediction is**')
"**y[0]**"
