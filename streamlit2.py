import streamlit as st
import pandas as pd
import mysql.connector

# Create a connection to the MySQL database
db_connection = mysql.connector.connect(
    user='<insert user here>',
    password='<insert password here>',
    host='aws.connect.psdb.cloud',
    database='<insert database here>',
)

# Streamlit app header
st.title('Expected Crop Yield Visualization')

# List of crop names
crop_names = ["Corn", "Cotton", "Beans", "Barley", "Flaxseed"]

# Dropdown for selecting the crop
selected_crop_name = st.selectbox('Select a Crop', crop_names)

# Query to fetch data for the selected crop
query = f"SELECT Year, Yield FROM StreamlitData WHERE Crop = '{selected_crop_name}';"
data = pd.read_sql(query, con=db_connection)

# Display the data for the selected crop
st.write(f"Expected Yield for {selected_crop_name}")
st.write(data)

# Close the database connection
db_connection.close()
