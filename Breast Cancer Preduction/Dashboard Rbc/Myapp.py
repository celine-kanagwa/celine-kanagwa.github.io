import streamlit as st
from visual_analysis import *
from PredModel import *
from MeetTeam import *

SIDEBAR_OPTION_PROJECT_WIKI = "Project Wiki"
SIDEBAR_OPTION_ANALYSIS = "Exploratory Data Analysis"
SIDEBAR_OPTION_TEAM = "Meet the Team"
SIDEBAR_OPTION_FORECAST = "Prediction"

SIDEBAR_OPTIONS = [SIDEBAR_OPTION_PROJECT_WIKI, SIDEBAR_OPTION_ANALYSIS, SIDEBAR_OPTION_FORECAST, SIDEBAR_OPTION_TEAM]


def wiki_section():

    
    st.subheader("BREAST CANCER DIOGNASIS PREDICTION")
    
    with st.expander("Short introduction about Breast cancer"):
         st.subheader(" ---------------------")
         st.write("""
         Breast cancer (BC) is one of the most common cancers among women worldwide. 
         The early diagnosis of BC can improve the prognosis and chance of survival, 
         as it can promote timely clinical treatment to patients.  the correct diagnosis of BC and classification of patients 
         into malignant or benign groups are the subject of my project.
         """)
         st.subheader("--------------------")
         st.write("""
        
         This analysis aims to observe which features are most helpful in predicting malignant or benign cancer
         and to see general trends that may aid us in model selection and hyper-parameter selection. 
         The goal is to classify whether the breast cancer is benign or malignant. 
         To achieve this I have used machine learning classification methods to fit
        a function that can predict the discrete class of new input
         """)

         

def visual_analysis_section():

    DataAnalysis_section()
    
def Prediction_section():

    PredModel()
   
def MeetTeam_section():

     
     MeetTeam()

def main():
    st.sidebar.success("Choose an option.")
    SIDEBAR_STATUS = st.sidebar.selectbox('Menu Option', SIDEBAR_OPTIONS)

    if SIDEBAR_STATUS == SIDEBAR_OPTION_PROJECT_WIKI:
        wiki_section()
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_ANALYSIS:
        visual_analysis_section()
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_FORECAST:
        Prediction_section()
    elif SIDEBAR_STATUS == SIDEBAR_OPTION_TEAM:
        MeetTeam_section()
    else:
        pass
main()    
