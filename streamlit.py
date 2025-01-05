import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the App
st.title("Getting Started with Streamlit")

# Introduction
st.header("What is Streamlit?")
st.write("""
Streamlit is a Python library that makes it easy to build interactive, data-driven web applications for data science, machine learning, and other Python-based projects. 
You can turn your Python scripts into fully functional web apps with minimal effort.
""")

# Key Features of Streamlit
st.header("Why Use Streamlit?")
st.write("""
Streamlit provides several key features that make it unique:
1. **Simplicity**: Build apps with just Python. No need for HTML, CSS, or JavaScript.
2. **Interactivity**: Add sliders, buttons, text inputs, and other UI elements easily.
3. **Data Visualization**: Integrate seamlessly with libraries like Matplotlib, Plotly, and Altair.
4. **Deployment**: Share your apps with others easily using Streamlit Community Cloud or other deployment methods.
""")

# Code Example
st.header("How Simple is Streamlit?")
st.code("""
import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")
""", language="python")
st.write("With just a few lines of code, you can create a web app!")

# Interactive Widgets
st.header("Explore Streamlit Widgets")
st.write("Let's explore some basic widgets:")

# Text Input
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! 👋")

# Slider
age = st.slider("Select your age:", 0, 100, 25)
st.write(f"You selected: {age} years old.")

# Checkbox
agree = st.checkbox("Do you like Streamlit?")
if agree:
    st.write("That's awesome! 🎉")

# Radio Buttons
experience = st.radio(
    "How would you rate your experience with Streamlit?",
    ["Beginner", "Intermediate", "Advanced"]
)
st.write(f"You selected: {experience}")

# Data Visualization
st.header("Data Visualization with Streamlit")
st.write("Here's an example of displaying a simple chart:")

# Example Data
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=["Feature 1", "Feature 2", "Feature 3"]
)

# Line Chart
st.line_chart(data)

# Matplotlib Plot
st.subheader("Using Matplotlib")
fig, ax = plt.subplots()
ax.hist(data["Feature 1"], bins=15, alpha=0.7)
st.pyplot(fig)

# File Upload
st.header("Working with Files")
st.write("You can upload files and work with them in Streamlit.")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Here's the uploaded data:")
    st.dataframe(df)

# Sidebar Example
st.sidebar.header("Sidebar Example")
st.sidebar.write("This is a sidebar. Use it for navigation or displaying additional information.")
sidebar_option = st.sidebar.radio(
    "Choose a feature to explore:",
    ["Introduction", "Widgets", "Data Visualization", "File Upload"]
)
st.sidebar.write(f"You selected: {sidebar_option}")

# Summary
st.header("Summary")
st.write("""
Streamlit is a powerful, yet simple tool for creating web apps in Python. 
With its intuitive API and focus on interactivity, it's a great choice for beginners and professionals alike.
""")

# Resources
st.write("Want to learn more? Check out these resources:")
st.markdown("- [Streamlit Documentation](https://docs.streamlit.io)")
st.markdown("- [Streamlit GitHub Repository](https://github.com/streamlit/streamlit)")
st.markdown("- [Streamlit Community](https://discuss.streamlit.io)")

st.write("Happy coding! 🎉")
