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
    <div style="display: block; height: 35vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- Number of teams created in ES has been impacted by ads done in 2022 that have boosted creation (but not activation). Except NL, half of the teams are Club Team.
                <p>- Clear opportinity to sell Premium version to NL. Club Product has been hampered by competition like Sportlink or Allunited. Warning : this does not apply to Belgium clubs where SE Club has a huge potential.
                <p>- Essentially male teams
                <p>- High number of teams created on mobile in ES and IT. Is the device has an impact on activation ? Not much
                <p>- Focus on NL:
                <p>* High Premium rates in NL compared to other countries (even France) but much smaller rate of club teams : <b>market of premium opportunities ?</b>
                <br>* 9500 members in Premium NL vs 4600 members in Club NL
                <br>* 76% yearly plan -> web !
                <br>* 80% club team & 80% football
                <p>- Teams live less time in ES or PT. Same for Premium lifetime. NL teams have better stability
                </p>
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

st.markdown(
    """
    <div style="display: block; height: 35vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- In ES and IT, rugby is key in club sales development but it does not reflect here.
                </p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

st.subheader(':green[c. First Source]')
# first source pie chart
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=ssTyVB&theme=horizon&opt=ctxmenu",
        height=700,
        width=1000)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")

st.markdown(
    """
    <div style="display: block; height: 35vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- Need to better track this metrics
                </p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

st.subheader(':green[d. Activation Analysis]')
# A2
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=MtxHs&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption("We can notice a global saisonnality every year !")
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the team owner)**")

st.markdown(
    """
    <div style="display: block; height: 35vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- First week of a team lifetime is crucial to go A2, but we spot teams with late activation
                <p>- Follow up must be intense and very clear, mostly the first days of teams lifetime. If the coach loses interest or patience, it will be hard to get him back later.
                </p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

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

st.markdown(
    """
    <div style="display: block; height: 35vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- 'analyse_stats' : hypothesis that some coaches download SE having in mind a "Football Manager" like
                </p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

st.divider()
