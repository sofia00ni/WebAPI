import streamlit as st
import requests
import pandas as pd

# Title and description
st.title("People in Space")
st.markdown("""
This app displays real-time information about how many people 
are currently in space, along with their names.
""")

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    count = data["number"]
    people = data["people"]

    st.subheader(f"Total number of people in space: {count}")

    st.markdown("###Names of the astronauts:")
    for person in people:
        st.write(f"- {person['name']}")
else:
    st.error("Failed to retrieve data from the API.")


st.header("Current Location of the International Space Station")

iss_url = "http://api.open-notify.org/iss-now.json"
iss_response = requests.get(iss_url)

if iss_response.status_code == 200:
    iss_data = iss_response.json()
    latitude = float(iss_data["iss_position"]["latitude"])
    longitude = float(iss_data["iss_position"]["longitude"])

    # Description
    st.markdown("""
    The map below shows the real-time location of the ISS as it orbits Earth.
    """)

    df = pd.DataFrame([[latitude, longitude]], columns=["lat", "lon"])
    st.map(df)

    st.write(f"**Latitude:** {latitude}, **Longitude:** {longitude}")

else:
    st.error("Failed to retrieve ISS location.")
