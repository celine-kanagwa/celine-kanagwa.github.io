import streamlit as st
from PIL import Image 



def MeetTeam():

    #<div style="text-align: center"> st.text("Meet the team") </div>
    st.markdown("<h1 style='text-align: center; color:purple;'>Meet The Team</h1>", unsafe_allow_html=True)

    


    col1,col2 = st.columns(2)

    with col1:
         st.text("HIRWA Celine")

         image = Image.open ('E:/PHOTOS/CELINE SANDRINE/679A9973_1.JPG')
         st.image (image, caption='')


    with col2:
         st.text("hirwa celine ") 
         image = Image.open ('E:/PHOTOS/CELINE SANDRINE/679A9973_1.JPG')
         st.image (image, caption='')   





      
