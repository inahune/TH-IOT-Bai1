import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/lab/+/data"

def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("Da ket noi MQTT Broker!")
        client.subscribe(TOPIC)
    else:
        print("Ket noi MQTT Broker that bai!")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))

        device = data["device"]
        temperature = float(data["temperature"])
        humidity = float(data["humidity"])
        print(f"Device: {device}")
        print(f"Temperature: {temperature:.1f} C")
        print(f"Humidity: {humidity:.1f} %")

        if temperature > 35:
            print("CANH BAO: Nhiet do cao")
        if humidity < 40:
            print("CANH BAO: Do am thap")

        print() 

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as e:
        print(f"Loi xu ly du lieu: {e}")


client = mqtt.Client(
    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    client_id="monitor_subscriber_bai2"
)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.loop_forever()