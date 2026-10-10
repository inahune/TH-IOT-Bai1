# README - CHƯƠNG TRÌNH MQTT BÀI 1

## 1. Broker sử dụng
- MQTT Broker: Mosquitto 2.1.2
- Địa chỉ: `localhost`
- Cổng: `1883`
- Topic: `iot/lab/message`

## 2. Cách chạy chương trình
Mở 3 Terminal riêng và chạy theo thứ tự:

**Terminal 1 - Khởi động MQTT Broker:**
```bat
D:\mosquitto\mosquitto.exe -v
```

**Terminal 2 - Chạy Subscriber:**
```bat
python subscriber_bai1.py
```

**Terminal 3 - Chạy Publisher:**
```bat
python publisher_bai1.py
```

Subscriber đăng ký topic `iot/lab/message` để nhận thông điệp từ Publisher.

Nhấn `Ctrl+C` trong Terminal tương ứng để dừng chương trình.

## 3. Kết quả đạt được
- Publisher kết nối MQTT Broker, tạo thông điệp dạng JSON chứa họ tên, mã sinh viên và nội dung tin nhắn.
- Publisher gửi thông điệp lên topic `iot/lab/message`.
- Subscriber nhận và phân tích dữ liệu JSON, sau đó hiển thị thời gian nhận, topic, họ tên, mã sinh viên và nội dung thông điệp.
- Chương trình chạy thành công, Subscriber nhận được thông điệp: `Xin chao tu client Python MQTT.`

(.venv) D:\Desktop\IoT\thuc_hanh_tuan1>python subscriber_bai1.py
Da ket noi MQTT Broker thanh cong.
Dang lang nghe topic: iot/lab/message

========== THONG DIEP NHAN DUOC ==========
Thoi gian: 2026-10-10 17:40:28
Topic: iot/lab/message
Thong diep: Xin chao tu client Python MQTT - B23DCCN618 - Cao Thi Thanh Nhan
==========================================

Da dung Subscriber.

(.venv) D:\Desktop\IoT\thuc_hanh_tuan1>python publisher_bai1.py
Da ket noi MQTT Broker thanh cong.
Topic: iot/lab/message
Da gui thong diep: Xin chao tu client Python MQTT - B23DCCN618 - Cao Thi Thanh Nhan
