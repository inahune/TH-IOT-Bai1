README - CHƯƠNG TRÌNH MQTT BÀI 2

1. Broker sử dụng
- MQTT Broker: Mosquitto 2.1.2
- Địa chỉ: localhost
- Cổng: 1883

2. Cách chạy chương trình
Mở 3 Terminal riêng và chạy theo thứ tự:

Terminal 1 - Khởi động MQTT Broker:
D:\Mosquitto\mosquitto.exe -v

Terminal 2 - Chạy Subscriber:
python monitor_subscriber_bai2.py

Terminal 3 - Chạy Publisher:
python sensor_publisher_bai2.py

Nếu chưa cài thư viện Paho MQTT, chạy:
python -m pip install paho-mqtt

Subscriber đăng ký topic iot/lab/+/data để nhận dữ liệu từ sensor01 và sensor02.
Nhấn Ctrl+C trong Terminal tương ứng để dừng chương trình.

3. Kết quả đạt được
- Publisher tạo dữ liệu nhiệt độ, độ ẩm ngẫu nhiên, chuyển thành JSON và gửi định kỳ qua MQTT.
- Dữ liệu được gửi lên các topic:
  + iot/lab/sensor01/data
  + iot/lab/sensor02/data
- Subscriber nhận và phân tích JSON, sau đó in tên thiết bị, nhiệt độ và độ ẩm ra màn hình.
- Nếu nhiệt độ > 35°C, in cảnh báo: CANH BAO: Nhiet do cao
- Nếu độ ẩm < 40%, in cảnh báo: CANH BAO: Do am thap
