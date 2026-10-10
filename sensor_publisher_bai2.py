import json
import time
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
SENSORS = ["sensor01", "sensor02"]

client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="publisher_bai2"
)
client.connect(BROKER, PORT, 60)
client.loop_start()
try:
    while True:
        for device in SENSORS:
            temperature = round(random.uniform(30, 40), 1) #giả lập dữ liệu cảm biến 
            humidity = round(random.uniform(30, 60), 1)
            data = {
                "device": device,
                "temperature": temperature,
                "humidity": humidity
            }
            topic = f"iot/lab/{device}/data"
            payload = json.dumps(data)
            client.publish(topic, payload)

            print(f"[PUBLISH] {device}")
            print(f"  Nhiet do : {temperature:.1f} C")
            print(f"  Do am    : {humidity:.1f} %")
            print(f"  Topic    : {topic}")
            print("-" * 40)
            time.sleep(2)

except KeyboardInterrupt:
    print("\nDa dung Publisher.")

finally:
    client.loop_stop()
    client.disconnect()