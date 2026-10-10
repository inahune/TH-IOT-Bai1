# README - CHƯƠNG TRÌNH MQTT BÀI 3: SMART LIGHT DEVICE

## 1. Broker sử dụng

- **MQTT Broker:** Mosquitto 2.1.2
- **Địa chỉ:** `localhost`
- **Cổng:** `1883`

## 2. Cách chạy chương trình

Mở 2 Terminal riêng và chạy theo thứ tự sau:

### Terminal 1 - Chạy Smart Light Device

```powershell
python device.py
```

### Terminal 2 - Chạy Controller App

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