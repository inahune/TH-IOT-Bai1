import json
import paho.mqtt.client as mqtt

MQTT_HOST = "localhost"
MQTT_PORT = 1883

DEVICE_ID = "light01"
MQTT_SUB = "iot/lab/light01/cmd"
MQTT_PUB = "iot/lab/light01/status"

light_status = "OFF"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Da ket noi voi MQTT")
        client.subscribe(MQTT_SUB)
        print(f"Subscribed: {MQTT_SUB}")
    else:
        print(f"Loi ket noi MQTT: {reason_code}")


def on_message(client, userdata, msg):
    global light_status

    try:
        payload = json.loads(msg.payload.decode())

        print("====== Nhan duoc lenh ======")
        print("Topic:", msg.topic)
        print("Data:", payload)

        cmd = payload.get("cmd")
        device_id = payload.get("device_id")

        if device_id != DEVICE_ID:
            print("Sai device_id")
            return

        if cmd not in ["ON", "OFF"]:
            print("Lenh khong hop le:", cmd)
            return

        # Cap nhat trang thai den
        light_status = cmd

        status_payload = {
            "device_id": DEVICE_ID,
            "status": light_status
        }

        client.publish(
            MQTT_PUB,
            json.dumps(status_payload),
            qos=1
        )

        print("Da gui trang thai:", status_payload)

    except json.JSONDecodeError:
        print("INVALID JSON:", msg.payload.decode())


def start_device():
    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2
    )

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_forever()


if __name__ == "__main__":
    start_device()