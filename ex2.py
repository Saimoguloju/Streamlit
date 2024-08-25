import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Values': [10, 20, 15, 30, 25, 35]
}
df = pd.DataFrame(data)

st.title("Interactive Data Filtering and Plotting")

# Sidebar for filtering
category = st.sidebar.selectbox("Select Category:", df['Category'].unique())

# Filter data based on the selection
filtered_data = df[df['Category'] == category]

# Display filtered data
st.write("### Filtered Data")
st.write(filtered_data)

# Plot the filtered data
st.write("### Bar Chart")
fig, ax = plt.subplots()
ax.bar(filtered_data['Category'], filtered_data['Values'])
st.pyplot(fig)
