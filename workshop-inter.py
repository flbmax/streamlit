import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="workshop-international", page_icon='sporteasy_logo.png', layout="wide")

st.title(':flag-eu: :blue[Workshop International Team]')
st.markdown('2024-05-21')

st.header('1. Growth in number of users, teams & clubs')
st.caption('by country from 01/01/2019 to today')

st.subheader(':green[a. Users]')
# profiles created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=mzCzqu&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('*using profile.default_language to determine the country')


col1, col2 = st.columns(2, gap='large')
with col1:
    st.subheader(':green[b. Teams]')
    # teams created
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu",
            height=500,
            width=650)
    st.caption('*using team.country_id to determine the country')
with col2:
    st.subheader(':green[c. Clubs]')
    # clubs created
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=juSbKpp&theme=horizon&opt=ctxmenu",
            height=500,
            width=650)
    st.caption("Client : au moins un paiement autorisé ou en chargeback sur SportEasy - donc pas de clubs sponsorisés n'ayant jamais payé")
    st.caption("Churn : le club a payé au moins une fois sur SportEasy et est maintenant en Free Plan ou Free Trial Plan")

st.divider()
st.header('2. Typology of teams by country today')

st.subheader(':green[a. Type Plan, Group Type, Gender, Device]')
# trellis teams
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=SJrNx&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)

st.subheader(':green[b. Sport]')
# sport pie chart
components.iframe( "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=qAZaPTn&theme=horizon&opt=ctxmenu",
    height=400,
    width=1700)

st.subheader(':green[c. First Source]')
# first source pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=ssTyVB&theme=horizon&opt=ctxmenu",
    height=400,
    width=1700)

st.subheader(':green[d. Activation Analysis]')
# A2
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=MtxHs&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption("We can notice a global saisonnality everery year !")

st.divider()
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

st.subheader(':green[c. # Teams in clubs]')
# teams in clubs pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=MdyY&theme=horizon&opt=ctxmenu",
    height=400,
    width=1700)

st.subheader(':green[c. Clubs Region]')
# map of the clubs
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=CJLgCDy&theme=horizon&opt=ctxmenu",
    height=600,
    width=2000)

st.divider()
st.header('4. Churn Analysis')
st.caption('by country from 01/01/2019 to today')


