import schedule
import time 

def send_weather_update():
    # Add the longitude and latitude for your city i will be using Nairobi
    latitude = -1.286389
    longitude = 36.817223



    weather_data = get_weather(latitude, longitude)
    temperature_celsius = weather_data["hourly"]["temperature_2m"][0]
    relativehumidity = weather_data["hourly"]["relativehumidity"][0]
    wind_speed = weather_data["hourly"]["windspeed_10m"][0]
    temperature_farenheit = celsius_to_farenheit()

def main():
    schedule.every().day.at("08.00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)
def get_weather(latitude, longitude):
    base_url = f"https://api.open-meteo.com/v2/forecast?latitude"
    response = requests.get(base_url)
    data =response.json
    return data