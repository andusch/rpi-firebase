import pyrebase
import time

config = {
  "apiKey": "HuGYMqFLKv2mUKcPnLoBR1r7KtADEAA5lsrK6aF3",
  "authDomain": "rpi-powerstatus.firebaseapp.com",
  "databaseURL": "https://rpi-powerstatus-default-rtdb.europe-west1.firebasedatabase.app/",
  "storageBucket": "rpi-powerstatus.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

print("Send Data to Firebase Using Raspberry Pi")
print("—————————————---------------------------")
print()

while True:
    
    localtime = time.localtime()
    result1 = time.strftime("%H:%M:%S", localtime)
    time.sleep(5)
    localtime = time.localtime()
    result2 = time.strftime("%H:%M:%S", localtime)
    print("Previous Time :", result1)
    print("Current Time :", result2)

    data = {
        "time1": result1,
        "time2": result2
    }

    db.set(data)
    
