import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout, style_background_home
from src.components.footer import footer_home

def home_screen():

    header_home()

    style_base_layout()
    style_background_home()
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Student")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKBfcsWTnD61WVpHYdHW_gx6iKni7AyyNXoP7bmdmFVA&s=10", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
            st.session_state['login_type'] = 'student'
            st.rerun()
    with col2:
        st.header("I'm Teacher")
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSCQQoGif3zlyzpr9LzMTY0Y5CFNxYEH6vWdeB2A3GHfQ&s=10", width=130)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right'):
                st.session_state['login_type'] = 'teacher'
                st.rerun()

    footer_home()


            