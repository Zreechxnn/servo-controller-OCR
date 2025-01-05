import cv2
import serial
import pytesseract
from difflib import SequenceMatcher
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise ValueError("Kamera tidak dapat dibuka.")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

def control_servo(state: bool):
    """Mengontrol servo melalui Arduino."""
    if state:
        arduino.write(b'ON\n')  
        print("Servo ON")
        time.sleep(5) 
        arduino.write(b'OFF\n') 
        print("Servo OFF")
    else:
        arduino.write(b'OFF\n')
        print("Servo OFF")

def read_card_numbers() -> list:
    """Membaca daftar nomor kartu dari file."""
    with open('data.txt', 'r') as file:
        return [line.strip() for line in file.readlines()]

card_numbers = read_card_numbers()
print("Mulai deteksi kartu...")

try:
    frame_skip = 10
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Gagal menangkap frame. Keluar...")
            break

        if frame_count % frame_skip == 0:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

            card_text = pytesseract.image_to_string(gray_frame, config='--psm 6').strip()
            print(f"Nomor kartu terdeteksi: {card_text}")

            max_similarity = 0
            for card_number in card_numbers:
                similarity = SequenceMatcher(None, card_text, card_number).ratio()
                max_similarity = max(max_similarity, similarity)

            if max_similarity >= 0.85:
                control_servo(True) 
            else:
                control_servo(False)  

        frame_count += 1

        cv2.imshow("Deteksi Kartu", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program dihentikan oleh pengguna.")
finally:
    cap.release()
    cv2.destroyAllWindows()
    control_servo(False)
    arduino.close()
    print("Program keluar.")
