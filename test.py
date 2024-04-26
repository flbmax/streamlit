import streamlit as st

st.text('Fixed text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

def embed_qlik_iframe(iframe_url):
    # Afficher l'iFrame dans l'application Streamlit
    st.components.v1.iframe(iframe_url, height=600)

# Lien iFrame de votre graphique Qlik Sense
qlik_iframe_url = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu,currsel&select=%2310%20-%20Members%2"

# Appeler la fonction pour intégrer l'iFrame dans l'application Streamlit
embed_qlik_iframe(qlik_iframe_url)
