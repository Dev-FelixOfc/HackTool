import os
import time
import random
import socket
from colorama import Fore, Style, init

init(autoreset=True)

def limpiar():
    os.system('clear')

def animacion_hacker(duracion):
    inicio = time.time()
    caracteres = "0123456789ABCDEF"
    while time.time() - inicio < duracion:
        hex_val = "".join(random.choice(caracteres) for _ in range(8))
        addr = "".join(random.choice(caracteres) for _ in range(4))
        print(f"{Fore.GREEN}SCANNING OFFSET 0x{hex_val} AT ADDR 0x{addr}...")
        time.sleep(0.06)

def escanear_puertos(target):
    puertos_comunes = {
        21: "FTP (Transferencia de archivos)",
        22: "SSH (Acceso remoto)",
        23: "Telnet",
        25: "SMTP (Correo)",
        53: "DNS (Resolución de nombres)",
        80: "HTTP (Web sin seguridad)",
        110: "POP3",
        443: "HTTPS (Web segura)",
        3306: "MySQL (Base de datos)",
        8080: "Proxy/Alternativo"
    }
    
    resultados = []
    
    try:
        ip_objetivo = socket.gethostbyname(target)
    except:
        return None

    for puerto, servicio in puertos_comunes.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        resultado = sock.connect_ex((ip_objetivo, puerto))
        if resultado == 0:
            resultados.append(f"Puerto {puerto} [{servicio}]: ABIERTO")
        sock.close()
        
    return resultados

def principal():
    limpiar()
    print(f"{Fore.CYAN}--- MODULO DE ESCANEO DE PUERTOS V1.0 ---")
    print(f"{Fore.WHITE}[1] Iniciar escaneo de vulnerabilidades")
    print(f"{Fore.WHITE}[2] Regresar al panel de control")
    print("")
    
    opc = input(f"{Fore.CYAN}HacksTool > {Fore.WHITE}")
    if opc != "1": return

    target = input(f"\n{Fore.YELLOW}Ingrese IP o Dominio objetivo: {Fore.WHITE}")
    target = target.replace("https://", "").replace("http://", "").split("/")[0]
    
    print(f"\n{Fore.RED}Estableciendo conexion con los sockets...")
    animacion_hacker(30)
    
    hallazgos = escanear_puertos(target)
    
    animacion_hacker(5)
    
    print(f"\n{Fore.RED}{Style.BRIGHT}=========================================")
    print(f"{Fore.RED}{Style.BRIGHT}        PUERTOS DETECTADOS EN RED        ")
    print(f"{Fore.RED}{Style.BRIGHT}=========================================")
    
    if hallazgos:
        for h in hallazgos:
            print(f"{Fore.GREEN}[+] {h}")
    else:
        print(f"{Fore.WHITE}No se encontraron puertos publicos abiertos.")
        print(f"{Fore.YELLOW}Nota: El host podria tener un Firewall activo.")
        
    print(f"{Fore.RED}{Style.BRIGHT}=========================================")
    
    input(f"\n{Fore.CYAN}Analisis completado. Presione Enter...")

if __name__ == "__main__":
    principal()