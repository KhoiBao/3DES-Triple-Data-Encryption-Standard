#python encryption/decryption by using DES3 - made by khoi
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad 
# "làm đầy" (padding), bổ sung thêm khi dữ liệu đưa vào không là bội số của 8, và "bỏ làm đầy" (unpadding) sau khi "làm đầy" 
import binascii # chuyển từ mã nhị phân -> dạng ASCII và ngược lại

#Hàm xử lý key (trường hợp người dùng nhập vào không đủ/hoặc quá mức 24 bytes)
def xu_ly_key(key):
    key = key.encode('utf-8')
    if len(key) < 24:
        key = key.ljust(24,b' ') # ljust bổ sung vào cuối cho đủ 24 ký tự
    elif len(key) > 24:
        key = key[:24]
    
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
        message = input("Nhập vào nội dung cần mã hóa: ")
        key = input("Nhập key : ")
        key = xu_ly_key(key)
            
        ciphertext = ma_hoa(message, key) #Mã hóa nội dung có trong message
            
    # chữ -> mã hex
        hex_ciphertext = binascii.hexlify(ciphertext).decode()
        print(f"\nTin nhắn đã mã hóa: {ciphertext}")
        print(f"Tin nhắn đã mã hóa (hex): {hex_ciphertext}")

    elif choice == 2:
        hex_ciphertext = input("Nhập mã (hex) cần giải mã: ")
        key = input("Nhập key: ")

        try:
        # mã hex -> chữ
            ciphertext = binascii.unhexlify(hex_ciphertext)
            key = xu_ly_key(key)
        
        # Giải mã:
            decrypted_message = giai_ma(ciphertext, key)
            print(f"\n Tin nhắn đã được giải mã: {decrypted_message}")

        except Exception as e:
            print(f"Lỗi khi chuyển đổi dữ liệu: {e}")
        
    elif choice == 3:
            print("Thoát chương trình...")
            break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1,2 hoặc 3.")

