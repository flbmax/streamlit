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
qlik_iframe_url = "URL_de_votre_iframe"

# Appeler la fonction pour intégrer l'iFrame dans l'application Streamlit
embed_qlik_iframe(qlik_iframe_url)
