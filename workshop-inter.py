import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="worksop-international", layout="wide")

st.title('Workshop International Team')
st.markdown('2024-05-21')

st.header('1. Growth in number of users, teams & clubs')
st.caption('by country from 01/01/2019 to today')

st.subheader('a. Users')

components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu",
        height=100%,
        width=100%)






#qlik_teams = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu"


#embed_qlik_iframe(qlik_teams)



