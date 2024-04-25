import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st  # To display plots in Stream# Function to clean data
def clean_data(data):
    data = data.replace([np.inf, -np.inf], np.nan)

    # Coerce invalid timestamps to NaN and handle them accordingly
    if 'Timestamp' in data.columns:
        data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')
        most_common_date = (
            data['Timestamp'].mode()[0] if not data['Timestamp'].mode().empty else pd.Timestamp.now()
        )
        data['Timestamp'] = data['Timestamp'].fillna(most_common_date)
        data.set_index('Timestamp', drop=False, inplace=True)

    # Impute missing values in numeric columns with the median
    numeric_columns = data.select_dtypes(include=[np.number]).columns
    data[numeric_columns] = data[numeric_columns].apply(lambda x: x.fillna(x.median()))

    data.drop_duplicates(inplace=True)

    return data

def get_summary_stats(data):
    return data.describe()

# Function to generate a line plot with explicit figure creation
def generate_line_plot(data, x, y, title):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=data, x=x, y=y, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    st.pyplot(fig)


# Function to generate a scatter plot with explicit figure creation
def generate_scatter_plot(data, x, y, title, hue=None):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(data=data, x=x, y=y, hue=hue, ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    st.pyplot(fig)


# Function to generate a box plot with explicit figure creation
def generate_box_plot(data, column, title):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=data, x=column, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)


# Function to generate a histogram with explicit figure creation
def generate_histogram(data, column, title):
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.histplot(data[column], kde=True, ax=ax)
    ax.set_title(title)
    ax.set_xlabel("Value")
    ax.set_ylabel("Count")
    st.pyplot(fig)
