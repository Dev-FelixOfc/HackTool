#!/bin/bash

clear
echo "-------------------------------------------------------"
echo "   Siganme en GitHub: https://github.com/Dev-FelixOfc   "
echo "              Proyecto: HacksTool                      "
echo "-------------------------------------------------------"

pkg install python -y > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1

chmod +x main.py

python main.py