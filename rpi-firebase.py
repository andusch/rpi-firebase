import pyrebase
import time

# Use your Firebase details to send data to your database
config = {
  "apiKey": "...",
  "authDomain": "...",
  "databaseURL": "...",
  "storageBucket": "..."
}

# This initializez the database
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Code for debugging
print("Send Data to Firebase Using Raspberry Pi")
print("—————————————-")
print()

while True:
    
    # It saves the current time in your location
    localtime = time.localtime()
    result = time.strftime("%H:%M:%S", localtime)

    # Code fot debugging
    print("Current Time :", result)

    # This creates the data package to send it to your database
    data = {
        "Current Time": result
    }

    # It pushes the data onto the database
    db.push(data)

    # It sleeps for 5 seconds
    time.sleep(5)
