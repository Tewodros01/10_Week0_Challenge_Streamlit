import streamlit as st
import pandas as pd
import numpy as np
import utils  # Import the updated utility functions from utils.py

st.title("Data Visualization Dashboard")
st.markdown("This dashboard allows you to visualize data with various interactive features.")

# Load and clean data
data = pd.read_csv("benin-malanville.csv")  # Update with your data source
data = utils.clean_data(data)

# Sidebar for interactive plot type selection
st.sidebar.header("Customize the Dashboard")
plot_type = st.sidebar.selectbox("Select Plot Type", ["Line Plot", "Scatter Plot", "Box Plot", "Histogram"])

# Interactive plot settings
x_column = st.sidebar.selectbox("X-Axis", data.columns)
y_column = st.sidebar.selectbox("Y-Axis", data.columns)

# Render the appropriate plot based on the selection
if plot_type == "Line Plot":
    utils.generate_line_plot(data, x_column, y_column, "Line Plot")

elif plot_type == "Scatter Plot":
    hue_column = st.sidebar.selectbox("Hue", ["None"] + list(data.columns))
    hue = None if hue_column == "None" else hue_column
    utils.generate_scatter_plot(data, x_column, y_column, "Scatter Plot", hue=hue)

elif plot_type == "Box Plot":
    utils.generate_box_plot(data, x_column, "Box Plot")

elif plot_type == "Histogram":
    utils.generate_histogram(data, x_column, "Histogram")

# Summary statistics
st.header("Summary Statistics")
st.write(utils.get_summary_stats(data))
