# TH-IOT-Bai1

# Chương trình bài 1
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

```text
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
```

# Chương trình bài 2

## 1. Broker sử dụng

- **MQTT Broker:** Mosquitto 2.1.2
- **Địa chỉ:** `localhost`
- **Cổng:** `1883`

## 2. Cách chạy chương trình

Mở 3 Terminal riêng và chạy theo thứ tự sau:

### Terminal 1 - Khởi động MQTT Broker

```powershell
D:\Mosquitto\mosquitto.exe -v
```

### Terminal 2 - Chạy Subscriber

```powershell
python monitor_subscriber_bai2.py
```

### Terminal 3 - Chạy Publisher

```powershell
python sensor_publisher_bai2.py
```

Nếu chưa cài thư viện Paho MQTT, chạy lệnh:

```powershell
python -m pip install paho-mqtt
```

Subscriber đăng ký topic `iot/lab/+/data` để nhận dữ liệu từ `sensor01` và `sensor02`.

Nhấn `Ctrl + C` trong Terminal tương ứng để dừng chương trình.

## 3. Kết quả đạt được

- Publisher tạo dữ liệu nhiệt độ và độ ẩm ngẫu nhiên, chuyển thành JSON và gửi định kỳ qua MQTT.
- Dữ liệu được gửi lên các topic:
  - `iot/lab/sensor01/data`
  - `iot/lab/sensor02/data`
- Subscriber nhận và phân tích JSON, sau đó in tên thiết bị, nhiệt độ và độ ẩm ra màn hình.
- Nếu nhiệt độ > 35°C, in cảnh báo: `CANH BAO: Nhiet do cao`.
- Nếu độ ẩm < 40%, in cảnh báo: `CANH BAO: Do am thap`.

# Chương trình bài 3

## 1. Broker sử dụng

- **MQTT Broker:** Mosquitto 2.1.2
- **Địa chỉ:** `localhost`
- **Cổng:** `1883`

## 2. Cách chạy chương trình

Mở 3 Terminal riêng và chạy theo thứ tự sau:

### Terminal 1 - Khởi động MQTT Broker

```powershell
D:\Mosquitto\mosquitto.exe -v
```

### Terminal 2 - Chạy Smart Light Device

```powershell
python device.py
```

### Terminal 3 - Chạy Controller App

```powershell
python controller.py
```

Nhấn `Ctrl + C` hoặc nhập `EXIT` tại Controller để kết thúc chương trình.

## 3. Kết quả đạt được

- Smart Light Device đăng ký topic `iot/lab/light01/cmd` để nhận lệnh điều khiển từ Controller.
- Controller cho phép người dùng nhập lệnh `ON` hoặc `OFF` từ bàn phím.
- Controller gửi lệnh điều khiển dưới dạng JSON lên topic `iot/lab/light01/cmd`.
- Device nhận và phân tích JSON, kiểm tra `device_id` và tính hợp lệ của lệnh.
- Nếu lệnh hợp lệ:
  - `ON`: chuyển trạng thái đèn thành bật.
  - `OFF`: chuyển trạng thái đèn thành tắt.
- Sau mỗi lệnh hợp lệ, Device gửi trạng thái mới dưới dạng JSON lên topic `iot/lab/light01/status`.
- Controller đăng ký topic trạng thái, nhận phản hồi và hiển thị thông tin đèn.
- Nếu người dùng nhập lệnh khác `ON`, `OFF` hoặc `EXIT`, Controller thông báo lệnh không hợp lệ.

## 4. Ví dụ dữ liệu MQTT

### Lệnh điều khiển

Topic: `iot/lab/light01/cmd`

```json
{
  "device_id": "light01",
  "cmd": "ON"
}
```

### Trạng thái phản hồi

Topic: `iot/lab/light01/status`

```json
{
  "device_id": "light01",
  "status": "ON"
}
```

## 5. Luồng hoạt động

1. Mosquitto khởi động và chờ các client kết nối.
2. Device kết nối broker và đăng ký topic điều khiển.
3. Controller kết nối broker và đăng ký topic trạng thái.
4. Người dùng nhập lệnh điều khiển.
5. Controller publish lệnh lên broker.
6. Device nhận lệnh, cập nhật trạng thái và publish phản hồi
7. Controller nhận phản hồi và hiển thị trạng thái đèn.