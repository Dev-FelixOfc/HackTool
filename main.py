import os
import subprocess
import time
from colorama import Fore, Style, init

init(autoreset=True)

def limpiar():
    os.system('clear')

def banner():
    limpiar()
    print(f"{Fore.CYAN}{Style.BRIGHT}=========================================")
    print(f"{Fore.GREEN}{Style.BRIGHT}        BIENVENIDO AL PROYECTO")
    print(f"{Fore.WHITE}{Style.BRIGHT}               HacksTool")
    print(f"{Fore.CYAN}{Style.BRIGHT}=========================================")
    print(f"{Fore.YELLOW}     Desarrollado por: Dev-FelixOfc")
    print(f"{Fore.CYAN}-----------------------------------------")

def menu():
    banner()
    print(f"{Fore.WHITE}[01] {Fore.GREEN}Obtener información de dominio")
    print(f"{Fore.WHITE}[02] {Fore.GREEN}Obtener información de IP")
    print(f"{Fore.WHITE}[03] {Fore.GREEN}Escaneo de puertos")
    print(f"{Fore.WHITE}[04] {Fore.GREEN}Ataque de fuerza bruta (Simulado)")
    print(f"{Fore.WHITE}[00] {Fore.RED}Salir")
    print("\n")
    
    opcion = input(f"{Fore.CYAN}HacksTool > {Fore.WHITE}")

    if opcion == "01" or opcion == "1":
        subprocess.run(["python", "src/domain.py"])
    elif opcion == "02" or opcion == "2":
        subprocess.run(["python", "src/ip.py"])
    elif opcion == "03" or opcion == "3":
        subprocess.run(["python", "src/ports.py"])
    elif opcion == "04" or opcion == "4":
        subprocess.run(["python", "src/attack.py"])
    elif opcion == "00" or opcion == "0":
        print(f"{Fore.RED}Saliendo del panel...")
        exit()
    else:
        print(f"{Fore.RED}Opción no válida.")
        time.sleep(1)
        menu()

if __name__ == "__main__":
    menu()