import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx' #Your API_KEY  in Website: https://www.weatherapi.com/
LOCATION = 'Hanoi'
url = f'http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={LOCATION}&days=7'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    dates = []
    temperatures = []
    for day in data['forecast']['forecastday']:
        date = datetime.strptime(day['date'], '%Y-%m-%d')
        temp = day['day']['avgtemp_c']
        dates.append(date)
        temperatures.append(temp)
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o')
    plt.title(f'Trung bình nhiệt độ hàng ngày tại {LOCATION}')
    plt.xlabel('Ngày')
    plt.ylabel('Nhiệt độ (°C)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()
else:
    print("ERROR")
