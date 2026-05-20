import os
import time
import random
import sys
import requests
from colorama import Fore, Style, init

init(autoreset=True)

def limpiar():
    os.system('clear' if os.name == 'posix' else 'cls')

def animacion_hacker(duracion):
    inicio = time.time()
    caracteres = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZコンテンツデータ#$@&%*"
    try:
        columnas = os.get_terminal_size().columns
    except OSError:
        columnas = 60

    while time.time() - inicio < duracion:
        linea = ""
        for _ in range(columnas):
            if random.random() > 0.85:
                linea += random.choice(caracteres)
            else:
                linea += " "
        sys.stdout.write(f"\r{Fore.GREEN}{linea}")
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n")

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