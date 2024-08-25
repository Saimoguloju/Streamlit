import streamlit as st
import time
import numpy as np

st.title("Real-Time Data Dashboard")

# Simulate real-time data
placeholder = st.empty()

# Update data every second
for i in range(100):
    new_data = np.random.randn(1, 1)
    placeholder.metric("Real-Time Value", f"{new_data[0, 0]:.2f}")
    time.sleep(1)
