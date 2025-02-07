import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

gif_html = """
    <img src="https://media.giphy.com/media/26gR0BwpqHjsUu6YY/giphy.gif" width="400">
    """
st.components.v1.html(gif_html, height=300)

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

st.header('1. Growth in number of profiles, teams & clubs')
st.caption('by country from 01/01/2019 to today')

st.subheader(':green[a. Profiles]')
# profiles created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=Lhvbszb&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('*using profile.default_language to determine the country : "es","en","it","nl","pt"')


st.markdown(
    """
    <div style="display: block; height: 35vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- International teams follow the French YoY trend <b>but can't get on track</b> like in  France and <b>activate less their profiles</b>
                <br>- Global reduce in amplitude for all. <b>Warning for March 24</b> amplitude compared to March 23 for International team
                <br>- Harold hypothesis is that non-validated profiles come from teams owners letting their teams inactive (80% of inactive team in INT) because they did not figure out the SportEasy purpose. They create a team and disapear right after without ever reconnect again
                <br>- Maxence hypothesis is that it comes from club member (players & parents) and not team owners
                <br>- Need to conntinue the work of translation, streghten the marketing messages (presentation and revival) and the <b>onboarding</b> to immprove validation rates
                <br>- NL and PT are below in profiles creation <b>BUT</b> NL has the best validation rate with IT</p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

st.write('**France Analysis**')
df_profiles_france = pd.DataFrame()
df_profiles_france['Months'] = ['dec.', 'jan.','feb.','mar.','apr.']
df_profiles_france['YoY'] = ['+ 13,6%', '- 15,5%','- 9,9%','- 11,7 %','+ 17,6%']
df_profiles_france['amplitude % previous month 2023'] = ['', '+ 56,8%','- 25,9%','+ 7,4 %','- 37,2%']
df_profiles_france['amplitude % previous month 2024'] = ['', '+ 16,7%','- 21,1%','+ 5,4 %','- 16,3%']
st.table(df_profiles_france)

st.write('**International Analysis**')
df_profiles_int = pd.DataFrame()
df_profiles_int['Months'] = ['dec.', 'jan.','feb.','mar.','apr.']
df_profiles_int['YoY'] = ['+ 20,0%', '- 4,6%','- 1,7%','- 20,7 %','- 8,9%']
df_profiles_int['amplitude % previous month 2023'] = ['', '+ 79,7%','- 18,4%','+ 12,5 %','- 26,4%']
df_profiles_int['amplitude % previous month 2024'] = ['', '+ 42,9%','- 13,0%','- 12,3 %','- 15,4%']
st.table(df_profiles_int)

st.subheader(':green[b. MAU]')
# MAU
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=bb985210-f17b-480a-abf5-40a9654b8576&obj=ACpgM&theme=horizon&opt=ctxmenu",
        height=500,
        width=1100)
st.caption('*using profile.default_language to determine the country : "es","en","it","nl","pt" starting from **01/01/2022**')


st.markdown(
    """
    <div style="display: block; height: 25vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- Seasonnality is exactly the same; MAU growth is too low in international
                <br>- International MAU goes from 100k -> 130k -> 150k i.e. +30% -> +15%
                <br>- Where France MAU goes from 400k -> 550k -> 720k i.e. +38% -> +31%
                <br>- Teams creation and profiles creation are disparate : our new teams are scattered in Europe (and in the world), we do not create (or less) clusters empowering word-to-mouth (which provides the best activation source in France). The new users come from diverse sources and activate less (not agree)</p>
        </div>
    </div>""",
    unsafe_allow_html=True
)


st.subheader(':green[c. Teams]')
# teams created
components.iframe("https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu",
        height=500,
        width=1000)
st.caption('*using team.country_id to determine the country')
st.caption('**NL = Netherlands + Flanders (ie, "nl" as the default language of the team owner)**')

st.markdown(
    """
    <div style="display: block; height: 60vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- Check https://sporteasy-bi.eu.qlikcloud.com/sense/app/fe30758a-8efe-48e4-943d-367693619486/sheet/bb3354f0-125b-4a8c-966e-3e2eb2c3088f/state/analysis/hubUrl/%2Fcatalog%3Fquick_search_filter%3Dteam
                <p>- Still a <b>huge problem</b> of international teams activation despite some updgrades on onboarding: void modes, carousels, path of teams creation ...)
                <p>- Why teams do not even go A1 ?
                <p>- Do users understand the use of SE ?
                <p>- Are they qualify ? Is this what they were looking for ?
                <p>- Don't they dare involve their members ?
                <p>-  Club Teams do activate better than others ? Yes a bit but the huge difference is for A2
                <p><b>Note:</b> A study conducted by Ana and Harold in 2022 for Spain (calling a dozens of inactive created teams) showed that users created teams were well-qualified (they were coaches) but they did not get the purpose of SE</p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

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

st.markdown(
    """
    <div style="display: block; height: 25vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 20px;">
                <p>- Number of new clubs increase in countries where ressources are put. Need to have fulltime sales to improve acquisition. Starting from scratch before beginning. We expect to pass the 100-customer mark in the near future for ES, IT and the UK. For instance, in ES, we were down to a dozen customer clubs by 2022 (4k€ of turnover) and we are now at 78 clients clubs (31k€ of turnover). But <b>we are not moving fast enough</b> compare to the international competition
                <p>- Now, the biggest challenge is to keep clients. AM is essential for the future, let's see churn figures later.</p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

st.divider()




