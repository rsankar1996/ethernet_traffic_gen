# Simple ethernet packet generator using scapy tool

from scapy.all import *
import sys
import string
import random

if os.geteuid() != 0:
    exit ("You must be root!!! exiting.")

n = len(sys.argv)

src_ip = sys.argv[1]
dst_ip = sys.argv[2]
proto = sys.argv[3]
iface = sys.argv[4]
length = int(sys.argv[5])
count = int(sys.argv[6])

l2 = Ether()
l3 = IP()

def gen_l2():
    if n >= 8:
        l2.dst = sys.argv[7]

def gen_l3():
    l3.src = src_ip
    l3.dst = dst_ip

def gen_l4():
    global l4
    if proto == "udp":
        l4 = UDP()
    elif proto == "icmp":
        l4 = ICMP()
    elif proto == "tcp":
        l4 = TCP()
    else:
        exit ("Invalid protocol mentioned!!! exiting.")

def gen_data():
    data = ''.join(random.choices(string.ascii_letters, k=length))
    return data

if n >= 7:
    gen_l2()
    gen_l3()
    gen_l4()
    data = gen_data()

    sendp(l2/l3/l4/data, iface=iface, count=count)
else:
    exit ("oops")
