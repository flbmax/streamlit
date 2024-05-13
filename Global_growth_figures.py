import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Workshop International", page_icon='sporteasy_logo.png', layout="wide")


st.title(':flag-eu: :blue[Workshop International Team]')
st.markdown('2024-05-21')

st.header('1. Growth in number of profiles, teams & clubs')
st.caption('by country from 01/01/2019 to today')

st.subheader(':green[a. Profiles]')
# profiles created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=mzCzqu&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('*using profile.default_language to determine the country : "es","en","it","nl","pt"')

st.subheader(':green[b. MAU]')
# MAU
#components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=mzCzqu&theme=horizon&opt=ctxmenu",
#        height=500,
#        width=1000)
#st.caption('*using profile.default_language to determine the country : "es","en","it","nl","pt"')


st.subheader(':green[c. Teams]')
# teams created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('*using team.country_id to determine the country')
st.caption('**NL = Netherlands + Flanders (ie, "nl" as the default language of the team owner)**')

st.subheader(':green[d. Clubs]')
# clubs created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=juSbKpp&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption("**NL = Netherlands + Flanders (ie, 'nl' as the default language of the club owner)**")
multi = '''
Client : at least one authorised payment or in chargeback status - hence no sponsored clubs that have never paid

Churn : the club has paid at least once in SportEasy and is now under a Free Plan or Free Trial Plan
'''
st.write(multi)
st.divider()



