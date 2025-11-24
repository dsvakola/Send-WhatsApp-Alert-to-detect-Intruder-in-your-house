'''
Tested ok project at Vidyasagar Academy
www.vsa.edu.in

'''

import urequests as requests
from machine import Pin
import time
import network

ssid = 'write wifi or hotspot your ssid here'
password = 'write its password here'
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
while not wlan.isconnected():
    print("Connecting to network...")
    time.sleep(1)
print('Network connected:', wlan.ifconfig())
buzzer = Pin(15, Pin.OUT)
irs = Pin(16, Pin.IN, Pin.PULL_UP)# remove Pin.PULL_UP if not necessary.
phone_number = 'write your cellphone number here with 91 at the beginning as country code of India'
message = '%F0%9F%9A%A8 *ALERT MESSAGE* %F0%9F%9A%A8 %0AIntruder detected in your house! %F0%9F%8F%A0 %F0%9F%94%94'
api_key = 'write your api key which you will get from Callmebot. Its just like WhatsApp'
# How to create your own API key? Read the details given in Readme.md file at the beginning.

def send_whatsapp_message():
    url = f'https://api.callmebot.com/whatsapp.php?phone={phone_number}&text={message.replace(" ", "+")}&apikey={api_key}'
    response = requests.get(url)
    print("Message sent on mobile number: ", phone_number, "successfully!")
while True:
    if irs.value() == 0:
        send_whatsapp_message()
        buzzer.on()
        time.sleep(2)
        buzzer.off()
        time.sleep(300)
    else:
        buzzer.off()