# Libraries for the time and firebase
import pyrebase
import time

# This is the config for the connection to your Firebase database
config = {
  "apiKey": "HuGYMqFLKv2mUKcPnLoBR1r7KtADEAA5lsrK6aF3",
  "authDomain": "rpi-powerstatus.firebaseapp.com",
  "databaseURL": "https://rpi-powerstatus-default-rtdb.europe-west1.firebasedatabase.app/",
  "storageBucket": "rpi-powerstatus.appspot.com"
}

# This initializes the database
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# This prints on the console that it beggins to transimt data
print("Sending data to Firebase using the Raspberry PI")
print("—————————————---------------------------")
print()

# This program runs forever
while True:
  
    # This creates the previous time result
    localtime = time.localtime()
    result1 = time.strftime("%H:%M:%S", localtime)
    
    # This creates the now current time result
    time.sleep(5)
    localtime = time.localtime()
    result2 = time.strftime("%H:%M:%S", localtime)
    
    # This prints both times for debugging
    print("Previous Time :", result1)
    print("Current Time :", result2)

    # This creates a data package
    data = {
        "time1": result1,
        "time2": result2
    }
    
    # This sends the data to the database (it will update the previous values from there and won't create a new child)
    db.set(data)
    
