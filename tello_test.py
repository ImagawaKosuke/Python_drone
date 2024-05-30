#!/usr/bin/env python
import socket
import time

#udpソケット作成
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ('192.168.10.1', 8889)

#コマンドモードを使うため'command'というテキストを投げる
socket.sendto('command'.encode('utf-8'),tello_address)

time.sleep(1)
socket.sendto('takeoff'.encode('utf-8'),tello_address)
socket.sendto('delay 2'.encode('utf-8'),tello_address)

socket.sendto('up 100'.encode('utf-8'),tello_address)
time.sleep(1)

socket.sendto('down 100'.encode('utf-8'),tello_address)
time.sleep(1)

#着陸のため'land'というテキストを投げる
socket.sendto('land'.encode('utf-8'),tello_address)