import streamlit as st

# * optional kwarg unsafe_allow_html = True

def embed_qlik_iframe(iframe_url):
    # Afficher l'iFrame dans l'application Streamlit
    st.components.v1.iframe(iframe_url, height=600, width=900)

# Lien iFrame de votre graphique Qlik Sense
qlik_iframe_url = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=mzCzqu&theme=horizon&opt=ctxmenu"
# Appeler la fonction pour intégrer l'iFrame dans l'application Streamlit
embed_qlik_iframe(qlik_iframe_url)

