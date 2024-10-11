# Hướng Dẫn Sử Dụng Script

Script Python này cho phép bạn thực hiện lệnh `ping` và `tracert` liên tục dựa trên đầu vào từ người dùng. 

## Tổng Quan về Script

Script sẽ:
1. Nhận đầu vào từ người dùng (là một tên miền hoặc địa chỉ IP).
2. Sử dụng lệnh `ping` và `tracert` với đầu vào đó.
3. Lặp lại quy trình cho đến khi người dùng nhập `"czx"` để kết thúc vòng lặp và dừng script.

### Tính Năng Chính:
- **Ping và Tracert**: Với bất kỳ tên miền hoặc địa chỉ IP nào được nhập, script sẽ chạy cả lệnh `ping` và `tracert`.
- **Lặp lại**: Script liên tục hỏi đầu vào từ người dùng cho đến khi nhận được lệnh dừng (`czx`).


## Cách Chạy Script

1. **Tải Script**

2. **Mở Command Prompt hoặc Terminal**:
   - Di chuyển đến thư mục nơi lưu trữ file script.

3. **Chạy Script**:
   Chạy lệnh sau để thực thi script:
   ```bash
   python {tên_file_ban_luu}
