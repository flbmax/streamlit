import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="workshop-international", page_icon='sporteasy_logo.png', layout="wide")

st.title(':flag-eu: :blue[Workshop International Team]')
st.markdown('2024-05-21')

st.header('1. Growth in number of profiles, teams & clubs')
st.caption('by country from 01/01/2019 to today')

st.subheader(':green[a. Profiles]')
# profiles created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=mzCzqu&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('*using profile.default_language to determine the country')

st.subheader(':green[b. MAU]')
# MAU
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=mzCzqu&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('*using profile.default_language to determine the country')

col1, col2 = st.columns(2, gap='large')
with col1:
    st.subheader(':green[c. Teams]')
    # teams created
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu",
            height=500,
            width=650)
    st.caption('*using team.country_id to determine the country')
with col2:
    st.subheader(':green[d. Clubs]')
    # clubs created
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=juSbKpp&theme=horizon&opt=ctxmenu",
            height=500,
            width=650)
multi = '''Client : at least one authorised payment or in chargeback status - hence no sponsored clubs that have never paid
Churn : the club has paid at least once in SportEasy and is now under a Free Plan or Free Trial Plan
'''
st.caption(multi)

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
st.caption("We can notice a global saisonnality every year !")

st.subheader(':green[e. Teams Purposes Analysis]')
# purpose
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=jdXpj&theme=horizon&opt=ctxmenu",
        height=1000,
        width=3000)

st.write("Let's compare with France :")
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=UXJAjC&theme=horizon&opt=ctxmenu" ,
        height=500,
        width=1000)

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

st.divider()
st.header('4. Churn Analysis')
st.caption('by country from 01/01/2019 to today')


st.divider()
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

st.subheader(':green[c. Churn Analysis]')
# churn the last 5 years
col3, col4 = st.columns(2, gap='small')
with col3:
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=LHhEnK&theme=horizon&opt=ctxmenu",
            height=500,
            width=100)
with col4:
    components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=GQmHumj&theme=horizon&opt=ctxmenu&select=KPI%20AM::club.country_id,ES,GB,IT,NL,PT",
            height=500,
            width=1000)


def open_link_in_new_tab(url):
    js = f"window.open('{url}');"
    st.write(f'<script>{js}</script>', unsafe_allow_html=True)


# Création de la barre latérale (sidebar)
st.sidebar.title("Executive Summary")

# Ajout des liens cliquables dans la barre latérale
if st.sidebar.button("1. Growth in number of profiles, teams & clubs"):
    # Lien redirigeant vers une URL externe
    st.link_button('google',"https://www.google.com")


# Fonction JavaScript pour déclencher le défilement vers une section spécifique
def scroll_to_section(section_id):
    js = f"document.getElementById('{section_id}').scrollIntoView();"
    st.write(f'<script>{js}</script>', unsafe_allow_html=True)

# Bouton pour déclencher le défilement vers la Section 1
if st.sidebar.button("Aller à la Section 1"):
    scroll_to_section("section1")