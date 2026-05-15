import os
import time
import random
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def limpiar():
    os.system('clear')

def animacion_ataque(texto, duracion, color):
    inicio = time.time()
    while time.time() - inicio < duracion:
        puntos = "." * random.randint(1, 3)
        print(f"{color}[STRESS] {texto}{puntos} Payload: {random.getrandbits(32)}")
        time.sleep(0.1)

def principal():
    limpiar()
    print(f"{Fore.CYAN}--- MODULO DE STRESS-TEST & EXPLOIT V3 ---")
    print(f"{Fore.WHITE}[1] Iniciar secuencia de ataque simulado")
    print(f"{Fore.WHITE}[2] Volver al menu")
    print("")
    
    opc = input(f"{Fore.CYAN}HacksTool > {Fore.WHITE}")
    if opc != "1": return

    target = input(f"\n{Fore.YELLOW}Ingrese la URL objetivo: {Fore.WHITE}")
    if not target.startswith("http"):
        target = "https://" + target

    print(f"\n{Fore.MAGENTA}Iniciando Scraper de reconocimiento...")
    try:
        # Simula la entrada al sitio
        requests.get(target, timeout=5)
        print(f"{Fore.GREEN}[OK] Conexion establecida. Creando sesion fantasma...")
        time.sleep(2)
    except:
        print(f"{Fore.RED}[ERROR] No se pudo conectar al sitio.")
        return

    # Fases del ataque simulado
    print(f"\n{Fore.RED}Lanzando Ataque 1: Inyeccion de Headers")
    animacion_ataque("Enviando paquetes TCP/UDP", 10, Fore.RED)
    
    print(f"\n{Fore.YELLOW}Lanzando Ataque 2: Bypass de Formulario")
    animacion_ataque("Probando exploits de sesion", 10, Fore.YELLOW)
    
    print(f"\n{Fore.RED}Lanzando Ataque 3: Stress de CPU")
    animacion_ataque("Sobrecargando peticiones GET", 10, Fore.RED)

    print(f"\n{Fore.CYAN}Analizando integridad del Firewall...")
    time.sleep(3)

    print(f"\n{Fore.RED}{Style.BRIGHT}=========================================")
    print(f"{Fore.RED}{Style.BRIGHT}           REPORTE FINAL                ")
    print(f"{Fore.RED}{Style.BRIGHT}=========================================")
    print(f"{Fore.WHITE}Objetivo: {Fore.YELLOW}{target}")
    print(f"{Fore.WHITE}Estado: {Fore.GREEN}EXITO PARCIAL")
    print(f"{Fore.WHITE}Seguridad: {Fore.YELLOW}Bajo de 10/10 a 7/10")
    print(f"{Fore.WHITE}Resultado: {Fore.WHITE}El sitio resistio el desbordamiento.")
    print(f"{Fore.WHITE}Nota: {Fore.RED}Firewall adaptativo detectado.")
    print(f"{Fore.RED}{Style.BRIGHT}=========================================")
    
    input(f"\n{Fore.CYAN}Presione Enter para cerrar la sesion...")

if __name__ == "__main__":
    principal()