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
    
    st.write("Choose the team country:")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=JgvMp&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)

    st.write("Choose the club country:")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=bjAJDAZ&theme=horizon&opt=ctxmenu",
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

st.markdown(
    """
    <div style="display: block; height: 60vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- This only takes into account targeted countries (no South America for instance) hence the results are not a financial report but show the trend on targeted markets
                <p>- Should have a more exponential curve in 2024, as S2 should be significant
                <p>- Average basket increases YoY 
                <p>- We are currently on a +85% trend compare to the same period last year
                <p>- In February 2024, we top the performance of September 2023 (if we sum all countries with South America for example)
                <p>- <b>Global Revenue Figures :</b>
                        <p>* Forecast of 224 000€ INT (with 27% premium vs 41% in 2023)
                        <p>* 18% in FR in 2023
                        <p>* 61% in NL in 2023
                <p><b>62%</b> churn Premium INT / 57% in NL / 40 000€ loss in FR
                </p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

st.divider()
