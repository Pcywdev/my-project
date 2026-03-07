import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = "Module 2: Widgets, Forms, and Layout Basics"
    layout = "wide"
)

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

uber_df = load_data('ncr_ride_bookings_with_coordinates.csv')

st.sidebar.header("1. Instant Filters")
st.sidebar.write("These widgets trigger a rerun immediately.")

#Widget: Slider for Fare
min_dare = float(uber_df["Booking Value"].min())
max_dare = float(uber_df)
