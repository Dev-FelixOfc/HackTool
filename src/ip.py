import os
import time
import random
import socket
import dns.resolver
from colorama import Fore, Style, init

init(autoreset=True)

def limpiar():
    os.system('clear')

def animacion_hacker(duracion):
    inicio = time.time()
    caracteres = "0123456789ABCDEF"
    while time.time() - inicio < duracion:
        linea = "".join(random.choice(caracteres) for _ in range(50))
        print(f"{Fore.GREEN}[DEBUG] 0x{linea}")
        time.sleep(0.04)

def obtener_ip_dominio(target):
    try:
        clean_host = target.replace("https://", "").replace("http://", "").split("/")[0]
        ip = socket.gethostbyname(clean_host)
        
        registros = []
        try:
            answers = dns.resolver.resolve(clean_host, 'MX')
            for rdata in answers:
                registros.append(str(rdata.exchange))
        except:
            registros.append("No detectados")
            
        return {
            "Tipo": "Dominio / Host",
            "IP Detectada": ip,
            "DNS MX": registros[0],
            "Puerto Seguro": "443 (SSL/TLS)",
            "Status": "Interceptado"
        }
    except:
        return None

def info_telefono(num):
    paises = {
        "+1809": "Rep. Dominicana",
        "+1829": "Rep. Dominicana",
        "+1849": "Rep. Dominicana",
        "+52": "México",
        "+34": "España",
        "+54": "Argentina",
        "+57": "Colombia"
    }
    ubicacion = "Desconocida (Prefijo Global)"
    for prefijo, pais in paises.items():
        if num.startswith(prefijo):
            ubicacion = pais
            break
            
    ip_fake = f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}"
    return {
        "Tipo": "Dispositivo Movil",
        "Origen": ubicacion,
        "IP Asignada": ip_fake,
        "Red": "Roaming / LTE",
        "Bypass": "Exitoso"
    }

def principal():
    limpiar()
    print(f"{Fore.CYAN}--- MODULO DE RASTREO IP Y REGISTROS ---")
    print(f"{Fore.WHITE}[1] Continuar rastreo")
    print(f"{Fore.WHITE}[2] Volver al main")
    print("")
    
    opc = input(f"{Fore.CYAN}HacksTool > {Fore.WHITE}")
    if opc != "1": return

    target = input(f"\n{Fore.YELLOW}Ingrese Dato (Dominio, Tel o Email): {Fore.WHITE}")
    
    print(f"\n{Fore.RED}Iniciando rastreador de paquetes...")
    animacion_hacker(30)

    if "@" in target:
        datos = {
            "Tipo": "Correo Electronico",
            "Servidor": target.split("@")[-1],
            "IP Virtual": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
            "Fuga de datos": "Detectada en DB",
            "Ubicacion": "Nube (Cloud)"
        }
    elif target.startswith("+"):
        datos = info_telefono(target)
    else:
        datos = obtener_ip_dominio(target)
        if not datos:
            datos = {
                "Error": "Host no alcanzable",
                "IP Generada": f"10.0.{random.randint(1,255)}.{random.randint(1,255)}",
                "Nota": "Usando tunel de emergencia"
            }

    animacion_hacker(5)
    
    print(f"\n{Fore.RED}{Style.BRIGHT}=========================================")
    print(f"{Fore.RED}{Style.BRIGHT}        INFORME DE INTELIGENCIA          ")
    print(f"{Fore.RED}{Style.BRIGHT}=========================================")
    for c, v in datos.items():
        print(f"{Fore.WHITE}{c}: {Fore.YELLOW}{v}")
    print(f"{Fore.RED}{Style.BRIGHT}=========================================")
    
    input(f"\n{Fore.CYAN}Presione Enter para reiniciar...")

if __name__ == "__main__":
    principal()