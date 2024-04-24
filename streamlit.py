import streamlit as st
import pandas as pd 
table=pd.DataFrame({"column1":[1,2,3,4,5,6,7],"column2":[22,45,90,78,68,78,100]})
st.title("HI STREAMLIT IS POWERFUL FOR WEB APPLICATION")
st.write(table)
st.text('streamlit is used by data science for them to create visualization app in datascience.')