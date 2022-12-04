dataframe = dataset()

def DataAnalysis_section():
    st.text('Bellow is a sneak peak on to our dataset')
    st.dataframe(dataframe.data.head())

    st.text('Explotary Data Anlysis')
    st.text('Removing unneeded feature ')
    st.dataframe(dataframe.remove_id_unnamed)

    st.text('Analysis for target ')
    Target, Count_Target = dataframe.Target
    st.dataframe(Target)
    st.bar_chart(Target)
