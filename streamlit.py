import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set Streamlit page configuration
st.set_page_config(page_title="Supermarket Sales Dashboard", layout="wide")

# Load the dataset
df = pd.read_csv("supermarket_sales.csv")

# Display dataset summary
st.header("Supermarket Sales Data Summary")
st.write(df.describe(include="all"))

# Check and display the count of null values
st.subheader("Null Values in Dataset")
st.write(df.isnull().sum())

# Clean the data by removing rows with null values
df_cleaned = df.dropna(axis=0)

# Re-check null values to confirm cleaning
st.subheader("Null Values After Cleaning")
st.write(df_cleaned.isnull().sum())

# Create a Plotly count plot for Payment by Gender
st.subheader("Count of Payment Types by Gender")
fig1 = px.histogram(df_cleaned, x="Payment", color="Gender", barmode="group",
                    title="Count of Payment Types by Gender")
st.plotly_chart(fig1)

# Create a Plotly count plot for Payment by Gender split by City
st.subheader("Count of Payment Types by Gender and City")
fig2 = px.histogram(df_cleaned, x="Payment", color="Gender", barmode="group",
                    facet_col="City", title="Count of Payment Types by Gender across Cities")
st.plotly_chart(fig2)

# Create a Plotly histogram for Ratings
st.subheader("Distribution of Ratings")
fig3 = go.Figure(data=[go.Histogram(x=df_cleaned['Rating'], nbinsx=20)])
fig3.update_layout(title_text="Distribution of Ratings", xaxis_title="Rating", yaxis_title="Count",
                   width=900, height=500)
st.plotly_chart(fig3)

# Additional Streamlit components (optional)
st.write("This dashboard provides interactive visualizations of supermarket sales data, including payment types by gender and city, and the distribution of customer ratings.")
