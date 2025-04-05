import os
import qrcode
import cv2
from pyzbar.pyzbar import decode

def create_qr(data, filename="qrcode.png"):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR saved as {filename}")
    
def read_qr(filename="qrcode.png"):
    img = cv2.imread(filename)
    codes = decode(img)
    for code in codes:
        print("Decoded:", code.data.decode())
    os.remove(filename)
    print(f"{filename} deleted after decoding.")

choice = input("Encode or Decode? (e/d): ").lower()
if choice == 'e':
    create_qr(input("Enter data to encode: "))
elif choice == 'd':
    read_qr(input("Enter QR image filename: "))
else:
    print("Invalid choice")
