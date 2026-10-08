import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen

def main():
#     st.header("This is title")
#     name = st.text_input('Enter your name')

#     col1, col2 = st.columns(2, gap='small')

#     with col1:
#         if st.button('Display my Name', type='primary', key='btn1', width='stretch'):
#             st.write('hi', name)
#     with col2:
#         st.button('Display my Name', type='secondary', key='btn2', width='content')

#     st.markdown("""
        
# """, unsafe_allow_html=True)

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()
main()