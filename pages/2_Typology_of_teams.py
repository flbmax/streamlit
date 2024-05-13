import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="workshop-international", page_icon='sporteasy_logo.png', layout="wide")

st.title(':flag-eu: :blue[Workshop International Team]')
st.markdown('2024-05-21')

st.header('2. Typology of teams by country today')

st.subheader(':green[a. Type Plan, Group Type, Gender, Device]')
# trellis teams
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=SJrNx&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)

st.subheader(':green[b. Sport]')
# sport pie chart
with st.container():
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=qAZaPTn&theme=horizon&opt=ctxmenu",
                height=500,
                width=1700)
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=XMCAHYr&theme=horizon&opt=ctxmenu",
                height=500,
                width=500)
        st.caption('BE = Flanders, only dutch speaking part')


st.subheader(':green[c. First Source]')
# first source pie chart
with st.container():
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=ssTyVB&theme=horizon&opt=ctxmenu",
                height=700,
                width=1000)
        components.iframe( "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=sPTEbw&theme=horizon&opt=ctxmenu",
                height=500,
                width=500)
        st.caption('BE = Flanders, only dutch speaking part')

st.subheader(':green[d. Activation Analysis]')
# A2
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=MtxHs&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption("We can notice a global saisonnality every year !")

st.subheader(':green[e. Teams Purposes Analysis]')
# purpose
with st.container():
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=jdXpj&theme=horizon&opt=ctxmenu",
                height=1000,
                width=3000)
        components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=NeAzEt&theme=horizon&opt=ctxmenu",
                height=500,
                width=1000)

st.write("Let's compare with France :")
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=UXJAjC&theme=horizon&opt=ctxmenu" ,
        height=500,
        width=1000)

st.divider()
