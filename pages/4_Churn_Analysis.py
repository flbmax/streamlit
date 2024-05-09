import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="workshop-international", page_icon='sporteasy_logo.png', layout="wide")

st.title(':flag-eu: :blue[Workshop International Team]')
st.markdown('2024-05-21')

st.header('4. Churn Analysis')
st.caption('by country from 01/01/2019 to today')

st.subheader(':green[a. Numbers]')
with st.container():
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=hJUtP&theme=horizon&opt=ctxmenu&select=2-workshop::%3DIf(Match(club.country_id%2C'ES'%2C'IT'%2C'GB'%2C'NL'%2C'PT')%2Cclub.country_id),ES,GB,IT,NL,PT",
        height=50,
        width=1200)
    col1, col2, col3 = st.columns(3, gap='large')
    with col1:
        # results
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=Btfjt&theme=horizon&opt=ctxmenu&select=2-workshop::%3DIf(Match(club.country_id%2C'ES'%2C'IT'%2C'GB'%2C'NL'%2C'PT')%2Cclub.country_id),ES,GB,IT,NL,PT",
            height=400,
            width=600)
    with col3:
        # target
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=tNSLpW&theme=horizon&opt=ctxmenu&select=2-workshop::%3DIf(Match(club.country_id%2C'ES'%2C'IT'%2C'GB'%2C'NL'%2C'PT')%2Cclub.country_id),ES,GB,IT,NL,PT",
            height=400,
            width=600)




st.subheader(':green[b. 2024 Target]')
# target of renewal
with st.container():
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=LHhEnK&theme=horizon&opt=ctxmenu",
        height=100,
        width=1200)

    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=GQmHumj&theme=horizon&opt=ctxmenu&select=1-workshop::%3DIf(Match(club.country_id%2C'ES'%2C'IT'%2C'GB'%2C'NL'%2C'PT')%2Cclub.country_id),ES,GB,IT,NL,PT",
        height=400,
        width=1000)
