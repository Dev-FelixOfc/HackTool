import os
import time
import random
import sys
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def limpiar():
    os.system('clear')

def animacion_hacker(duracion):
    inicio = time.time()
    caracteres = "0123456789ABCDEFHIJKLMNOPQRSTUVWXYZ#$@&%*"
    while time.time() - inicio < duracion:
        linea = "".join(random.choice(caracteres) for _ in range(60))
        print(f"{Fore.GREEN}{linea}")
        time.sleep(0.05)

def obtener_info(url):
    try:
        if not url.startswith("http"):
            url = "https://" + url
        
        dominio = url.split("//")[-1].split("/")[0]
        response = requests.get(url, timeout=10)
        headers = response.headers
        
        info = {
            "Dominio": dominio,
            "Estado": "Activo (200 OK)" if response.status_code == 200 else f"Status: {response.status_code}",
            "Servidor": headers.get("Server", "Protegido/Oculto"),
            "Content-Type": headers.get("Content-Type", "Desconocido"),
            "X-Powered-By": headers.get("X-Powered-By", "No detectado"),
            "Cache-Control": headers.get("Cache-Control", "N/A"),
            "Seguridad": "HSTS Activado" if "Strict-Transport-Security" in headers else "HSTS No detectado"
        }
        return info
    except Exception as e:
        return {"Error": "No se pudo conectar con el host remoto."}

def principal():
    limpiar()
    print(f"{Fore.CYAN}--- MODULO DE ANALISIS DE DOMINIO ---")
    print(f"{Fore.WHITE}[1] Continuar con el proceso")
    print(f"{Fore.WHITE}[2] Salir al menu principal")
    print("")
    
    opc = input(f"{Fore.CYAN}HacksTool > {Fore.WHITE}")
    
    if opc == "2":
        return
    
    if opc == "1":
        target = input(f"\n{Fore.YELLOW}Ingrese el dominio (ej: https://google.com): {Fore.WHITE}")
        
        print(f"\n{Fore.MAGENTA}Iniciando secuencia de bypass y extraccion...")
        time.sleep(1)
        
        animacion_hacker(30)
        
        datos = obtener_info(target)
        
        animacion_hacker(5)
        
        print(f"\n{Fore.RED}{Style.BRIGHT}=========================================")
        print(f"{Fore.RED}{Style.BRIGHT}      RESULTADOS DE LA INFILTRACION      ")
        print(f"{Fore.RED}{Style.BRIGHT}=========================================")
        for clave, valor in datos.items():
            print(f"{Fore.WHITE}{clave}: {Fore.YELLOW}{valor}")
        print(f"{Fore.RED}{Style.BRIGHT}=========================================")
        
        input(f"\n{Fore.CYAN}Presione Enter para volver...")

if __name__ == "__main__":
    principal()