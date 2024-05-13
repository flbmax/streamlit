import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="workshop-international", page_icon='sporteasy_logo.png', layout="wide")

st.title(':flag-eu: :blue[Workshop International Team]')
st.markdown('2024-05-21')

with st.container():
    col1, col2, col3 = st.columns(3,gap='small')
    with col1:
        st.caption("Number of Clubs Clients")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=yrHngPc&theme=horizon&opt=nointeraction,noselections&select=$4-workshop::club.country_id,ES,GB,IT,NL,PT",
            height=100,
            width=170)
    with col2:
        st.caption("Current Sub Price")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=huvHjt&theme=horizon&opt=nointeraction,noselections&select=$4-workshop::club.country_id,ES,GB,IT,NL,PT" ,
            height=100,
            width=220)
    with col3:
        st.caption("Total Price")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=WNjgyN&theme=horizon&opt=nointeraction,noselections&select=$4-workshop::club.country_id,ES,GB,IT,NL,PT",
            height=100,
            width=250)

st.header('3. Typology of clubs by country today')

st.subheader(':green[a. Type Plan, Lifetime]')
# trellis clubs
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=LZWsLQr&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)

st.subheader(':green[b. Sport]')
# sport pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=sgmqJ&theme=horizon&opt=ctxmenu",
    height=400,
    width=1700)

st.subheader(':green[c. # Members in clubs]')
# members in clubs pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=Rthqzs&theme=horizon&opt=ctxmenu",
    height=400,
    width=1700)

st.subheader(':green[d. # Teams in clubs]')
# teams in clubs pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=MdyY&theme=horizon&opt=ctxmenu",
    height=400,
    width=1700)

st.subheader(':green[e. Clubs Region]')
# map of the clubs
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=CJLgCDy&theme=horizon&opt=ctxmenu",
    height=600,
    width=2000)

st.subheader(':green[f. Health Score]')
# clubs health score
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=thLrd&theme=horizon&opt=ctxmenu",
    height=500,
    width=1000)
st.write("The French trend is better : high-rated clubs are paying more")

st.subheader(':green[g. Main Features]')
# 3 top used features based on health score
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=YJhfvBP&theme=horizon&opt=ctxmenu&select=5-workshop::club.country_id,ES,GB,IT,NL,PT&select=5-workshop::club.current_plan,Integral%20Plan,Monthly%20Plan,Yearly%20Plan",
    height=220,
    width=800)

st.subheader(':green[h. Zoom on Collections]')
# collections use
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=208348cd-dc03-46da-a1d4-4047cedf6f77&obj=wFGPbM&theme=horizon&opt=ctxmenu" ,
    height=500,
    width=1100)
st.caption("The KYC France is just here to compare the trend not the value ")

# trellis with the activities by country
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=208348cd-dc03-46da-a1d4-4047cedf6f77&obj=djFv&theme=horizon&opt=ctxmenu",
    height=700,
    width=1000)
st.caption("*At least 3 authorised payments on the collections")
st.divider()
