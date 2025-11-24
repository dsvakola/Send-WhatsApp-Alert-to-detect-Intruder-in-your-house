"""
main.py
IR sensor -> WhatsApp alert (CallMeBot) + buzzer
Tested OK project at Vidyasagar Academy
www.vsa.edu.in

IMPORTANT: Do NOT hardcode secrets into a public repo.
Place real credentials into a local file (e.g. secrets.py) that is listed in .gitignore.
"""

import urequests as requests
from machine import Pin
import time
import network
import ubinascii
import ure

# ---------- CONFIG (edit before upload) ----------
ssid = 'YOUR_WIFI_SSID'
password = 'YOUR_WIFI_PASSWORD'

# Phone number format: country code + number (no + sign for the CallMeBot URL).
# For India example: phone_number = '919812345678'
phone_number = '91YOURPHONENUMBER'

# Message to send (plain text). MicroPython string only — URL encoding applied in send function.
message = '🚨 *ALERT MESSAGE* 🚨\nIntruder detected in your house! 🏠🔔'

# api_key from CallMeBot (you obtain it by messaging CallMeBot on WhatsApp — see README)
api_key = 'YOUR_CALLMEBOT_APIKEY'
# --------------------------------------------------

# Pins (adjust to your board)
buzzer = Pin(15, Pin.OUT)   # active HIGH buzzer pin
irs = Pin(16, Pin.IN, Pin.PULL_UP)  # IR sensor input (change pull mode if needed)

# Connect to WiFi
def connect_wifi(ssid, password, timeout=20):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(ssid, password)
        start = time.time()
        while not wlan.isconnected():
            if time.time() - start > timeout:
                raise RuntimeError('WiFi connection timeout')
            print('Connecting to WiFi...')
            time.sleep(1)
    print('Network connected, IP:', wlan.ifconfig()[0])
    return wlan

def url_encode(s):
    # Minimal url encoding: replace spaces and newlines; MicroPython has no urllib
    enc = s.replace(' ', '+')
    enc = enc.replace('\n', '%0A')
    # For safety, encode percent and plus already present
    enc = enc.replace('%', '%25')
    return enc

def send_whatsapp_message(phone, msg, apikey):
    encoded = url_encode(msg)
    url = 'https://api.callmebot.com/whatsapp.php?phone={}&text={}&apikey={}'.format(phone, encoded, apikey)
    try:
        r = requests.get(url)
        # For debugging: print status and first 200 chars of response
        print('Sent request to CallMeBot, status:', getattr(r, 'status_code', 'unknown'))
        try:
            print(r.text[:200])
        except:
            pass
        try:
            r.close()
        except:
            pass
    except Exception as e:
        print('Error sending message:', e)

# Main
def main():
    # connect WiFi
    try:
        connect_wifi(ssid, password)
    except Exception as e:
        print('WiFi error:', e)
        return

    cooldown = 300  # seconds between alerts to avoid spamming
    last_alert = 0

    while True:
        sensor_val = irs.value()
        # IR sensors typically read 0 when object detected; confirm with your sensor
        if sensor_val == 0:
            now = time.time()
            if now - last_alert > cooldown:
                print('Obstacle detected! Sending alert...')
                send_whatsapp_message(phone_number, message, api_key)
                buzzer.on()
                time.sleep(2)
                buzzer.off()
                last_alert = now
            else:
                print('Obstacle detected but in cooldown period.')
            # short delay to debounce/read again
            time.sleep(0.2)
        else:
            buzzer.off()
            time.sleep(0.1)

if __name__ == '__main__':
    main()