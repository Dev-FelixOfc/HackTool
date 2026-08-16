#!/bin/bash

clear
echo "-------------------------------------------------------"
echo "   Siganme en GitHub: https://github.com/Dev-FelixOfc   "
echo "              Proyecto: HacksTool                      "
echo "-------------------------------------------------------"

# Verificar si node está instalado
if ! command -v node &> /dev/null; then
    echo "Node.js no está instalado. Instalando..."
    apt update
    apt install nodejs npm -y
fi

# Instalar dependencias de Node.js
echo "Instalando dependencias de Node.js..."
npm install axios

# Verificar si python3 está instalado
if ! command -v python3 &> /dev/null; then
    echo "Python3 no está instalado. Instalando..."
    apt install python3 python3-pip -y
fi

# Instalar dependencias de Python
echo "Instalando dependencias de Python..."
pip3 install -r requirements.txt

# Dar permisos de ejecución
chmod +x main.py

# Ejecutar el script JavaScript principal
echo "Ejecutando HacksTool..."
node main.js