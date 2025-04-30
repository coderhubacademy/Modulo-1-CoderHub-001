const os = require("node:os");

console.log("Sistema Operativo: ", os.platform());
console.log("Version del SO: ", os.release());
console.log("Arquitectura del SO: ", os.arch());
console.log("Nombre del Host: ", os.hostname());
console.log("Directorio de Inicio: ", os.homedir());
console.log("Memoria Total: ", os.totalmem());
console.log("Memoria Libre: ", os.freemem());
console.log("Memoria Usada: ", os.totalmem() - os.freemem());
console.log("CPU: ", os.cpus());
console.log("Carga Promedio: ", os.loadavg());
