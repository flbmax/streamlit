import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Workshop International", page_icon='sporteasy_logo.png', layout="wide")

st.title(':flag-eu: :blue[Workshop International Team]')
st.markdown('2024-05-21')

with st.sidebar:
    st.write("Choose the team type plan :")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=BtJcuV&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)
    
    st.write("Choose the country:")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=JgvMp&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)

st.header('5. Turnover Analysis YoY')
st.caption('by country from 01/01/2019 to today')

st.subheader(':green[a. Club Version]')
# turnover generated by club version
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=ZWByr&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)

st.subheader(':green[b. Premium Version]')
# turnover generated by team premium version
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=mSjqNZu&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)

st.divider()
