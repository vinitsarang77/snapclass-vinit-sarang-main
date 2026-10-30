import streamlit as st
from src.database.dp import create_subject

@st.dialog("Create New Subject")
def create_subject_dialog(teacher_id):
    # FIXED: Changed clear_on_submit to False so your typed data is preserved if validation fails
    with st.form("create_subject_form", clear_on_submit=False):
        st.write("Enter the details of the new subject below:")
        
        sub_id = st.text_input("Subject Code", placeholder="CS101").strip()
        sub_name = st.text_input("Subject Name", placeholder="Introduction to Computer Science").strip()
        sub_section = st.text_input("Section", placeholder="A").strip()
        
        # primary form submission element
        submit_btn = st.form_submit_button("Create Subject Now", type='primary', use_container_width=True)
        
        if submit_btn:
            # Validate input contents smoothly *only after* clicking the submit trigger
            if not sub_id or not sub_name or not sub_section:
                st.warning("Please fill all the fields before submitting.")
            else:
                try:
                    create_subject(sub_id, sub_name, sub_section, teacher_id)
                    st.toast("🎉 Subject Created Successfully!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {str(e)}")
