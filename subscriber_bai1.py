import json
from datetime import datetime
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/lab/message"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Da ket noi MQTT Broker thanh cong.")
        client.subscribe(MQTT_TOPIC)
        print(f"Dang lang nghe topic: {MQTT_TOPIC}")
    else:
        print(f"Ket noi that bai: {reason_code}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    receive_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n========== THONG DIEP NHAN DUOC ==========")
    print("Thoi gian:", receive_time)
    print("Topic:", msg.topic)
    print("Thong diep:", payload)
    print("=" * 42)

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="subscriber-bai1"
)
client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
    client.loop_forever()
except KeyboardInterrupt:
    print("\nDa dung Subscriber.")
except Exception as e:
    print(f"Loi: {e}")
finally:
    client.disconnect()
