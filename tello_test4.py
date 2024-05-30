# tkinterライブラリの読み込み
import tkinter
import time
import cv2
from djitellopy import Tello

# ウィンドウの作成と、Tkinterオブジェクトの取得
window = tkinter.Tk()

# ウィンドウのサイズと位置を設定
window.geometry("500x400+300+200")
tello = Tello('192.168.10.1', 8889)

#Telloを接続
def connect():
    tello.connect()

#Telloを離陸
def takeoff_land():
    tello.takeoff()

#Telloを着陸
def land_tello():
    tello.land()

#前進
def forward():
    tello.move_forward(20)

#後退
def back():
    tello.move_back(20)

#左に移動
def left():
    tello.move_left(20)

#右に移動
def right():
    tello.move_right(20)

#上昇
def up():
    tello.move_up(20)

#下降
def down():
    tello.move_down(20)

# ボタンを作成
button_tello = tkinter.Button(window, text="Telloをつなげる", font=("MSゴシック", "10", "bold"), command =  connect)
button_takeoff = tkinter.Button(window, text="離陸", font=("MSゴシック", "10", "bold"), command = takeoff_land)
button_land = tkinter.Button(window, text="着陸", font=("MSゴシック", "10", "bold"), command = land_tello)

button_forward = tkinter.Button(window, text="↑", font=("MSゴシック", "15", "bold"), command =  forward)
button_back = tkinter.Button(window, text="↓", font=("MSゴシック", "15", "bold"), command =  back)
button_right = tkinter.Button(window, text="→", font=("MSゴシック", "15", "bold"), command =  right)
button_left = tkinter.Button(window, text="←", font=("MSゴシック", "15", "bold"), command =  left)

button_up = tkinter.Button(window, text="上昇", font=("MSゴシック", "10", "bold"), command =  up)
button_down = tkinter.Button(window, text="下降", font=("MSゴシック", "10", "bold"), command =  down)

# GUI設計
button_tello.place(x=10, y=10)
button_takeoff.place(x=10, y=50)
button_land.place(x=50, y=50)
button_forward.place(x=200, y=10, width=40,height=40)
button_back.place(x=200, y=60, width=40,height=40)
button_right.place(x=250, y=60, width=40,height=40)
button_left.place(x=150, y=60, width=40,height=40)
button_up.place(x=350, y=10)
button_down.place(x=350, y=50)


# ウィンドウのループ処理
window.mainloop()
