import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Workshop International", page_icon='sporteasy_logo.png', layout="wide")

st.title(':flag-eu: :blue[Workshop International Team]')
st.markdown('2024-05-21')

with st.sidebar:
    st.write("Choose the current team type plan :")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=BtJcuV&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)

st.header('4. Churn Analysis')
st.caption('by country from 01/01/2019 to today')

with st.container():
    col1, col2, col3 = st.columns(3,gap='small')
    with col1:
        st.caption("Number of Churn")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=ztXWgsj&theme=horizon&opt=nointeraction,noselections",
            height=100,
            width=170)
    with col2:
        st.caption("2024 Loss")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=jhLZm&theme=horizon&opt=nointeraction,noselections" ,
            height=100,
            width=220)
    with col3:
        st.caption("Total Loss")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=BGyEw&theme=horizon&opt=nointeraction,noselections",
            height=100,
            width=250)

st.subheader(':green[a. Targets & Results]')
with st.container():
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=hJUtP&theme=horizon&opt=ctxmenu",
        height=60,
        width=400)
    # results
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=Btfjt&theme=horizon&opt=ctxmenu",
        height=400,
        width=650)
    # target
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=tNSLpW&theme=horizon&opt=ctxmenu",
        height=400,
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
with st.container():
    st.write("% renewed turnover")
    col1, col2, col3, col4, col5, col6 = st.columns(6, gap="small")
    with col1:
        st.caption("2019")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=qmULrH&theme=horizon&opt=nointeraction,noselections",
            height=60,
            width=100)
    with col2:
        st.caption("2020")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=JWaDJ&theme=horizon&opt=nointeraction,noselections",
            height=60,
            width=100)
    with col3:
        st.caption("2021")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=VUWJdSP&theme=horizon&opt=nointeraction,noselections",
            height=60,
            width=100)
    with col4:
        st.caption("2022")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=FUdderN&theme=horizon&opt=nointeraction,noselections",
            height=60,
            width=100)
    with col5:
        st.caption("2023")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=NTdnHf&theme=horizon&opt=nointeraction,noselections",
            height=60,
            width=100)
    with col6:
        st.caption("2024")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=jbEPTL&theme=horizon&opt=nointeraction,noselections",
            height=60,
            width=100) 
        
        
    with st.container():
        st.write("% renewed clubs")
        col1, col2, col3, col4, col5, col6 = st.columns(6, gap="small")
        with col1:
            st.caption("2019")
            components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=ynhjmJ&theme=horizon&opt=nointeraction,noselections",
                height=60,
                width=100)
        with col2:
            st.caption("2020")
            components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=pmpeU&theme=horizon&opt=nointeraction,noselections",
                height=60,
                width=100)
        with col3:
            st.caption("2021")
            components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=LQcT&theme=horizon&opt=nointeraction,noselections",
                height=60,
                width=100)
        with col4:
            st.caption("2022")
            components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=eYQQUQE&theme=horizon&opt=nointeraction,noselections",
                height=60,
                width=100)
        with col5:
            st.caption("2023")
            components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=YvtMmW&theme=horizon&opt=nointeraction,noselections",
                height=60,
                width=100)
        with col6:
            st.caption("2024")
            components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=uFLnErN&theme=horizon&opt=nointeraction,noselections",
                height=60,
                width=100)

multi = '''
We can notice the high number of churn clubs and the low number of churn in turnover, why ? **3 reasons** :

    1/ The churned clubs resulted in a loss of 2236,90 € in 2024. 

    2/ The upsell on renewed clubs was 1196,34 € in 2024

    3/ 1 monthly reacquired plan for the amount of 36,00 €

:warning: The net churn in turnover is therefore **1004,56 €**
'''
st.write(multi)

st.markdown(
    """
    <div style="display: compact; flex-direction: column; justify-content: center; height: 20vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 30px;">
            <p>- Losing half of the clubs but we can renew 90% of turnover
            <p>- Beginning of 2024 is worrying but on a low number of clubs (9/16). The main renew period is coming soon
            <p>- An more precise AM strategy more is necessary
            <p>- Now 282 clients outside France <b>and</b> not speaking French
        </div>
    </div>""",
    unsafe_allow_html=True
)

st.divider()
