#/usr/bin/python

import socket
import os
import struct
import binascii

def analyze_ether_header(data):
    ip_bool = False
    eth_hdr = struct.unpack("!6s6sH", data[:14]) #ipv4 = 0x0800
    dest_mac = binascii.hexlify(eth_hdr[0])
    src_mac = binascii.hexlify(eth_hdr[1])
    proto = eth_hdr[2]
    
    if hex(proto) == 0x0800:
        ip_bool = True
    
    print (dest_mac)
    print (src_mac)
    print hex(proto)
    data = data[14:]
    return data, ip_bool

def analyze_ip_header(data):
    ip_hdr = struct.unpack("!5H4s4s", data[:20])
    ver = ip_hdr[0] >> 12
    ihl = (ip_hdr[0] >> 8) & 0x0f
    tos = ip_hdr[0] & 0x00ff
    tot_len = ip_hdr[1]
    ip_id = ip_hdr[2]
    flag = ip_hdr[3] >> 13
    frag = ip_hdr[3] & 0x1fff
    ip_tty = ip_hdr[4] >> 8
    ip_proto = ip_hdr[4] & 0x00ff
    chk_sum = ip_hdr[5]
    src_add = socket.ntoa(ip_hdr[6])
    dest_add = socket.ntoa(ip_hdr[7])
    data = data[:20]
    return data, ip_proto
    

def main():
    sniffer_socket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
    recv_data = sniffer_socket.recv(2048)
    os.system('clear')
    
    data, ip_bool = analyze_ether_header(recv_data)
    
main()