import schedule
import time 

def send_weather_update():
    # Add the longitude and latitude for your city i will be using Nairobi
    latitude = -1.286389
    longitude = 36.817223

    weather_data = get_weather(latitude, longitude)

def main():
    schedule.every().day.at("08.00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep(1)
def get_weather(latitude, longitude):
    base url