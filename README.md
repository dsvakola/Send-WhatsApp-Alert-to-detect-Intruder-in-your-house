# 🔔 IR-Sensor → WhatsApp Alert (CallMeBot)  
**Tested OK — Project at Vidyasagar Academy**  
![Vidyasagar Academy banner](banner.png)
![Platform: Raspberry Pi Pico W](https://img.shields.io/badge/Platform-RPi%20Pico%20W-brightgreen.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.txt) [![Platform: ESP32/ESP8266](https://img.shields.io/badge/Platform-ESP32%2FESP8266-green.svg)](#) [![Language: MicroPython](https://img.shields.io/badge/Language-MicroPython-orange.svg)](#)

## Project overview
A simple MicroPython script for ESP32/ESP8266 (NodeMCU)/ **Raspberry Pi Pico W** that sends a WhatsApp text alert (via CallMeBot) and sounds a buzzer when an IR sensor detects an intruder/obstacle.

**Contents**
- `main.py` — MicroPython script (ready to upload)
- `README.md` — this file
- `readme.txt` — plain text summary
- `changelog.txt` — release notes
- `LICENSE.txt` — MIT license
- `.gitignore`
- `assets/banner.png` —

---

## Quick start (for students)
1. Clone the repo to your machine.
2. Edit `main.py` and replace placeholders:
   - `ssid`, `password`
   - `phone_number` (include country code, e.g. `91XXXXXXXXXX` for India)
   - `api_key` (see **How to get API key (CallMeBot)** below)
3. Upload `main.py` to your RPi Pico W using Thonny / ampy / rshell / WebREPL.
4. Add `assets/wiring-diagram.png` (we will upload this PNG to the repo root `assets/` folder).
5. Power the board and observe. When IR detects an obstacle, the buzzer will sound and a WhatsApp message will be sent.

> **Important security note:** Do **not** commit your real Wi-Fi password or `api_key` to a public repository. Use environment config or a local `secrets.py` ignored by git. See `.gitignore` included.

---

## How the WhatsApp part works
This project uses the free CallMeBot WhatsApp API: a single HTTP GET request (to `https://api.callmebot.com/whatsapp.php?...`) sends a text message to your own WhatsApp number using an API key the bot issues to your number after you send it an activation message from your phone. See CallMeBot docs for details. :contentReference[oaicite:0]{index=0}

---

## How to get a CallMeBot API key (step-by-step)
1. **Add the CallMeBot WhatsApp number to your phone contacts.**  
   The number published on CallMeBot pages is currently **+34 694 29 84 96** (Spain). Add it as a contact (e.g., `CallMeBot`). *CallMeBot phone numbers have changed historically; if that number does not respond, check the CallMeBot homepage or blog for the latest number.* :contentReference[oaicite:1]{index=1}

2. **Open WhatsApp and send this exact message** to that contact from the phone number that will receive the alerts:

### Wait for the bot to reply.
3. **Wait for the bot reply.** The bot will message back something like:
'xxxxxx' in six digit form. That `XXXXXX` is your `apikey`. If you don't receive the ApiKey within 2 minutes, try again later (the site notes sometimes delay / try after 24 h). :contentReference[oaicite:2]{index=2}

4. **Use the apikey** in the URL format:
Example: replace `<phone>` with `91XXXXXXXXXX` (include country code without `+`) and URL-encode message text. :contentReference[oaicite:3]{index=3}

---

## Wiring diagram
Check the wiring diagram for construction of the project.

---

## License
This project is released under the **MIT License**. See `LICENSE.txt`.

---

## Support & references
- CallMeBot official site: https://www.callmebot.com/ (instructions and API docs). :contentReference[oaicite:4]{index=4}
- Example blog/tutorial (ESP32 + CallMeBot): Random Nerd Tutorials — double-check the CallMeBot number they recommend, as it sometimes changes. :contentReference[oaicite:5]{index=5}





