const http = require("node:http");

const server = http.createServer((req, res) => {
  res.setHeader("Content-Type", "text/html");
  res.setHeader("X-Powered-By", "Node.js");

  if (req.url === "/" && req.method === "GET") {
    res.statusCode = 200;
    res.end("<h1>Hola este es mi portafolio</h1>");
  } else if (req.url === "/portafolio" && req.method === "GET") {
    res.statusCode = 200;
    res.end("<h1>Estos son mis proyectos</h1>");
  } else if (req.url === "/contacto" && req.method === "GET") {
    res.statusCode = 200;
    res.end("<h1>Estos son mis datos de contacto</h1>");
  } else {
    res.statusCode = 404;
    res.end("<h1>Pagina no encontrada</h1>");
  }
});

server.listen(9000, () => {
  console.log("Servidor corriendo en http://localhost:9000");
});
