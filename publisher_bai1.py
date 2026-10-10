import json
import time
import paho.mqtt.client as mqtt

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "iot/lab/message"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Da ket noi MQTT Broker thanh cong.")
    else:
        print(f"Ket noi that bai: {reason_code}")

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2,
    client_id="publisher-bai1"
)
client.on_connect = on_connect

try:
    client.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
    client.loop_start()
    time.sleep(1)

    message = "Xin chao tu client Python MQTT"
    msv = "B23DCCN618"
    ho_ten = "Cao Thi Thanh Nhan"

    payload = f"{message} - {msv} - {ho_ten}"

    info = client.publish(MQTT_TOPIC, payload, qos=0)
    info.wait_for_publish()

    print(f"Topic: {MQTT_TOPIC}")
    print(f"Da gui thong diep: {payload}")

except KeyboardInterrupt:
    print("\nDa dung Publisher.")
except Exception as e:
    print(f"Loi: {e}")
finally:
    client.loop_stop()
    client.disconnect()
