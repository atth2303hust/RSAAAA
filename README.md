# RSA demo bằng Python

Chương trình mô phỏng RSA để học nguyên lý toán học: tạo khóa, mã hóa, giải mã và đo thời gian.

## Chạy

Yêu cầu Python 3.8 trở lên. Không cần cài thêm thư viện.

```bash
python rsa_demo.py
python rsa_demo.py --message "Toi dang hoc RSA" --bits 512
```

Chương trình mã hóa riêng từng byte UTF-8 để đơn giản hóa phần trình diễn.

**Cảnh báo:** Đây là textbook RSA không có OAEP, có tính xác định và không an toàn trong thực tế. Không dùng để bảo vệ dữ liệu thật. Với ứng dụng thực tế, dùng thư viện mật mã được kiểm chứng, RSA-OAEP và khóa đủ mạnh (thường từ 2048 bit).
