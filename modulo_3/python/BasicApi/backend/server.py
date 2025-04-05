import http.server
import socketserver
import json
import random
with open("./data/frases.json", "r", encoding="utf-8") as file:
  frases = json.load(file)

PORT = 3000

class basicApiHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/frase":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")  # Para permitir peticiones desde el navegador
            self.end_headers()
            respuesta = random.choice(frases)
            self.wfile.write(json.dumps(respuesta).encode())
        elif self.path == "/api/frases":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            respuesta = {"frases": frases}
            self.wfile.write(json.dumps(respuesta).encode())
        elif self.path.startswith("/api/frase/"):
            frase_id = self.path.split("/")[-1]
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            try:
                print("frase_id", frase_id)
                frase = frases[int(frase_id) - 1]
                respuesta = {"frase": frase}
                self.wfile.write(json.dumps(respuesta).encode())
            except (IndexError, ValueError):
                self.send_error(404, "Frase no encontrada")
        else:
            self.send_error(404, "Ruta no encontrada")

with socketserver.TCPServer(("", PORT), basicApiHandler) as httpd:
    print(f"Servidor corriendo en http://localhost:{PORT}")
    httpd.serve_forever()