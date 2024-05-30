import time
import cv2
from djitellopy import Tello

tello = Tello('192.168.10.1', 8889)
tello.connect()

tello.takeoff()

time.sleep(3)
tello.move_up(50)
time.sleep(3)
#正方形に迂回する
for i in range(4):
    tello.move_forward(50)
    time.sleep(1)
    tello.rotate_counter_clockwise(90)
    time.sleep(1)


tello.move_down(50)

time.sleep(1)
tello.land()