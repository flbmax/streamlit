import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="worksop-international", layout="wide")

st.title('Workshop International Team')
st.markdown('2024-05-21')

st.header('1. Growth in number of users, teams & clubs')
st.caption('by country from 01/01/2019 to today')

st.subheader('a. Users')
# profiles created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=mzCzqu&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('*using profile.default_language to determine the country')


col1, col2 = st.columns(2, gap='medium')
with col1:
    st.subheader('b. Teams')
    # teams created
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu",
            height=500,
            width=700)
    st.caption('*using team.country_id to determine the country')
with col2:
    st.subheader('c. Clubs')
    # clubs created
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=juSbKpp&theme=horizon&opt=ctxmenu",
            height=500,
            width=700)
    st.caption("Client : au moins un paiement autorisé ou en chargeback sur SportEasy - donc pas de clubs sponsorisés n'ayant jamais payé")
    st.caption("Churn : le club a payé au moins une fois sur SportEasy et est maintenant en Free Plan ou Free Trial Plan")

st.header('2. Typology of teams by country today')

col3, col4 = st.columns(2)
with col3:
    st.subheader('a. Type Plan, Group Type, Gender, Device')
    # trellis teams
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=SJrNx&theme=horizon&opt=ctxmenu",
            height=500,
            width=700)
with col4:
    st.write("sport pie chart here")

st.subheader('b. Activation Analysis')
# A2
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=MtxHs&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)