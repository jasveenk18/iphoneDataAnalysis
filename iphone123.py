import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
def load_data():
    file_path = "apple_products.csv"
    return pd.read_csv(file_path)

df = load_data()

# Streamlit UI
st.title("Apple Products Dataset Analysis")
st.write("## Dataset Overview")
st.write(df.head())

# Summary Statistics
st.write("## Summary Statistics")
st.write(df.describe())

# Price Distribution
st.write("## Price Distribution")
fig, ax = plt.subplots()
sns.histplot(df['Sale Price'], bins=20, kde=True, ax=ax)
st.pyplot(fig)

# Discount vs Star Rating
st.write("## Discount vs Star Rating")
fig, ax = plt.subplots()
sns.scatterplot(x=df['Discount Percentage'], y=df['Star Rating'], ax=ax)
st.pyplot(fig)

# Top 5 Most Rated Products
st.write("## Top 5 Most Rated Products")
top_rated = df.nlargest(5, 'Number Of Ratings')[['Product Name', 'Number Of Ratings']]
st.write(top_rated)

# Top 5 Most Reviewed Products
st.write("## Top 5 Most Reviewed Products")
top_reviewed = df.nlargest(5, 'Number Of Reviews')[['Product Name', 'Number Of Reviews']]
st.write(top_reviewed)

# RAM Distribution
st.write("## RAM Distribution")
fig, ax = plt.subplots()
sns.countplot(y=df['Ram'], ax=ax)
st.pyplot(fig)