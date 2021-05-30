# 发送端
import socket
import cv2
import numpy



# 是否锁门
def lock(s):
    s.send(str(1).encode())
    # ToDo 本地应当记录此时状态


# 是否解锁
def unlock(s):
    s.send(str(0).encode())
    # ToDo 本地应当记录此时状态

# 调用def main开始，两种状态对应lock_index
def main(lock_index):
    # socket.SOCK_STREAM 代表基于TCP的流式socket通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接服务端
    address_server = ('192.168.43.207', 8010)
    sock.connect(address_server)

    # 调用锁门和解锁函数
    if lock_index:
        lock(sock)
    else:
        unlock(sock)
    sock.close(sock)

