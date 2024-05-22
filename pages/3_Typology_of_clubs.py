import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="workshop-international", page_icon='sporteasy_logo.png', layout="wide")

st.title(':flag-eu: :blue[Workshop International Team]')
st.markdown('2024-05-21')

with st.sidebar: 
    st.write("Choose the club country:")
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=bjAJDAZ&theme=horizon&opt=ctxmenu",
        height=140,
        width=200)

with st.container():
    col1, col2, col3 = st.columns(3,gap='small')
    with col1:
        st.caption("Number of Clubs Clients")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=yrHngPc&theme=horizon&opt=nointeraction,noselections",
            height=100,
            width=170)
    with col2:
        st.caption("Current Sub Price")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=huvHjt&theme=horizon&opt=nointeraction,noselections" ,
            height=100,
            width=220)
    with col3:
        st.caption("Total Price")
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=WNjgyN&theme=horizon&opt=nointeraction,noselections",
            height=100,
            width=250)

st.header('3. Typology of clubs by country today')

st.subheader(':green[a. Type Plan, Lifetime]')
# trellis clubs
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=LZWsLQr&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")

st.markdown(
    """
    <div style="display: block; height: 30vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- Integral Version begins to grow more in targeted countries
                <p>- Short lifetime for ES and IT -> <b>need to improve AM</b>
                </p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

st.subheader(':green[b. Sport]')
# sport pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=sgmqJ&theme=horizon&opt=ctxmenu",
    height=400,
    width=1700)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")

st.markdown(
    """
    <div style="display: block; height: 30vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- Rugby is a crucial sport (particularly in ES, where it has overtaken football and also in IT and NL where we signed big clubs)
                <p>- Cricket is n°2 sport in UK
                <p>- Volley (n°2 sport in IT after football) has a huge potential
                </p>
        </div>
    </div>""",
    unsafe_allow_html=True
)


st.subheader(':green[c. # Members in clubs]')
# members in clubs pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=Rthqzs&theme=horizon&opt=ctxmenu",
    height=500,
    width=1000)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")

st.markdown(
    """
    <div style="display: block; height: 30vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- Still signing small clubs (around 100 members)
                <p>- Average basket is lower
                <p>- Small clubs are often those with the less good grade, whereas medium/big clubs have better grades
        </div>
    </div>""",
    unsafe_allow_html=True
)
    
st.subheader(':green[d. # Teams in clubs]')
# teams in clubs pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=MdyY&theme=horizon&opt=ctxmenu",
    height=400,
    width=1700)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")


st.subheader(':green[e. Clubs Region]')
# map of the clubs
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=CJLgCDy&theme=horizon&opt=ctxmenu",
    height=600,
    width=2000)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")


st.subheader(':green[f. Health Score]')
# clubs health score
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=thLrd&theme=horizon&opt=ctxmenu" ,
    height=500,
    width=1000)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")
st.write("The French trend is better : high-rated clubs are paying more")

st.markdown(
    """
    <div style="display: block; height: 30vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- Gauss explanation
        </div>
    </div>""",
    unsafe_allow_html=True
)


st.subheader(':green[g. Main Features]')
# 3 top used features based on health score
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=YJhfvBP&theme=horizon&opt=ctxmenu",
    height=220,
    width=800)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")

st.markdown(
    """
    <div style="display: compact; flex-direction: column; justify-content: center; height: 60vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 30px;">
            <p>- Attendances are not much used (around 50%) when it's the core feature of SE
            <p>- Use of collections become interesting on markets like ES
            <p>- No use of club messaging system (because of WhatsApp ?)
            <p>- Apart from IT, the club database is not used (need to have an administrative tool in IT)
            <p>- Focus on NL :
            <p>* KNVB has a collab with Sportlink : dutch clubs have access to Sportlink Club.Basis and Club.Contribute products. It's administration tools.
            <p>* The Organisation and Communication tools are not in it (maybe juste a basis) : that's why some NL teams are interested in attendances ? Explianing the high Premium rates ?</p>
        </div>
    </div>""",
    unsafe_allow_html=True
)


#st.subheader(':green[h. Zoom on Collections]')
# collections use
#components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=208348cd-dc03-46da-a1d4-4047cedf6f77&obj=wFGPbM&theme=horizon&opt=ctxmenu" ,
#    height=500,
#    width=1100)
#st.caption("The KYC France is just here to compare the trend not the value ")
#st.caption("Data from **01/01/2022**")

# trellis with the activities by country
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=208348cd-dc03-46da-a1d4-4047cedf6f77&obj=djFv&theme=horizon&opt=ctxmenu",
    height=700,
    width=1000)
st.caption("*At least 3 authorised payments on the collections")
st.divider()
