# importing necessary libraries
import dht
from machine import Pin
from time import sleep
#import requests
#import json
from hcLib import HCSR04
from ldrLib import LDR

# defining constants and initial values
API_ENDPOINT = "https://backend-smart-chair.herokuapp.com/log/info"
chair_id = "1"
sensor = dht.DHT11(Pin(5))
presence_sensor = HCSR04(trigger_pin=13, echo_pin=12, echo_timeout_us=1000000)
ldr_sensor = LDR(34)
session_id = 0
count_time = 0
hc04_presence = False

# getting data from sensors
while True:
    try:
        sleep(2)

    # getting temperature and humidity
        sensor.measure()
        dht_temp = sensor.temperature()
        dht_hum = sensor.humidity()

    # getting presence
        if presence_sensor.distance_cm() < 10:
            hc04_presence = True
        else:
            hc04_presence = False

    # getting luminosity
        ldr_lum = ldr_sensor.value()

    # handling sessions
        if hc04_presence == True:
            session_id += 1
            count_time = 0
        elif count_time < 20:
            count_time += 1
        else:
            session_id = 0

        print('Temperature: %3.1f C' % dht_temp)
        print('Humidity: %3.1f %%' % dht_hum)
        print('Distance: %3.1f cm' % presence_sensor.distance_cm())
        if hc04_presence == True:
            print('Presente')
        else:
            print('Not Presente')
        print('Luiz: %3.1f' % ldr_lum)
        print(session_id)
        print(count_time)

    # creating post request
        payload = { "id": session_id, "temp": dht_temp, "chairId": chair_id, "presence": hc04_presence, "noise": 0, "lum": ldr_lum, "hum": dht_hum}
    
        print (payload)
    # sending post request and saving response as response object
    # r = requests.post(url = API_ENDPOINT, data = json.dumps(payload))

    # extracting response text
    # pastebin_url = r.text
    # print("The pastebin URL is:%s"%pastebin_url)

    # handling error
    except OSError as e:
        print('Failed to read sensors.')