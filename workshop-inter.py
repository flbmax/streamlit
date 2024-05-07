import streamlit as st

# Functions
def wide_space_default():
st.set_page_config(layout=“wide”)

wide_space_default()

def embed_qlik_iframe(iframe_url):
    st.components.v1.iframe(iframe_url, height=600, width=900)
# Functions

st.title('Workshop International Team')
st.markdown('2024-05-21')



#qlik_profiles = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=dfbf997f-84e2-4ef7-90c5-9a809d81bfc5&obj=mzCzqu&theme=horizon&opt=ctxmenu"
#qlik_teams = "https://sporteasy-bi.eu.qlikcloud.com/single/?appid=fe30758a-8efe-48e4-943d-367693619486&obj=kxPqHuT&theme=horizon&opt=ctxmenu"


"""
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
"""


#embed_qlik_iframe(qlik_profiles)
#embed_qlik_iframe(qlik_teams)



