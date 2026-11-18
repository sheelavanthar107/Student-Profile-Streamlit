import streamlit as st
st.set_page_config(
    page_title="Student Profile Application",
    layout="centered"
)
st.markdown("""
<style>
.stApp {
    background-color: black;
    color: white;
}
.block-container {
    max-width: 850px;
    padding-top: 2rem;
}
.profile-card {
    background: #050505;
    border: 1px solid #292929;
    border-radius: 28px;
    padding: 30px;
}
.stButton > button {
    background: white;
    color: black;
    border-radius: 30px;
    padding: 10px 25px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("## Student Profile Application")
st.write("Developed by Harshitha")
st.info(
    "Fill in your details and click View My Profile."
)
with st.form("student_form"):
    name = st.text_input(
        "Student Name",
        placeholder="Enter your name"
    )
    usn = st.text_input(
        "Roll Number",
        placeholder="Enter roll number"
    )
    department = st.selectbox(
        "Department",
        ["CSE", "ISE", "ECE", "EEE",
         "ME", "CIVIL", "AIML", "Other"]
    )
    year = st.radio(
        "Current Year",
        ["1st Year", "2nd Year",
         "3rd Year", "4th Year"]
    )
    submit = st.form_submit_button(
        "View My Profile"
    )
if submit:
    if name.strip() == "" or usn.strip() == "":
        st.error("Please enter all details.")
    else:
        st.success("Profile Created Successfully!")
        st.subheader("Student Profile")
        st.write("**Student Name:**", name)
        st.write("Roll Number:", usn)
        st.write("**Department:**", department)
        st.write("**Current Year:**", year)
