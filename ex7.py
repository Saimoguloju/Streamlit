import streamlit as st

# Define pages
def home():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

def about():
    st.title("About Page")
    st.write("This is the About Page.")

def contact():
    st.title("Contact Page")
    st.write("This is the Contact Page.")

# Sidebar for navigation
page = st.sidebar.selectbox("Navigate", ["Home", "About", "Contact"])

# Routing based on the selected page
if page == "Home":
    home()
elif page == "About":
    about()
elif page == "Contact":
    contact()
