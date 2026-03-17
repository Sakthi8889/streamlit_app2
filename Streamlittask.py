import streamlit as st

# Title
st.title("Student Information Form")


app_name = "Student App"



st.write(f"App Name: {app_name}")
st.write(f"Version: {version}")


with st.form("student_form"):
    
    
    name = st.text_input("Enter your Name")
    gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])
    age = st.number_input("Enter Age", min_value=1, max_value=100, step=1)
    college = st.text_input("Enter your College Name")
    
    
    submit = st.form_submit_button("Submit")


if submit:
    st.success("Form Submitted Successfully!")

    
    st.write("### Entered Details:")
    st.write(f"Name: {name}")
    st.write(f"Gender: {gender}")
    st.write(f"Age: {age}")
    st.write(f"College: {college}")

    
    if age >= 18:
        st.write("Status: Adult")
    else:
        st.write("Status: Minor")