from http.server import BaseHTTPRequestHandler, HTTPServer


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Simple Server</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is Yang's Mac Mini.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer(('0.0.0.0', 69), MyServer)
    print("Yang's local server started at port 69")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
