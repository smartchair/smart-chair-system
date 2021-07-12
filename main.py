# importing necessary libraries
import dht
from machine import Pin
from time import sleep
import urequests
import ujson
from hcLib import HCSR04
from ldrLib import LDR
import network

# defining constants and initial values
API_ENDPOINT = "https://backend-smart-chair.herokuapp.com/log/info"
chair_id = "ID dispositivo"
sensor = dht.DHT11(Pin(5))
presence_sensor = HCSR04(trigger_pin=27, echo_pin=26, echo_timeout_us=1000000)
ldr_sensor = LDR(34)
hc04_presence = False
sta_if = network.WLAN(network.STA_IF)
led = Pin(2, Pin.OUT)

# getting data from sensors
while True:
    try:
    #check if internet is connected
        led.value(not sta_if.isconnected())
        
    #resting    
        sleep(10)

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

        print('Temperature: %3.1f C' % dht_temp)
        print('Humidity: %3.1f %%' % dht_hum)
        print('Distance: %3.1f cm' % presence_sensor.distance_cm())
        if hc04_presence == True:
            print('Presente')
        else:
            print('Not Presente')
        print('Luiz: %3.1f' % ldr_lum)

    # creating post request
        payload = { "temp": dht_temp, "chairId": chair_id, "presence": hc04_presence, "noise": 0, "lum": ldr_lum, "hum": dht_hum}
        api_data = ujson.dumps(payload)
        
    # sending post request and saving response as response object
        r = urequests.post(API_ENDPOINT, data = api_data)

    # extracting response text
        pastebin_url = r.text
        print("The pastebin URL is:%s"%pastebin_url)

    # handling error
    except OSError as e:
        print('Failed to read sensors.')