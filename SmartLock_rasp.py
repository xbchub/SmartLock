# !/usr/bin/python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO  # 导入Rpi.GPIO库函数命名为GPIO
import time  # 导入计时time函数
import socket
import cv2


def recieve():
    while True:
        try:
            conn, addr = s.accept()
            print("connect by", addr)
            index = conn.recv(1024)
            index = int(index.decode())
            if index:
                GPIO.output(switchOut, GPIO.HIGH)
                print("关锁")
            else:
                GPIO.output(switchOut, GPIO.LOW)
                print("开锁")
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        except (KeyboardInterrupt, SystemExit):
            GPIO.cleanup()
            break


if __name__ == '__main__':
    # GPIO port
    # switchIn = 36
    switchOut = 18
    # flowSensor = 12
    # light = 32

    GPIO.setmode(GPIO.BOARD)  # 将GPIO编程方式设置为BOARD模式
    GPIO.setup(switchOut, GPIO.OUT)
    # GPIO.setup(flowSensor, GPIO.IN)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = ('192.168.43.207', 8010)
    s.bind(address)  # 将Socket（套接字）绑定到地址
    s.listen(True)  # 开始监听TCP传入连接
    print('Waiting for ...')

    recieve()

