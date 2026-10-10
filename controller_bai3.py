import json
import paho.mqtt.client as mqtt

MQTT_HOST = "localhost"
MQTT_PORT = 1883

DEVICE_ID = "light01"
MQTT_SUB = "iot/lab/light01/status"
MQTT_PUB = "iot/lab/light01/cmd"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Da ket noi voi MQTT")
        client.subscribe(MQTT_SUB)
        print(f"Subscribed: {MQTT_SUB}")
    else:
        print(f"Loi ket noi MQTT: {reason_code}")


def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())

        print("\nTrang thai nhan duoc:")
        print(json.dumps(payload, ensure_ascii=False))

    except json.JSONDecodeError:
        print("INVALID JSON:", msg.payload.decode())


def send_command(client, cmd):
    payload = {
        "device_id": DEVICE_ID,
        "cmd": cmd
    }

    client.publish(
        MQTT_PUB,
        json.dumps(payload),
        qos=1
    )

    print(f"Da gui lenh {cmd} toi {DEVICE_ID}")


def start_controller():
    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2
    )

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_HOST, MQTT_PORT, 60)
    client.loop_start()

    try:
        while True:
            cmd = input("\nNhap lenh (ON/OFF/EXIT): ").strip().upper()

            if cmd == "EXIT":
                break

            if cmd not in ["ON", "OFF"]:
                print("Lenh khong hop le!")
                continue

            send_command(client, cmd)

    except KeyboardInterrupt:
        print("\nDang thoat...")

    finally:
        client.disconnect()
        client.loop_stop()


if __name__ == "__main__":
    start_controller()