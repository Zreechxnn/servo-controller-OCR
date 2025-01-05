#include <Servo.h>

#define SERVO_PIN 2

Servo myServo; 

void setup() {
  myServo.attach(SERVO_PIN); 
  Serial.begin(9600);  
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); 
    
    command.trim();  

    if (command == "ON") {
      myServo.write(90);  
      Serial.println("Servo ON");  
    } else if (command == "OFF") {
      myServo.write(0);  
      Serial.println("Servo OFF");  
    } else {
      Serial.println("Unknown command");  
    }
  }
}
