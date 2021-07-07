# importing necessary libraries
import dht
from machine import Pin
from time import sleep
import requests
import json
  
# defining constants
API_ENDPOINT = "https://backend-smart-chair.herokuapp.com/log/info" 
char_id = "1"
temp_hum_sensor = dht.DHT11(Pin(5))  
session_id = 0
count_time = 0

#getting data from sensors

while True:
  try:
        sleep(2)
        temp_hum_sensor.measure()
        dht_temp = temp_hum_sensor.temperature()
        dht_hum = temp_hum_sensor.humidity()
        print('Temperature: %3.1f C' %temp)
        print('Humidity: %3.1f %%' %hum)
        
        #handling sessions
        if hc04_presence = True:
                session_id += 1
                count_time = 0
        elif count_time < 20:
                count_time += 1
        else:
                session_id = 0
        
        # creating post request
        payload = { "id": session_id, "temp": dht_temp, "chairId": char_id, "presence": hc04_presence, "noise": 0, "lum": ldr_lum, "hum":dht_hum}
        
        # sending post request and saving response as response object
        r = requests.post(url = API_ENDPOINT, data = json.dumps(payload))

        
        
        
        # extracting response text 
        pastebin_url = r.text
        print("The pastebin URL is:%s"%pastebin_url)

        #handling error
        except OSError as e:
                print('Failed to read sensor.')
