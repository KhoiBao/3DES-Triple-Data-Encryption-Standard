#python encryption/decryption by using DES3 - made by khoi
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import binascii
# khởi tạo mã 24 byte cho key
key = DES3.adjust_key_parity(get_random_bytes(24))

# IV buộc phải là 8 bytes
iv = get_random_bytes(8)

#Hàm mã hóa:
def ma_hoa(message, key, iv):
    try:
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        goi_dem = pad(message.encode('utf-8'),DES3.block_size)
        ciphertext = cipher.encrypt(goi_dem)
        return ciphertext
    except Exception as e:
        print(f"Lỗi:{e}")
        return None
    
#Hàm Giải mã:
def giai_ma(ciphertext,key,iv):
    try:
        cipher = DES3.new(key,DES3.MODE_CBC,iv)
        decrypted_padded_message = cipher.decrypt(ciphertext)
        message = unpad(decrypted_padded_message,DES3.block_size)
        return message.decode('utf-8')
    except Exception as e:
        print(f"lỗi:{e}")
        return None
   
#CLI
while True:
    print("==================Menu====================")
    print("* Chọn chế độ: ")
    print("* 1-Mã hóa nội dung (Encrypt)")
    print("* 2-Giải mã (decrypt)")
    print("* 3-Thoát chương trình")
    choice = int(input("* Nhập lựa chọn (1-3): "))
    print("==========================================")

    if choice == 1:
    #input 
        print("Nhập vào: ") 
        message = input("")
    #Mã hóa nội dung có trong message
        ciphertext = ma_hoa(message, key, iv)
        print(f"Tin nhắn đã mã hóa:{ciphertext}")
        hex_ciphertext = binascii.hexlify(ciphertext).decode()
        hex_key = binascii.hexlify(key).decode()
        hex_iv = binascii.hexlify(iv).decode()
        # chữ -> mã hex và binascii
        print(f"Tin nhắn đã mã hóa (hex): {hex_ciphertext}")
        print(f"Key (hex): {hex_key}")
        print(f"IV (hex): {hex_iv}") 
    
    elif choice == 2:
        hex_ciphertext = input("Nhập mã (hex) cần giải mã: ")
        hex_key = input("Nhập key hex: ")
        hex_iv = input("Nhập IV hex: ")

        try:
            ciphertext = binascii.unhexlify(hex_ciphertext)
            key = binascii.unhexlify(hex_key)
            iv = binascii.unhexlify(hex_iv)
            # mã hex -> chữ
            decrypted_message = giai_ma(ciphertext, key, iv)
            print(f"\n Tin nhắn đã được giải mã: {decrypted_message}")

        except Exception as e:
            print(f"Lỗi khi chuyển đổi dữ liệu: {e}")
        
    elif choice == 3:
            print("Thoát chương trình")
            break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2.")

