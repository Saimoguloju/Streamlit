import streamlit as st

# Set the title of the app
st.title("Welcome to my first example")

# Get user input 
name = st.text_input("Enter your name:")
age = st.number_input("Enter yout age:",min_value=0,max_value=120)

# Display the greeting and calculated output when the "Submit" button is clicked
if st.button("Submit"):
    st.write(f"Hello, {name}!")
    st.write(f"You are {age} years old, which is approximately {age*12} months.")
    
# Display a footer or additional information 
st.write("Thank you for using my GitHub!")