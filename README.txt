# Bài tập lớn: 5. TÌM HIỂU VỀ GIẢI THUẬT MÃ HÓA 3DES (CƠ CHẾ HOẠT ĐỘNG
CỦA GIẢI THUẬT MÃ HÓA – GIẢI MÃ, CHO VD VÀ VIẾT ỨNG
DỤNG CHO PHÉP MÃ HÓA VÀ GIẢI MÃ CÁC GIẢI THUẬT) 

**Nhóm các tác giả:** Nguyễn Bảo Khôi, Nguyễn Ngọc Quý, Long Huỳnh Quốc Tài

# 1. Giới thiệu  
Đây là chương trình mã hóa và giải mã dữ liệu bằng thuật toán DES3 (Triple DES) sử dụng Python. Chương trình hỗ trợ chế độ ECB , cho phép người dùng nhập khóa thủ công hoặc tự động sinh khóa nếu cần.  

## 2. Cài đặt  
Trước khi chạy chương trình, bạn cần cài đặt thư viện `pycryptodome`. Tùy vào phiên bản hệ điều hành của bạn đang sử dụng:  

Windows: Command Prompt hoặc PowerShell:
py -m pip install pycryptodome

macOS/Linux:
python3 -m pip install perceptome

Các tài liệu hướng dẫn tải: 
Trang chủ Pycryptodome: https://pycryptodome.readthedocs.io/en/latest/src/installation.html#windows-from-sources

Youtube:
https://www.youtube.com/watch?v=O4dYEzk9rzc

### 3. Hướng dẫn sử dụng
Khi compile code sẽ xuất hiện menu:
==================Menu====================
* Chọn chế độ:
* 1-Mã hóa nội dung (Encrypt)
* 2-Giải mã (decrypt)
* 3-Thoát chương trình
* Nhập lựa chọn (1-3):

Lựa chọn 1: Bạn muốn mã hóa nội dung (encrypt), hãy nhấn số 1 rồi Enter, sau đó hãy nhập theo chỉ dẫn, khi nhập đoạn tin nhắn cần mã hóa và key cần thiết, sẽ xuất hiện 4 dòng chữ. ví dụ:
"
Nhập vào: ThayThinhDepTrai
Nhập key: 012345678910

Tin nhắn đã mã hóa: b'\x89\x8c{\xb21\x179\x94#=u\xb5\x9f\xf5U\x90\xb1\xc9\xc6;\x13\xbc\xdd\xd8'
Tin nhắn đã mã hóa (hex): 898c7bb231173994233d75b59ff55590b1c9c63b13bcddd8

Key: b'\xcdW\x13\x9bEIQ\x97\xae\xb9\x80\xa2\x86\x1a\xab\xf2\x19\xb5\x02\x8c\xfd7\x16\x80'
Key (hex): cd57139b45495197aeb980a2861aabf219b5028cfd371680
"
=> Sau khi xuất 4 dòng sẽ xuất hiện tiếp thanh menu.

Lựa chọn 2: Bạn muốn giải mã nội dung (decrypt), hãy tiếp tục nhấn số 2 rồi Enter, sau đó sẽ yêu cầu bạn nhập đoạn tin nhắn đã mã hóa (dạng hex) và key dạng hex, ví dụ tôi sẽ sử dụng lại tin nhắn đã mã hóa phía trên và đoạn key (dạng hex):
==========================================
Nhập mã (hex) cần giải mã: 898c7bb231173994233d75b59ff55590b1c9c63b13bcddd8
Nhập key (hex): cd57139b45495197aeb980a2861aabf219b5028cfd371680

 Tin nhắn đã được giải mã: ThayThinhDepTrai
===========================================
Hoặc bạn có thể sử dụng đoạn tin nhắn hex và key khác của riêng bạn!

Cảm ơn bạn dã sử dụng đoạn code của chúng tôi! Chúc bạn một ngày tốt lành.

