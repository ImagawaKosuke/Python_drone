import time
import cv2
from djitellopy import Tello

tello = Tello('192.168.10.1', 8889)
tello.connect()

tello.streamon()
tello.takeoff()

try:
    while True:
        img = tello.get_frame_read().frame#
        im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #BGRとRGBを反転
        cv2.imshow('frame', im_rgb)
        key = cv2.waitKey(1)
        if key == ord('c'):
            cv2.imwrite('drone.png', im_rgb)
        elif key == ord('l'):
            tello.land()
        elif key == ord('q'):
            tello.streamoff()
            tello.land()
            time.sleep(3)
            exit(1)
except:
    exit(1)

exit()


'''
tello.takeoff()

time.sleep(3)
tello.move_up(50)
print("OK")
time.sleep(3)
# ストリームを開始し、画像を取得して保存します
tello.streamon()
frame_read = tello.get_frame_read()
cv2.imwrite("picture1.png", frame_read.frame)

time.sleep(5)
# ストリームを再度開始し、画像を取得して保存します
tello.streamon()
frame_read = tello.get_frame_read()
cv2.imwrite("picture2.png", frame_read.frame)

tello.move_down(50)

time.sleep(1)
tello.land()
'''