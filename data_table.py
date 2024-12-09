import streamlit as st
import pandas as pd
import numpy as np
import time

# Function to simulate real-time data updates
def generate_data():
    """Generate or update a random data table."""
    data = {
        "Timestamp": [pd.Timestamp.now() for _ in range(5)],
        "Category": np.random.choice(["Josiah", "Adeagbo", "Access"], size=5),
        "Value": np.random.randint(10, 100, size=5),
    }
    return pd.DataFrame(data)

# Streamlit app
st.title("Real-Time Data Analysis Table")
st.write("This table updates dynamically in real-time!")

# Initialize empty dataframe
data_placeholder = st.empty()

# Real-time loop
while True:
    # Generate updated data
    df = generate_data()
    
    # Display the table
    data_placeholder.write(df)
    
    # Simulate a 2-second delay for real-time effect
    time.sleep(2)
