import streamlit as st

from src.screens.home_screen import home_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog

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
    st.set_page_config(
        page_title= 'SnapClass - AI Smart Attendance',
        page_icon= 'D:/Vinit Sarang/AI_ML_Batch/My Projects/page_icon.png'
    )

    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()
        case None:
            home_screen()

    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
main()