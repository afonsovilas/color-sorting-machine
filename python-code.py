# Colour Sorting Machine - main program (Raspberry Pi 3)
#
# Code as submitted in the final project report (PAP, 2023/2024).
# - Webcam: reads the hue (HSV) of the pixel at the centre of the image
# - servo1 (GPIO pin 12): moves each piece through the machine
# - servo2 (GPIO pin 32): turns the guide to the compartment of the detected colour
# - Non-blocking timing with time.time() (instead of time.sleep()) keeps the camera running
# Press Esc to exit.

import RPi.GPIO as GPIO
import cv2
import time
cap= cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(12,50)
GPIO.setup(32,GPIO.OUT)
servo2 = GPIO.PWM(32,50)
servo1.start(0)
color="undefined"
tempo1=int(round(time.time()*1000))
tempo3=int(round(time.time()*1000))
tempo5=int(round(time.time()*1000))
tempo7=int(round(time.time()*1000))
tempo9=int(round(time.time()*1000))
tempo11=int(round(time.time()*1000))
tempo0=int(round(time.time()*1000))
tempo99=int(round(time.time()*1000))
while True:
  _, frame = cap.read()
  hsv_frame =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  height, width, _ = frame.shape
  cx = int(width / 2)
  cy = int(height / 2)
  pixel_center=hsv_frame[cy,cx]
  hue_value = pixel_center[0]
  tempo0x=int(round(time.time()*1000))
  if (tempo0x-tempo0>1000):
    servo1.ChangeDutyCycle(12)
    tempo0=float("+inf")
    print("ola")
  tempo2=int(round(time.time()*1000))
  if (tempo2-tempo1>2000):
    servo1.ChangeDutyCycle(0)
    tempo1=float("+inf")
    print("a")
  tempo4=int(round(time.time()*1000))
  if (tempo4-tempo3>3000):
    servo1.ChangeDutyCycle(7)
    tempo3=float("+inf")
    print("todos")
  tempo6=int(round(time.time()*1000))
  if (tempo6-tempo5>3700):
    servo1.ChangeDutyCycle(0)
    servo2.start(0)
    tempo5=float("+inf")
    print("tudo")
    color="Undefined"
    if hue_value<20:
      color="LARANJA"
      servo2.ChangeDutyCycle(9)
    elif hue_value<38:
      color="AMARELO"
      servo2.ChangeDutyCycle(7)
    elif hue_value<125:
      color="VERDE"
      servo2.ChangeDutyCycle(6)
    elif hue_value<140:
      color="ROXO"
      servo2.ChangeDutyCycle(4)
    elif hue_value<169:
      color="ROSA"
      servo2.ChangeDutyCycle(2)
    else:
      color="LARANJA"
      servo2.ChangeDutyCycle(9)
  tempoxx=int(round(time.time()*1000))
  if (tempoxx-tempo99>4100):
    servo2.ChangeDutyCycle(0)
    tempo99=float("+inf")
    print ("k")
  tempo8=int(round(time.time()*1000))
  if (tempo8-tempo7>4700):
    servo1.ChangeDutyCycle(2)
    tempo7=float("+inf")
    print("bem")
  tempo10=int(round(time.time()*1000))
  if (tempo10-tempo9>5200):
    servo1.ChangeDutyCycle(0)
    tempo9=float("+inf")
    print("?")
  tempo12=int(round(time.time()*1000))
  if (tempo12-tempo11>5700):
    tempo1=int(round(time.time()*1000))
    tempo3=int(round(time.time()*1000))
    tempo5=int(round(time.time()*1000))
    tempo7=int(round(time.time()*1000))
    tempo9=int(round(time.time()*1000))
    tempo11=int(round(time.time()*1000))
    tempo0=int(round(time.time()*1000))
    tempo99=int(round(time.time()*1000))
  pixel_center_bgr= frame[cy,cx]
  b, g, r= int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
  cv2.putText(frame, color, (10,70), 0,1.5 ,(b,g,r), 2)
  cv2.circle(frame, (cx, cy), 5, (0, 0, 0), 3)
  cv2.imshow("Frame", frame)
  key=cv2.waitKey(1)
  if key == 27:
    break
cap.release()
cv2.destroyAllWindows()