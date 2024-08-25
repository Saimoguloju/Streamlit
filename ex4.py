import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("Interactive Dashboard Example")

# Sidebar options
st.sidebar.header("User Input Features")
x = st.sidebar.slider("Select X value", 1, 100, 50)
y = st.sidebar.slider("Select Y value", 1, 100, 50)
plot_type = st.sidebar.selectbox("Choose plot type:", ["Line", "Bar"])

# Create a simple dataframe
data = pd.DataFrame({
    "X": np.arange(1, 101),
    "Y": np.random.randint(1, 100, 100)
})

# Update Y column based on selected values
data["Y"] = data["Y"] * (x / 10) + y

# Plot based on user selection
st.write(f"### {plot_type} Plot")
if plot_type == "Line":
    st.line_chart(data)
else:
    st.bar_chart(data)
