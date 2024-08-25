import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Train a simple model
clf = RandomForestClassifier()
clf.fit(X, y)

st.title("Iris Flower Species Prediction")

# Sidebar for user input features
st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider("Sepal Length", float(X[:, 0].min()), float(X[:, 0].max()), float(X[:, 0].mean()))
sepal_width = st.sidebar.slider("Sepal Width", float(X[:, 1].min()), float(X[:, 1].max()), float(X[:, 1].mean()))
petal_length = st.sidebar.slider("Petal Length", float(X[:, 2].min()), float(X[:, 2].max()), float(X[:, 2].mean()))
petal_width = st.sidebar.slider("Petal Width", float(X[:, 3].min()), float(X[:, 3].max()), float(X[:, 3].mean()))

# Predict the species
input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction = clf.predict(input_features)
predicted_species = iris.target_names[prediction][0]

# Display the prediction
st.write(f"### Predicted Species: **{predicted_species}**")
