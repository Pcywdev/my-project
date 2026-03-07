import streamlit as st
import pandas as pd
st.header("Load Uber Dataset")

#cache so we don't re-read the file every rerun
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df
    
DATA_PATH = 'ncr_ride_bookings_with_coordinates.csv'

try:
    #load the data using the function
    uber_df = load_data(DATA_PATH)
except FileNotFoundError:
    st.error(f"Could not find {DATA_PATH}. Please check the filename.")
    st.stop()

st.success("Data loaded successfully!")
st.dataframe(uber_df.head())

if "Ride Distance" in uber_df.columns:
    #get the min and max ride ditance for the slider range
    min_dist = float(uber_df["Ride Distance"].min())
    max_dist = float(uber_df["Ride Distance"].max())
    
    #Create a slider to select a ride ditance range
    ride_range = st.slider(
        "Select ride distance range (miles)",
        min_value = min_dist,
        max_value = max_dist,
        value = (min_dist, max_dist),
    )
    low, high = ride_range
    
    filtered_df = uber_df[
        (uber_df["Ride Distance"] >= low) & (uber_df["Ride Distance"] <= high)
    ]
    st.dataframe(filtered_df.head())
else:
    st.warning("The dataset does not contain a 'Ride Distance'")
'''    
if "Driver Ratings" in uber_df.columns:
    #get the min and max ride ditance for the slider range
    min_rating = float(uber_df["Driver Ratings"].min())
    max_rating = float(uber_df["Driver Ratings"].max())
    
    #Create a slider to select a ride ditance range
    rating_range = st.slider(
        "Select ride driver rating ",
        min_value = min_rating,
        max_value = max_rating,
        value = (min_rating, max_rating),
    )
    low, high = rating_range
    
    filtered_df = uber_df[
        (uber_df["Ride Distance"] >= low) & (uber_df["Ride Distance"] <= high)
    ]
    st.dataframe(filtered_df.head())
else:
    st.warning("The dataset does not contain a 'Ride Distance'")
'''
st.header("Choose Vehicle Type")
col_name = "Vehicle Type"

if col_name in uber_df.columns:
    # Get unique, non-null Vehicle Types
    vehicle_types = sorted(uber_df[col_name].dropna().unique().tolist())
    
    # Let user pick one or more vehicle types
    chosen_types = st.multiselect(
        "Vehicle Type(s):",
        options=vehicle_types,
        default=[]  # start with nothing selected
    )

    # Start from full dataframe
    subset = uber_df.copy()

    # If user selected at least one type, filter
    if chosen_types:
        subset = subset[subset[col_name].isin(chosen_types)]
    
    st.write("Matching rides:", len(subset))
    st.dataframe(subset.head())

else:
    st.info("This dataset does not contain a 'Vehicle Type' column.")