import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st  # To display plots in Streamlit

# Function to clean data
def clean_data(data):
    # Handle infinite values by converting them to NaN
    data = data.replace([np.inf, -np.inf], np.nan)

    # Coerce invalid timestamps to NaN, then fill NaN with a common date or a specific strategy
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')
        most_common_date = data['Timestamp'].mode()[0] if not data['Timestamp'].mode().empty else pd.Timestamp.now()
        data['Timestamp'] = data['Timestamp'].fillna(most_common_date)
        data.set_index('Timestamp', drop=False, inplace=True)

    # Impute missing values in numeric columns with the median
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    data[numeric_columns] = data[numeric_columns].apply(lambda x: x.fillna(x.median()))

    # Remove duplicates in the entire dataset or a specific subset
    data.drop_duplicates(inplace=True)

    return data

# Function to calculate summary statistics
def get_summary_stats(data):
    return data.describe()

# Function to calculate the correlation matrix
def get_correlation_matrix(data):
    return data.corr()

# Function to generate line plots
def generate_line_plot(data, columns, title):
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data[columns])
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Value")
    st.pyplot()  # Display in Streamlit

# Function to generate box plots
def generate_box_plot(data, columns, title):
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data[columns])
    plt.title(title)
    st.pyplot()

# Function to generate histograms
def generate_histogram(data, column, title):
    plt.figure(figsize=(12, 6))
    sns.histplot(data[column], kde=True)
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Count")
    st.pyplot()

# Function to generate scatter plots
def generate_scatter_plot(data, x, y, title, hue=None):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=data, x=x, y=y, hue=hue, palette='viridis')
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    st.pyplot()
