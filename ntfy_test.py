# SPDX-FileCopyrightText: © 2023 Peter Tacon <contacto@petertacon.com>
#
# SPDX-License-Identifier: MIT

""" Requests Test """

# Import OS libraries
import os
import rtc
import time
import ssl
import board
import microcontroller
from digitalio import DigitalInOut, Direction

#Import Network libraries
import ipaddress
import wifi
import adafruit_requests
import socketpool

"""Creating objects for required libraries"""
#  Onboard LED setup
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
led.value = False

# Connect to network
print()
print("Connecting to WiFi")

#  connect to your SSID
try:
    wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID2'), os.getenv('CIRCUITPY_WIFI_PASSWORD2'))
except:
    wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connected to WiFi")
pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

#Arrays and strings in JSON format, required to send the message to ntfy.sh
headers = {
	"title": "ALERTA: PRUEBA SAN",
	"tags": "warning,shield"
}

data = "This is a test, please do not attend this message"
url = "https://ntfy.sh/skyred_test"

#specific variables for timing and pinging
ping_address = ipaddress.ip_address("1.1.1.1")
clock = time.monotonic()

while True:
    try:
        # Every 30 secs make a Ping, to certify it's connected
        if (clock + 30) < time.monotonic():
            if wifi.radio.ping(ping_address) is None:
                print("lost connection")
            else:
                print("connected")
            clock = time.monotonic()
        else:
			# Attempt to send message, then awaits for response and delays
			# for 60 seconds
            print("Sending Message to %s" % url)
            response = requests.post(url, data=data, headers=headers)
            print("-" * 40)
            print(response.text)
            response.close()
            time.sleep(60)
    except Exception as e:
        print(e)
        continue

