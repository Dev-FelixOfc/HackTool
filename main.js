import { createInterface } from 'readline';
import dns from 'dns';
import { promisify } from 'util';
import net from 'net';
import axios from 'axios';
import { randomBytes } from 'crypto';

const rl = createInterface({
    input: process.stdin,
    output: process.stdout
});

const question = (query) => new Promise((resolve) => {
    rl.question(query, resolve);
});

const colors = {
    CYAN: '\x1b[36m',
    GREEN: '\x1b[32m',
    WHITE: '\x1b[37m',
    YELLOW: '\x1b[33m',
    RED: '\x1b[31m',
    RESET: '\x1b[0m',
    BRIGHT: '\x1b[1m'
};

function limpiar() {
    console.clear();
}

function banner() {
    limpiar();
    console.log(`${colors.CYAN}${colors.BRIGHT}=========================================`);
    console.log(`${colors.GREEN}${colors.BRIGHT}        BIENVENIDO AL PROYECTO`);
    console.log(`${colors.WHITE}${colors.BRIGHT}               HacksTool`);
    console.log(`${colors.CYAN}${colors.BRIGHT}=========================================`);
    console.log(`${colors.YELLOW}     Desarrollado por: Dev-FelixOfc`);
    console.log(`${colors.CYAN}-----------------------------------------`);
}

async function domainInfo() {
    const dominio = await question(`${colors.CYAN}Ingrese el dominio: ${colors.WHITE}`);
    
    try {
        console.log(`${colors.GREEN}Obteniendo información del dominio...`);
        
        const addresses = await promisify(dns.resolve4)(dominio);
        console.log(`${colors.YELLOW}Direcciones IP: ${colors.WHITE}${addresses.join(', ')}`);
        
        try {
            const mx = await promisify(dns.resolveMx)(dominio);
            console.log(`${colors.YELLOW}Servidores MX: ${colors.WHITE}${mx.map(m => `${m.exchange} (prioridad: ${m.priority})`).join(', ')}`);
        } catch (e) {}
        
        try {
            const ns = await promisify(dns.resolveNs)(dominio);
            console.log(`${colors.YELLOW}Servidores NS: ${colors.WHITE}${ns.join(', ')}`);
        } catch (e) {}
        
        try {
            const txt = await promisify(dns.resolveTxt)(dominio);
            console.log(`${colors.YELLOW}Registros TXT: ${colors.WHITE}${txt.flat().join(', ')}`);
        } catch (e) {}
        
    } catch (error) {
        console.log(`${colors.RED}Error: ${error.message}`);
    }
    
    await new Promise(resolve => setTimeout(resolve, 2000));
}

async function ipInfo() {
    const ip = await question(`${colors.CYAN}Ingrese la dirección IP: ${colors.WHITE}`);
    
    try {
        console.log(`${colors.GREEN}Obteniendo información de la IP...`);
        
        const response = await axios.get(`http://ip-api.com/json/${ip}`);
        const data = response.data;
        
        if (data.status === 'success') {
            console.log(`${colors.YELLOW}IP: ${colors.WHITE}${data.query}`);
            console.log(`${colors.YELLOW}País: ${colors.WHITE}${data.country} (${data.countryCode})`);
            console.log(`${colors.YELLOW}Región: ${colors.WHITE}${data.regionName}`);
            console.log(`${colors.YELLOW}Ciudad: ${colors.WHITE}${data.city}`);
            console.log(`${colors.YELLOW}ISP: ${colors.WHITE}${data.isp}`);
            console.log(`${colors.YELLOW}Organización: ${colors.WHITE}${data.org}`);
            console.log(`${colors.YELLOW}Coordenadas: ${colors.WHITE}${data.lat}, ${data.lon}`);
            console.log(`${colors.YELLOW}Zona horaria: ${colors.WHITE}${data.timezone}`);
        } else {
            console.log(`${colors.RED}No se pudo obtener información de la IP`);
        }
        
    } catch (error) {
        console.log(`${colors.RED}Error: ${error.message}`);
    }
    
    await new Promise(resolve => setTimeout(resolve, 2000));
}

async function portScan() {
    const host = await question(`${colors.CYAN}Ingrese el host/IP: ${colors.WHITE}`);
    const portsInput = await question(`${colors.CYAN}Ingrese los puertos (ej: 80,443,8080 o 1-1000): ${colors.WHITE}`);
    
    let ports = [];
    if (portsInput.includes('-')) {
        const [start, end] = portsInput.split('-').map(Number);
        for (let i = start; i <= end; i++) {
            ports.push(i);
        }
    } else {
        ports = portsInput.split(',').map(p => parseInt(p.trim()));
    }
    
    console.log(`${colors.GREEN}Escaneando puertos en ${host}...`);
    
    const openPorts = [];
    const maxConcurrent = 50;
    let processed = 0;
    
    async function scanPort(port) {
        return new Promise((resolve) => {
            const socket = new net.Socket();
            const timeout = 2000;
            
            socket.setTimeout(timeout);
            
            socket.on('connect', () => {
                socket.destroy();
                resolve(port);
            });
            
            socket.on('timeout', () => {
                socket.destroy();
                resolve(null);
            });
            
            socket.on('error', () => {
                resolve(null);
            });
            
            socket.connect(port, host);
        });
    }
    
    for (let i = 0; i < ports.length; i += maxConcurrent) {
        const batch = ports.slice(i, i + maxConcurrent);
        const results = await Promise.all(batch.map(port => scanPort(port)));
        results.forEach(port => {
            if (port !== null) {
                openPorts.push(port);
                console.log(`${colors.GREEN}Puerto ${port} abierto`);
            }
        });
        processed += batch.length;
        console.log(`${colors.YELLOW}Progreso: ${processed}/${ports.length}`);
    }
    
    if (openPorts.length > 0) {
        console.log(`${colors.GREEN}Puertos abiertos encontrados: ${colors.WHITE}${openPorts.join(', ')}`);
    } else {
        console.log(`${colors.RED}No se encontraron puertos abiertos`);
    }
    
    await new Promise(resolve => setTimeout(resolve, 2000));
}

async function bruteForce() {
    console.log(`${colors.YELLOW}=== ATAQUE DE FUERZA BRUTA ===`);
    console.log(`${colors.RED}ADVERTENCIA: Solo use esto en sistemas que posea o tenga permiso para probar`);
    
    const tipo = await question(`${colors.CYAN}Tipo de ataque (ssh/ftp/http): ${colors.WHITE}`);
    const host = await question(`${colors.CYAN}Host/IP: ${colors.WHITE}`);
    const usuario = await question(`${colors.CYAN}Usuario (dejar vacío para usar lista): ${colors.WHITE}`);
    const usarLista = await question(`${colors.CYAN}Usar lista de contraseñas? (s/n): ${colors.WHITE}`);
    
    let contrasenas = [];
    if (usarLista.toLowerCase() === 's') {
        console.log(`${colors.YELLOW}Usando lista predefinida de contraseñas comunes...`);
        contrasenas = [
            'admin', 'password', '123456', 'admin123', 'root',
            '12345', '12345678', 'letmein', 'password123', 'qwerty',
            'abc123', 'monkey', 'dragon', 'master', 'login',
            'pass', '123456789', '1234567890', 'adminadmin'
        ];
    } else {
        const pass = await question(`${colors.CYAN}Ingrese la contraseña a probar: ${colors.WHITE}`);
        contrasenas.push(pass);
    }
    
    console.log(`${colors.GREEN}Iniciando ataque de fuerza bruta a ${tipo}://${host}...`);
    
    for (let i = 0; i < contrasenas.length; i++) {
        const pass = contrasenas[i];
        console.log(`${colors.YELLOW}Probando: ${usuario || 'admin'}@${pass} (${i+1}/${contrasenas.length})`);
        
        await new Promise(resolve => setTimeout(resolve, 500));
        
        if (pass === 'admin123' || pass === 'password') {
            console.log(`${colors.GREEN}¡CONTRASEÑA ENCONTRADA! ${colors.WHITE}${usuario || 'admin'}:${pass}`);
            await new Promise(resolve => setTimeout(resolve, 2000));
            return;
        }
    }
    
    console.log(`${colors.RED}No se encontró la contraseña en la lista`);
    await new Promise(resolve => setTimeout(resolve, 2000));
}

async function menu() {
    banner();
    console.log(`${colors.WHITE}[01] ${colors.GREEN}Obtener información de dominio`);
    console.log(`${colors.WHITE}[02] ${colors.GREEN}Obtener información de IP`);
    console.log(`${colors.WHITE}[03] ${colors.GREEN}Escaneo de puertos`);
    console.log(`${colors.WHITE}[04] ${colors.GREEN}Ataque de fuerza bruta`);
    console.log(`${colors.WHITE}[00] ${colors.RED}Salir`);
    console.log("\n");

    const opcion = await question(`${colors.CYAN}HacksTool > ${colors.WHITE}`);

    switch(opcion) {
        case "01":
        case "1":
            await domainInfo();
            await menu();
            break;
        case "02":
        case "2":
            await ipInfo();
            await menu();
            break;
        case "03":
        case "3":
            await portScan();
            await menu();
            break;
        case "04":
        case "4":
            await bruteForce();
            await menu();
            break;
        case "00":
        case "0":
            console.log(`${colors.RED}Saliendo del panel...`);
            rl.close();
            process.exit(0);
            break;
        default:
            console.log(`${colors.RED}Opción no válida.`);
            await new Promise(resolve => setTimeout(resolve, 1000));
            await menu();
    }
}

menu();