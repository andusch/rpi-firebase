# The libraries needed for the application
import pyrebase
import time
import Adafruit_DHT as dht
import RPi.GPIO as GPIO

# Enter your Firebase db details here
config = {
  "apiKey": "...",
  "authDomain": "...",
  "databaseURL":"...",
  "storageBucket": "...",
}

# Sets the pin
GPIO.setmode(GPIO.BCM)
DHT11_pin = 23

# Initializing the Firebase database
firebase = pyrebase.initialize_app(config)
db = firebase.database()

print("Sening data to Firebase Using Raspberry Pi")
print("—————————————---------------------------")
print()

while True:
    
    # This reads the data from the DHT11 sensor
    humi, temp = dht.read_retry(dht.DHT11, DHT11_pin)
    humi = '{0:0.1f}' .format(humi)
    temp = '{0:0.1f}' .format(temp)
    
    # Creating the data package that will be sent to Firebase
    data = {
    'temperature' : temp,
    'humidity' : humi
    }
    
    # Printing data to console to debug
    print("Temperature: " + temp + " °C")
    print("Humidity: " + humi + " RH")

    # This sends the data to the db
    db.set(data)

    # This will sleep for 5 seconds
    time.sleep(5)
    
