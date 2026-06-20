import http.server
import socketserver
PORT=8080
Handler=http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("",PORT),Handler)as httpd:
    print(f"Servidor Tienda 3D en http://localhost:{PORT}")
    print("Presiona Ctrl+C para detener")
    httpd.serve_forever()
