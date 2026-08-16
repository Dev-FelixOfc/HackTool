import { exec } from 'child_process';
import { promisify } from 'util';
import readline from 'readline';

const execAsync = promisify(exec);

const rl = readline.createInterface({
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

async function menu() {
    banner();
    console.log(`${colors.WHITE}[01] ${colors.GREEN}Obtener información de dominio`);
    console.log(`${colors.WHITE}[02] ${colors.GREEN}Obtener información de IP`);
    console.log(`${colors.WHITE}[03] ${colors.GREEN}Escaneo de puertos`);
    console.log(`${colors.WHITE}[04] ${colors.GREEN}Ataque de fuerza bruta`);
    console.log(`${colors.WHITE}[00] ${colors.RED}Salir`);
    console.log("\n");

    const opcion = await question(`${colors.CYAN}HacksTool > ${colors.WHITE}`);

    try {
        if (opcion === "01" || opcion === "1") {
            await execAsync("python src/domain.py");
        } else if (opcion === "02" || opcion === "2") {
            await execAsync("python src/ip.py");
        } else if (opcion === "03" || opcion === "3") {
            await execAsync("python src/ports.py");
        } else if (opcion === "04" || opcion === "4") {
            await execAsync("python src/attack.py");
        } else if (opcion === "00" || opcion === "0") {
            console.log(`${colors.RED}Saliendo del panel...`);
            rl.close();
            process.exit(0);
        } else {
            console.log(`${colors.RED}Opción no válida.`);
            await new Promise(resolve => setTimeout(resolve, 1000));
            await menu();
        }
    } catch (error) {
        console.error(`${colors.RED}Error al ejecutar el comando: ${error.message}`);
        await new Promise(resolve => setTimeout(resolve, 1000));
        await menu();
    }
}

menu();