import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# Connect to the MySQL database
conn = mysql.connector.connect(
    user='<insert user here>',
    password='<insert password here>',
    host='aws.connect.psdb.cloud',
    database='<insert database here>',
)

cursor = conn.cursor()

# Streamlit app
st.title("Crop Market Price Data")

# Query data for the selected crop from the database
selected_crop = st.selectbox("Select a Crop", ["Corn", "Barley", "Flaxseed", "Beans", "Cotton"])

query = f"SELECT Year, Price FROM StreamlitData WHERE Crop = '{selected_crop}'"
cursor.execute(query)
data = cursor.fetchall()

# Create a DataFrame
df = pd.DataFrame(data, columns=['Year', 'Price'])

# Create a line chart
st.write(f"Market Price Data for {selected_crop}")
fig, ax = plt.subplots()
ax.plot(df['Year'], df['Price'])
ax.set_xlabel('Year')
ax.set_ylabel('Market Price')

# Remove the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
