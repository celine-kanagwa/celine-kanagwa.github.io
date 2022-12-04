import streamlit as st
from BreastData import dataset


dataframe = dataset()

def DataAnalysis_section():
   
     col1, col2 = st.columns(2)

     with col1:
         st.text('Bellow is a Breast Cancer dataset')
         st.dataframe(dataframe.data.head())

     with col2:
          st.text('Explotary Data Anlysis')

          st.dataframe(dataframe.remove_id_unnamed)

    
     st.text('Diognasis Target values on graph ')
     Target, Count_Target = dataframe.Target
     st.bar_chart(Target)
        
     st.text("Relationship Between features")
     st.dataframe(dataframe.Corr_graph)   