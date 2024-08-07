import requests
import streamlit as st
import streamlit.components.v1 as components
import sys
# api key = 867a0216a489131cfa37409ca09cfc2e
custom_html = """
<div class="banner">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTN2jjYufn5KY4HF_-p7PnDGDu0x6h7siQ3a_utKvqk&s" alt="Banner Image">
</div>
<style>
    .banner {
        width: 100%;
        height: 250px;
        overflow: hidden;
    }
    .banner img {
        width: 98%;
        object-fit: cover;
    }
</style>
"""

components.iframe("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTN2jjYufn5KY4HF_-p7PnDGDu0x6h7siQ3a_utKvqk&s", height=150)
## Headers
st.title("Fun, detailed Weather App!")
st.header(":violet[The end of clunky weather apps with the fun and easy to use weather app!]")
st.subheader(":blue[Made by: Rayhaan Khan]")
## for the documentation
url = "https://countrycode.org/"
st.write("For finding country codes visit: [🔘](%s)" % url)

## Creating checkbox

g = st.checkbox("Visibility 👀")
h = st.checkbox("Location coordinates 🌎 🗼 ")
u = st.checkbox("Forecast")
i = st.checkbox("Wind Speed 💨")

##Main function - gets the input of the location

def main():
    z = st.text_input("Enter the location of the place")
    yuoi = st.info("Please enter Country Code for places which are in multiple areas, Eg: Cambridge, US")

    city()
    make_url(z)
    export




def city():
    z = st.text_input("enter the location (more detail)(optional): ")
    return z

# Making the URL for the openweather API to use.

def make_url(z):
    ip = f'http://api.openweathermap.org/data/2.5/weather?q={z}&appid=867a0216a489131cfa37409ca09cfc2e'
    zt = f'https://api.openweathermap.org/data/2.5/forecast?q={z}&appid=867a0216a489131cfa37409ca09cfc2e'
    response = requests.get(ip) #Requests library
    meow = requests.get(zt) # Requests library - gets the URL specified's info 
    
    if response.status_code == 200:
                #current
                data = response.json() # conversion to json
                temp = data['main']['temp'] # finding the desired stuff
                temp = temp -273
                temp = round(temp)
                desc = data['weather'][0]['description']
                vis = data['visibility']
                coord = data['coord']
                humid = data['main']['humidity']
                wind = data['wind']
                if i:
                     st.text(f'Wind speed is: {wind} 💨')
                st.text(f'Temperature: ~{temp} °C 🌡️')
                st.text(f"Humidy is: {humid}% 🏝️")

                st.text("The web address for the data: " + ip)
                #forecast
                #blah = meow.json()
                #forecast_temp = blah['2024-05-01 12:00:00']['temp']
                #forecast_temp = forecast_temp -273
                #forecast_temp = round(forecast_temp)
                #if u:
                   # st.text(f"The expected average temperature for the next 40 days: {forecast_temp}")#


                #Emoji thingie

                if desc == 'clear sky':
                     st.markdown(f':green[**Description: {desc} 🌤️**]')
                if desc == 'mist':
                     st.markdown(f':green[**Description: {desc} 🌫️**]')
                if desc == 'smoke':
                     st.markdown(f':green[**Description: {desc} 😶‍🌫️**]')
                if desc == 'broken clouds':
                     st.markdown(f":green[**Description: {desc} 🌥️**]")
                if desc == 'scattered clouds':
                     st.markdown(f':green[**Description: {desc} ⛈️**]')
                if desc == 'light rain':
                     st.markdown(f':green[**Description: {desc} 🌧️**]')
                if desc == 'overcast clouds':
                     st.markdown(f':green[**Description: {desc} ⛈️**]')
                else:
                     st.markdown(f':green[**Description: {desc}**]')

                #check box things
                if g:
                    st.text(f' 👀 Visibility is ~{vis} metres')
                if h:
                    st.text(f" 🌎 The co-ordinates of the weather station are: {coord}. Search them up to see the location of monitoring systems!")
    else:
        st.error("Error fetching data- maybe you were too specific?") # error displayed

def export():
      st.text(make_url)

main()
