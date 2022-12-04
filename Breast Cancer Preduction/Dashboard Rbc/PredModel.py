from re import sub
import streamlit as st
from BreastData import dataset
import pickle

# Breast_cancer_model = pickle.load('./Breast_Cancer_model.pkl')

with open ('Breast_cancer_model.pkl', 'rb')as f: 
    Breast_cancer_model = pickle.load(f)

dataframe = dataset()

def PredModel():
    st.text("Model Prediction using Logististic ")
    input = dict()


    with st.form("ai form"):
        col1, col2, col3 = st.columns(3)

        with col1:
             radius_mean= st.selectbox('Radius Mean',(set(dataframe.data['radius_mean'])))
             texture_mean= st.selectbox('Texture Mean', (set(dataframe.data['texture_mean'])))
             perimeter_mean = st.selectbox('Perimeter Mean',(set(dataframe.data['perimeter_mean'])))
             area_mean= st.selectbox('area Mean',(set(dataframe.data['area_mean'])))
             smoothness_mean = st.selectbox('smoothness Mean',(set(dataframe.data['smoothness_mean'])))
             compactness_mean = st.selectbox('compactness Mean',(set(dataframe.data['compactness_mean'])))
             concavity_mean= st.selectbox('concavity Mean',(set(dataframe.data['concavity_mean'])))
             concave_points_mean = st.selectbox('concave_points Mean',(set(dataframe.data['concave points_mean'])))
             symmetry_mean  = st.selectbox('symmetry Mean',(set(dataframe.data['symmetry_mean' ])))
       
        with col2:
             radius_se= st.selectbox('Radius sd',(set(dataframe.data['radius_se'])))
             perimeter_se = st.selectbox('Perimeter sd',(set(dataframe.data['perimeter_se'])))
             area_se= st.selectbox('area sd',(set(dataframe.data['area_se'])))
             compactness_se = st.selectbox('compactness sd',(set(dataframe.data['compactness_se'])))
             concavity_se= st.selectbox('concavity sd',(set(dataframe.data['concavity_se'])))
             concave_points_se = st.selectbox('concave_points sd ',(set(dataframe.data['concave points_se'])))
     

        with col3:
             radius_worst = st.selectbox('Radius worst',(set(dataframe.data['radius_worst'])))
             texture_worst = st.selectbox('Texture worst', (set(dataframe.data['texture_worst'])))
             perimeter_worst  = st.selectbox('Perimeter worst',(set(dataframe.data['perimeter_worst'])))
             area_worst  = st.selectbox('area_worst',(set(dataframe.data['area_worst'])))
             smoothness_worst= st.selectbox('smoothness worst',(set(dataframe.data['smoothness_worst'])))
             compactness_worst = st.selectbox('compactness worst',(set(dataframe.data['compactness_worst'])))
             concavity_worst= st.selectbox('concavity worst',(set(dataframe.data['concavity_worst'])))
             concave_points_worst = st.selectbox('concave_points worst ',(set(dataframe.data['concave points_worst'])))
             symmetry_worst = st.selectbox('symmetry worst',(set(dataframe.data['symmetry_worst' ])))
             fractal_dimension_worst= st.selectbox(' Fractal dimension wrost',(set(dataframe.data['fractal_dimension_worst'])))

     
        submitted = st.form_submit_button("Submit")
        if submitted:

          input['radius_mean'] = radius_mean
          input['texture_mean'] = texture_mean 
          input['perimeter_mean']=perimeter_mean
          input['area_mean']=area_mean
          input['smoothness_mean']=smoothness_mean
          input['compactness_mean']=compactness_mean
          input['concavity_mean']=concavity_mean
          input['concave points_mean']=concave_points_mean
          input['symmetry_mean' ]= symmetry_mean

          input['radius_se']= radius_se
          input['perimeter_se'] = perimeter_se
          input['area_se'] = area_se
          input['compactness_se'] = compactness_se
          input['concavity_se'] = concave_points_se
          input['concave points_se'] = concave_points_se
         

          input['radius_worst'] = radius_worst
          input['texture_worst'] = texture_worst
          input['perimeter_worst'] = perimeter_worst
          input['area_worst'] = area_worst
          input['smoothness_worst'] = smoothness_worst
          input['compactness_worst']= compactness_worst
          input['concavity_worst'] = compactness_worst
          input['concave points_worst'] = concave_points_worst
          input['symmetry_worst' ]=symmetry_worst
          input['fractal_dimension_worst']=fractal_dimension_worst 

               # predicting for the model
          prediction = Breast_cancer_model.predict([[
               input['radius_mean'],
               input['texture_mean'],
               input['perimeter_mean'],
               input['area_mean'],
               input['smoothness_mean'],
               input['compactness_mean'],
               input['concavity_mean'],
               input['concave points_mean'],
               input['symmetry_mean'],

               input['radius_se'],
               input['perimeter_se'],
               input['area_se'],
               input['compactness_se'],
               input['concavity_se'],
               input['concave points_se'],
          

               input['radius_worst'],
               input['texture_worst'],
               input['perimeter_worst'],
               input['area_worst'],
               input['smoothness_worst'],
               input['compactness_worst'],
               input['concavity_worst'],
               input['concave points_worst'],
               input['symmetry_worst'],
               input['fractal_dimension_worst']


               ]])
               
               
               
          st.subheader('PREDICTED DIAGNOSIS BREAST CANCER')
          st.subheader(int(prediction[0]))
 

        
        
         



              
    

    