import numpy as np
import socket
import time
import struct
import time
import array


def connect(HOST, PORT):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((HOST, PORT))
    return tcp_socket


def disconnect(tcp_socket):
    tcp_socket.close()
    return tcp_socket


def isconnect(tcp_socket):
    data = tcp_socket.recv(1116)
    message_size = struct.unpack('!1i', data[0:4])
    print(message_size)
    if np.asarray(message_size) != 1116:
        flag = 0
    else:
        flag = 1
    return flag


# def get_data(tcp_socket):
#     data = tcp_socket.recv(1116)
#     return data
def get_position(data):
    position = struct.unpack('!6d', data[444:492])
    a = np.array(position)  # numpy数组
    b = array.array('f', a)
    return b


def get_JJ_position(data):
    JJ_position = struct.unpack('!6d', data[252:300])
    a = np.array(JJ_position)  # numpy数组
    b = array.array('f', a)
    return b


def get_JJ_speed(data):
    JJ_speed = struct.unpack('!6d', data[300:348])
    a = np.array(JJ_speed)  # numpy数组
    b = array.array('f', a)
    return b


def send_speedj(tcp_socket, qre, acc, dt):
    send_data1 = '''
             def svt(): 
                  speedj([qre[0],qre[1],qre[2],qre[3],qre[4],qre[5]],acc,dt)      
             end
             '''
    send_data1 = send_data1.replace("qre[0]", str(qre[0]))
    send_data1 = send_data1.replace("qre[1]", str(qre[1]))
    send_data1 = send_data1.replace("qre[2]", str(qre[2]))
    send_data1 = send_data1.replace("qre[3]", str(qre[3]))
    send_data1 = send_data1.replace("qre[4]", str(qre[4]))
    send_data1 = send_data1.replace("qre[5]", str(qre[5]))
    send_data1 = send_data1.replace("acc", str(acc))
    send_data1 = send_data1.replace("dt", str(dt))
    # print(send_data1)
    tcp_socket.send(send_data1.encode('utf8'))


def send_movec(tcp_socket, pose_via, pose_to, acc, vv, radius):
    send_data1 = '''
               def svt():
                movec(p[pose_via[0],pose_via[1],pose_via[2],pose_via[3],pose_via[4],pose_via[5]],p[pose_to[0],pose_to[1],pose_to[2],pose_to[3],pose_to[4],pose_to[5]],a=acc,v=vv,r=radius)
                end
            '''
    send_data1 = send_data1.replace("pose_via[0]", str(pose_via[0]))
    send_data1 = send_data1.replace("pose_via[1]", str(pose_via[1]))
    send_data1 = send_data1.replace("pose_via[2]", str(pose_via[2]))
    send_data1 = send_data1.replace("pose_via[3]", str(pose_via[3]))
    send_data1 = send_data1.replace("pose_via[4]", str(pose_via[4]))
    send_data1 = send_data1.replace("pose_via[5]", str(pose_via[5]))
    send_data1 = send_data1.replace("pose_to[0]", str(pose_to[0]))
    send_data1 = send_data1.replace("pose_to[1]", str(pose_to[1]))
    send_data1 = send_data1.replace("pose_to[2]", str(pose_to[2]))
    send_data1 = send_data1.replace("pose_to[3]", str(pose_to[3]))
    send_data1 = send_data1.replace("pose_to[4]", str(pose_to[4]))
    send_data1 = send_data1.replace("pose_to[5]", str(pose_to[5]))
    send_data1 = send_data1.replace("acc", str(acc))
    send_data1 = send_data1.replace("vv", str(vv))
    send_data1 = send_data1.replace("radius", str(radius))
    # print(send_data1)
    tcp_socket.send(send_data1.encode('utf8'))


def send_movel(tcp_socket, pose, acc, vv, tt, radius):
    send_data1 = '''
             def svt(): 
                  movel(p[pose[0],pose[1],pose[2],pose[3],pose[4],pose[5]],a=acc, v=vv, t=tt, r=radius)      
             end
             '''
    send_data1 = send_data1.replace("pose[0]", str(pose[0]))
    send_data1 = send_data1.replace("pose[1]", str(pose[1]))
    send_data1 = send_data1.replace("pose[2]", str(pose[2]))
    send_data1 = send_data1.replace("pose[3]", str(pose[3]))
    send_data1 = send_data1.replace("pose[4]", str(pose[4]))
    send_data1 = send_data1.replace("pose[5]", str(pose[5]))
    send_data1 = send_data1.replace("acc", str(acc))
    send_data1 = send_data1.replace("vv", str(vv))
    send_data1 = send_data1.replace("tt", str(tt))
    send_data1 = send_data1.replace("radius", str(radius))
    # print(send_data1)
    tcp_socket.send(send_data1.encode('utf8'))


def send_movej(tcp_socket, pose, acc, vv, tt, radius):
    send_data1 = '''
             def svt(): 
                  movel([pose[0],pose[1],pose[2],pose[3],pose[4],pose[5]],a=acc, v=vv, t=tt, r=radius)      
             end
             '''
    send_data1 = send_data1.replace("pose[0]", str(pose[0]))
    send_data1 = send_data1.replace("pose[1]", str(pose[1]))
    send_data1 = send_data1.replace("pose[2]", str(pose[2]))
    send_data1 = send_data1.replace("pose[3]", str(pose[3]))
    send_data1 = send_data1.replace("pose[4]", str(pose[4]))
    send_data1 = send_data1.replace("pose[5]", str(pose[5]))
    send_data1 = send_data1.replace("acc", str(acc))
    send_data1 = send_data1.replace("vv", str(vv))
    send_data1 = send_data1.replace("tt", str(tt))
    send_data1 = send_data1.replace("radius", str(radius))
    # print(send_data1)
    tcp_socket.send(send_data1.encode('utf8'))



