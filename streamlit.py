import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
data = pd.read_csv('supermarket_sales.csv')

# Sidebar for selecting the column to plot
column_to_plot = st.sidebar.selectbox('Select a column to plot:', data.columns)

# Create a Seaborn count plot
plt.figure(figsize=(10, 6))
sns.countplot(x=column_to_plot, data=data)

# Show the plot in Streamlit
st.pyplot(plt)