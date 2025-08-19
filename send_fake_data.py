import requests
import random
import time

while True:
    voltage = round(random.uniform(210, 240), 2)
    current = round(random.uniform(4.0, 6.0), 2)
    power = round(voltage * current, 2)

    payload = {
        'voltage': voltage,
        'current': current,
        'power': power
    }

    try:
        response = requests.post('http://127.0.0.1:8000/add-reading/', json=payload)
        if response.status_code == 200:
            print(f"✅ Sent: {payload}")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
    except Exception as e:
        print("⚠️ Failed to send data:", e)

    time.sleep(10)
