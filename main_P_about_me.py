from  main_functions import *
from link_button import link_button

def page_about_me():
    st.title('Hello world')
    st.image('https://media-exp1.licdn.com/dms/image/C4D03AQHca98gKL-n1A/profile-displayphoto-shrink_200_200/0/1528227098040?e=1655942400&v=beta&t=2Q5g4dNLGU_P5V51gia6F0Y0o_17YnM-CmOzT1L9hsM')
    st.subheader('About me')
    st.text('This set of dashboards was prepared to illustrate possibilities of this Streamlit.')

    linkedinLink = 'https://pl.linkedin.com/in/kamilskoczylas96'
    repoLink = 'https://github.com/emptynonsens/SteamLitResearch'
    link_button('LinkedIn', linkedinLink)
    link_button('GitHub', repoLink)
    #if st.sidebar.button('LinkedIn'):
    #    webbrowser.open_new_tab(linkedinLink)
        
    #if st.sidebar.button('GitHub'):
    #    webbrowser.open_new_tab(repoLink)

    st.text('This set of dashboards was prepared to ilustrate possibilities of this Streamlit.')
