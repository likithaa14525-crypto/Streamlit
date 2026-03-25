import streamlit as st
st.title("User Registration Form")
with st.form("my_form"):
    col1, col2 = st.columns(2)
    
    name1 = col1.text_input("First Name")
    name2 = col2.text_input("Last Name")
    
    email = st.text_input("Enter your email")
    address = st.text_area("Enter your address")  
    
    password = st.text_input("Enter password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")
    
    submit = st.form_submit_button("Submit")

if submit:
    if password != confirm_password:
        st.error("Passwords do not match!")
    else:
        st.write("First Name:", name1)
        st.write("Last Name:", name2)
        st.write("Email:", email)
        st.write("Address:", address)  
        st.write("Submitted successfully!")