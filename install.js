import { execSync } from 'child_process';
import fs from 'fs';

console.log("-------------------------------------------------------");
console.log("   Siganme en GitHub: https://github.com/Dev-FelixOfc   ");
console.log("              Proyecto: HacksTool                      ");
console.log("-------------------------------------------------------");

try {
    console.log("Instalando dependencias...");
    execSync('pkg install python -y', { stdio: 'inherit' });
    execSync('pip install -r requirements.txt', { stdio: 'inherit' });
    
    fs.chmodSync('main.py', 0o755);
    
    console.log("Ejecutando main.py...");
    execSync('python main.py', { stdio: 'inherit' });
    
} catch (error) {
    console.error("Error:", error.message);
    process.exit(1);
}