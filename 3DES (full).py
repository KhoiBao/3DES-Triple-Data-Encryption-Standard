#python encryption/decryption by using DES3 - made by khoi
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad # "làm đầy" (padding), bổ sung thêm khi dữ liệu đưa vào không là bội số của 8, và "bỏ làm đầy" (unpadding) sau khi "làm đầy" 
import binascii # chuyển từ chữ -> hex và hex -> chữ
import hashlib 

#Hàm xử lý key (trường hợp người dùng nhập vào không đủ 24 bytes)
def xu_ly_key(secret_key):
    hashed = hashlib.sha256(secret_key.encode('utf-8')).digest()
    key = hashed[:24] 
    # SHA-256 = Secure Hash Algorithm 256-bit chuyển đổi dữ liệu đầu vào thành chuỗi 256-bit (32 byte)
    #digest(): tiêu hóa, tức là trả về kết quả dưới dạng byte (32 byte)
    # [:24] chỉ lấy 24 byte đầu tiên để làm key
    key = DES3.adjust_key_parity(key)
    return key

#Hàm mã hóa:
def ma_hoa(message, key):
    try:
        cipher = DES3.new(key, DES3.MODE_ECB)
        goi_dem = pad(message.encode('utf-8'),DES3.block_size)
        ciphertext = cipher.encrypt(goi_dem)
        return ciphertext
    except Exception as e:
        print(f"Lỗi:{e}")
        return None
    
#Hàm Giải mã:
def giai_ma(ciphertext,key):
    try:
        cipher = DES3.new(key,DES3.MODE_ECB)
        decrypted_padded_message = cipher.decrypt(ciphertext)
        message = unpad(decrypted_padded_message,DES3.block_size)
        return message.decode('utf-8')
    except Exception as e:
        print(f"lỗi:{e}")
        return None
#============================================================== 
#CLI
while True:
    print("==================Menu====================")
    print("* Chọn chế độ: ")
    print("* 1-Mã hóa nội dung (Encrypt)")
    print("* 2-Giải mã (decrypt)")
    print("* 3-Thoát chương trình")
    choice = int(input("* Nhập lựa chọn (1-3): "))
    print("==========================================")
#==============================================================
    if choice == 1:
    #input 
        message = input("Nhập vào: ")
        secret_key = input("Nhập key: ")
    #Mã hóa nội dung có trong message
        key = xu_ly_key(secret_key)
        ciphertext = ma_hoa(message, key)
        hex_ciphertext = binascii.hexlify(ciphertext).decode()
        hex_key = binascii.hexlify(key).decode()
        # chữ -> mã hex
        print(f"\nTin nhắn đã mã hóa:{ciphertext}")
        print(f"Tin nhắn đã mã hóa (hex): {hex_ciphertext}")
        print(f"\nKey:{key}")
        print(f"Key (hex): {hex_key}")
    
    elif choice == 2:
        hex_ciphertext = input("Nhập mã (hex) cần giải mã: ")
        hex_key = input("Nhập key (hex): ")

        try:
            ciphertext = binascii.unhexlify(hex_ciphertext)
            key = binascii.unhexlify(hex_key)
            # mã hex -> chữ
            decrypted_message = giai_ma(ciphertext, key)
            print(f"\n Tin nhắn đã được giải mã: {decrypted_message}")

        except Exception as e:
            print(f"Lỗi khi chuyển đổi dữ liệu: {e}")
        
    elif choice == 3:
            print("Thoát chương trình")
            break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")

