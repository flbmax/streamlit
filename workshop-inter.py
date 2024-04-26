import streamlit as st


def embed_qlik_iframe(iframe_url):
    st.components.v1.iframe(iframe_url, height=600, width=900)

qlik_profiles = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=mzCzqu&theme=horizon&opt=ctxmenu"
qlik_teams = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu"

qlik_standalone_button = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=EECcxS&theme=horizon&opt=ctxmenu,currsel"
qlik_premium_button = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=bJpyXM&theme=horizon&opt=ctxmenu,currsel"
qlik_club_button = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=XrdMB&theme=horizon&opt=ctxmenu,currsel"


st.components.v1.iframe(qlik_profiles, height=100, width=100)
st.components.v1.iframe(qlik_teams, height=100, width=100)
st.components.v1.iframe(qlik_pane, height=100, width=100)

embed_qlik_iframe(qlik_profiles)
embed_qlik_iframe(qlik_teams)



