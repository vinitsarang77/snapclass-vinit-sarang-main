import streamlit as st
import segno
import io
# from src.database.dp import create_subject

# @st.dialog("Create New Subject")
# def create_subject_dialog(teacher_id):
#     # FIXED: Changed clear_on_submit to False so your typed data is preserved if validation fails
#     with st.form("create_subject_form", clear_on_submit=False):
#         st.write("Enter the details of the new subject below:")
        
#         sub_id = st.text_input("Subject Code", placeholder="CS101").strip()
#         sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science").strip()
#         sub_section = st.text_input("Section", placeholder="A").strip()
        
#         # primary form submission element
#         submit_btn = st.form_submit_button("Create Subject Now", type='primary', use_container_width=True)
        
#         if submit_btn:
#             # Validate input contents smoothly *only after* clicking the submit trigger
#             if not sub_id or not sub_name or not sub_section:
#                 st.warning("Please fill all the fields before submitting.")
#             else:
#                 try:
#                     create_subject(sub_id, sub_name, sub_section, teacher_id)
#                     st.toast("🎉 Subject Created Successfully!")
#                     st.rerun()
#                 except Exception as e:
#                     st.error(f"Error: {str(e)}")

@st.dialog("Share Class Link")
def share_subject_dialog(subject_name, subject_code):
    app_domain = "snapclass-main.streamlit.app"
    join_url = f"{app_domain}/?join-code={subject_code}"

    st.header("Scan to join")

    qr = segno.make(join_url)
    out = io.BytesIO()

    qr.save(out, kind='png', scale=10, border=1)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('### Copy Link')
        st.code(join_url, language="text")
        st.code(subject_code, language="text")
        st.info('Copy this link to share on whatapp or Email')

    with col2:
        st.markdown('### Scan to Join')
        st.image(out.getvalue(), caption='QRCODE for class joining')
