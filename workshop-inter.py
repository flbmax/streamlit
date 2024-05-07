import streamlit as st

st.set_page_config(page_title="worksop-international", layout="wide")

# Functions
def embed_qlik_iframe(iframe_url):
    st.components.v1.iframe(iframe_url, height=600, width=900)
# Functions

st.title('Workshop International Team')
st.markdown('2024-05-21')

st.header('1. Growth in number of users, teams & clubs')
st.caption('by country from 01/01/2019 to today')

st.subheader('a. Users')







#qlik_profiles = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=mzCzqu&theme=horizon&opt=ctxmenu"
#qlik_teams = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu"


#embed_qlik_iframe(qlik_profiles)
#embed_qlik_iframe(qlik_teams)



