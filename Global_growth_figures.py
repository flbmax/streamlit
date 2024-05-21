import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

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

txt = st.text_area(
    "Remarks :",
    "- International teams follow the French YoY trend but can't get on track like in  France and activate less their profiles\n"
    "- Global reduce in amplitude for all. Warning for March 24 amplitude compared to March 23 for International team\n"
    "- Harold hypothesis is thant non-validated profiles come from teams owners letting their teams inactive (80% of inactive team in INT) because they did not figure out the SportEasy purpose. They create a team and disapear right after without ever reconnect again"
    ,
    height=4000)

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
    <div style="display: compact; flex-direction: column; justify-content: center; height: 20vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 30px;">
                <p>- Seasonnality is exactly the same
                <br>- International MAU goes from 100k -> 130k -> 150k i.e. +30% -> +15%
                <br>- Where France MAU goes from 400k -> 550k -> 720k i.e. +38% -> +31%
                <br>- International MAU growth <b>should be more stable</b></p>
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
    <div style="display: compact; flex-direction: column; justify-content: center; height: 20vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 30px;">
            <p>- International teams follow the French trend (-22% vs -25% for FR) but their activation rate rise a bit (France drops proportionnaly to the team creation rates)
            <br>- The trends are the same for all countries
            <br>- Check https://sporteasy-bi.eu.qlikcloud.com/sense/app/fe30758a-8efe-48e4-943d-367693619486/sheet/bb3354f0-125b-4a8c-966e-3e2eb2c3088f/state/analysis/hubUrl/%2Fcatalog%3Fquick_search_filter%3Dteam</p>
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
    <div style="display: compact; flex-direction: column; justify-content: center; height: 20vh;">
        <div style="background-color:rgb(237, 240, 243); padding: 20px; border-radius: 30px;">
            <p>- Spread of the seasonnality (lot of July 2022)</p>
        </div>
    </div>""",
    unsafe_allow_html=True
)

st.divider()




