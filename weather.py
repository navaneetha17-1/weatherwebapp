# weather_web.py
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

API_KEY = "ab9ff0826221ff2fb065bfb24bed463d"  # Replace with your OpenWeatherMap API key

# Page config
st.set_page_config(page_title="Weather App 🌤️", page_icon="🌦️", layout="centered")

# Background style (optional)
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to bottom, #87CEEB, #00BFFF);
        color: #333333;
        font-family: 'Helvetica', sans-serif;
    }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #104E8B;
    }
    </style>
    """, unsafe_allow_html=True
)

# App title
st.title("🌤️ Weather App")

# User input
city = st.text_input("Enter city name:")

if st.button("Get Weather"):
    if not city:
        st.warning("Please enter a city name")
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()

        if response.get("cod") != 200:
            st.error(f"City not found: {city}")
        else:
            weather = response['weather'][0]['description'].title()
            temp = response['main']['temp']
            humidity = response['main']['humidity']
            icon_code = response['weather'][0]['icon']

            # Display results in a card-like container
            st.markdown(f"""
            <div style="background-color: white; padding: 20px; border-radius: 15px; text-align: center;">
                <h2>{city.title()}</h2>
                <p style="font-size:18px;">Weather: {weather}</p>
                <p style="font-size:18px;">Temperature: {temp}°C</p>
                <p style="font-size:18px;">Humidity: {humidity}%</p>
            </div>
            """, unsafe_allow_html=True)

            # Fetch and display weather icon
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            img = Image.open(BytesIO(requests.get(icon_url).content))
            st.image(img, width=120)




