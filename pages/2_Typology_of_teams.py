import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="workshop-international", page_icon='sporteasy_logo.png', layout="wide")

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

st.header('2. Typology of teams by country today')

st.subheader(':green[a. Type Plan, Group Type, Gender, Device]')
# trellis teams
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=SJrNx&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")
st.markdown(
    """
    <div style="display: compact; flex-direction: column; justify-content: center; height: 20vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 30px;">
            <p>- High Premium rates in NL compared to other countries (event France) but much smaller rate of club : <b>market of premium opportunities ?</b>
            <br>- The trends are the same for all countries
            <br>- A seasonnality exists in team creation but does not follow in profiles creation i.e. coachs create their team but does not invite players : <b>onboarding issue</b>.</p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

st.subheader(':green[b. Sport]')
# sport pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=qAZaPTn&theme=horizon&opt=ctxmenu",
        height=500,
         width=1700)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")


st.subheader(':green[c. First Source]')
# first source pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=ssTyVB&theme=horizon&opt=ctxmenu",
        height=700,
        width=1000)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")

st.subheader(':green[d. Activation Analysis]')
# A2
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=MtxHs&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption("We can notice a global saisonnality every year !")
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")

st.subheader(':green[e. Teams Purposes Analysis]')
# purpose
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=jdXpj&theme=horizon&opt=ctxmenu",
        height=1000,
        width=3000)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")

st.write("Let's compare with France :")
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=UXJAjC&theme=horizon&opt=ctxmenu" ,
        height=500,
        width=1000)

st.divider()
