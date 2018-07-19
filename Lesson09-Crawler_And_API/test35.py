import requests
import json

url = 'https://www.metaweather.com/api/location/2306179/'
response = requests.get(url)
data=json.loads(response.text)
a=data['consolidated_weather'][0]['applicable_date']
b=data['consolidated_weather'][0]['weather_state_name']
print('今天'+a+'的天氣是'+b)
#print(type(data))
#print(data)
