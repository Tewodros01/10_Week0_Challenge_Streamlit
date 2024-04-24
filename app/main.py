import streamlit as st
import pandas as pd
import numpy as np
from utils import clean_data, get_summary_stats, get_correlation_matrix, generate_line_plot, generate_box_plot, generate_histogram, generate_scatter_plot

# Load Data with Error Handling
@st.cache_data
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        data = clean_data(data)  # Clean the data
        return data
    except FileNotFoundError:
        st.error(f"File not found: {file_path}. Please check the path and try again.")
        return pd.DataFrame()  # Return an empty DataFrame on error

# Main App
st.title("Solar Radiation Dashboard")
st.write("Interactive dashboard for visualizing solar radiation data.")

# Sidebar for user input
st.sidebar.header("User Input")
file_path = st.sidebar.text_input("Enter the path to the data file", "benin-malanville.csv")

# Load the data based on user input
data = load_data(file_path)

if not data.empty:
    # Summary statistics
    st.subheader("Summary Statistics")
    summary_stats = get_summary_stats(data)
    st.write(summary_stats)

    # Correlation matrix
    st.subheader("Correlation Matrix")
    correlation_matrix = get_correlation_matrix(data)
    st.write(correlation_matrix)

    # Time-series plots
    st.subheader("Time-Series Analysis")
    variables = st.multiselect("Select variables to plot", data.columns, default=['GHI', 'DNI', 'DHI', 'Tamb'])
    generate_line_plot(data, variables, "Time-Series Trends")

    # Scatter plots
    st.subheader("Scatter Plots")
    x_axis = st.selectbox("Select X-Axis", data.columns, index=1)
    y_axis = st.selectbox("Select Y-Axis", data.columns, index=2)
    generate_scatter_plot(data, x_axis, y_axis, "Scatter Plot")

    # Box plots
    st.subheader("Box Plots")
    boxplot_columns = st.multiselect("Select variables for box plot", data.columns, default=['GHI', 'DNI', 'DHI'])
    generate_box_plot(data, boxplot_columns, "Box Plot")

    # Histogram
    st.subheader("Histograms")
    histogram_column = st.selectbox("Select column for histogram", data.columns, index=3)
    generate_histogram(data, histogram_column, "Histogram")

else:
    st.warning("Data could not be loaded or is empty. Please check the file path and try again.")
