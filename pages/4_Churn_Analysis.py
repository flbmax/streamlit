import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="workshop-international", page_icon='sporteasy_logo.png', layout="wide")

st.title(':flag-eu: :blue[Workshop International Team]')
st.markdown('2024-05-21')

st.header('4. Churn Analysis')
st.caption('by country from 01/01/2019 to today')

st.subheader(':green[a. Targets & Results]')
with st.container():
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=hJUtP&theme=horizon&opt=ctxmenu",
        height=60,
        width=400)
    # results
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=Btfjt&theme=horizon&opt=ctxmenu",
        height=300,
        width=650)
    # target
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=tNSLpW&theme=horizon&opt=ctxmenu",
        height=300,
        width=650)


st.subheader(':green[b. 2024 Objective]')
# target of renewal
with st.container():
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=LHhEnK&theme=horizon&opt=ctxmenu",
        height=60,
        width=400)

    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=GQmHumj&theme=horizon&opt=ctxmenu",
        height=400,
        width=1000)
    
st.subheader(':green[c. Churn rates YoY]')
# compare churn rates in number of clubs & amount
row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(border=True)
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=AarkBp&theme=horizon&opt=nointeraction,noselections&select=$::club.country_id,ES,GB,IT,NL,PT",
        height=60,
        width=400)


