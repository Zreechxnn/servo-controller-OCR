# servo-controller-OCR

Servo Controller-OCR is a project that integrates computer vision, OCR (Optical Character Recognition), and Arduino to control a servo motor based on the detection of specific text (e.g., card numbers). This project uses Python for the computer vision and OCR processing, and Arduino for servo motor control.

## Features
- Real-time card detection using a webcam.
- Optical Character Recognition (OCR) using Tesseract.
- Servo motor control via Arduino based on detected text similarity.
- Adjustable similarity threshold for text recognition.
- Easy configuration for custom card numbers.

---

## Technologies Used
### Python Libraries
- **OpenCV**: For webcam video capture and image preprocessing.
- **pytesseract**: For text recognition from images.
- **serial**: For communication with Arduino.
- **difflib**: For text similarity comparison.

### Arduino Components
- **Servo.h**: For servo motor control.
- Arduino Uno or similar board.
- Servo motor.
- USB cable for serial communication.

---

## Prerequisites
1. Install Python (3.x).
2. Install Tesseract-OCR:
   - Download and install Tesseract from [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).
   - Update the path to the Tesseract executable in the Python script:
     ```python
     pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
     ```
3. Install required Python libraries:
   ```bash
   pip install opencv-python pyserial pytesseract
   ```
4. Set up an Arduino with a servo motor.

---

## Hardware Setup
- Connect the servo motor's signal pin to Arduino pin 2.
- Ensure the Arduino is connected to your computer via USB.
- Upload the provided Arduino code to your Arduino board using the Arduino IDE.

---

## Usage
### 1. Prepare Card Data
Create a file named `data.txt` in the project directory and add the card numbers (one per line) that should trigger the servo.

### 2. Run the Python Script
Execute the Python script to start real-time card detection:
```bash
python ocr.py
```

- The webcam will capture frames and process them for OCR.
- If the detected text matches any card number in `data.txt` with a similarity score ≥ 85%, the servo motor will turn on for 5 seconds, then turn off.
- Press `q` to exit the program.

---

## Python Code Explanation
The Python script performs the following tasks:
1. Captures video frames using OpenCV.
2. Processes the frames (grayscale and Gaussian blur) for better OCR results.
3. Uses Tesseract to extract text from the processed frames.
4. Compares the detected text with predefined card numbers using `SequenceMatcher`.
5. Sends commands (`ON`/`OFF`) to the Arduino via serial communication to control the servo motor.

---

## Arduino Code Explanation
The Arduino code listens for serial commands (`ON` or `OFF`):
- `ON`: Rotates the servo motor to 90° (active position).
- `OFF`: Rotates the servo motor back to 0° (idle position).

---

## Important Notes
1. Ensure the correct COM port is specified in the Python script:
   ```python
   arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
   ```
2. Adjust the camera resolution if needed:
   ```python
   cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
   cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
   ```
3. Modify the similarity threshold as necessary in the Python script (default is 85%).

---

## Troubleshooting
- **Webcam not detected:** Ensure the camera is properly connected and accessible.
- **Serial communication issues:** Verify the correct COM port and baud rate are set in the Python script.
- **OCR accuracy issues:**
  - Improve lighting conditions.
  - Use high-quality text for recognition.
  - Adjust Tesseract configuration options (e.g., `--psm` mode).

---

## Future Improvements
- Add a GUI for better user interaction.
- Enhance text preprocessing for improved OCR accuracy.
- Integrate additional sensors or features for more complex applications.

---

## License
This project is open-source and available under the [License](LICENSE).

---

## Acknowledgments
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV](https://opencv.org/)
- Arduino community for their comprehensive documentation and examples.

<p align="center">©️ 2025 Rechan Dinata</p>
