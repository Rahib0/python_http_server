from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler

class NeuralHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()


        self.wfile.write(bytes("<html<body><h1>This is a simple python http server!</h1></body></html>", "utf-8"))



def run(server_class=HTTPServer, handler_class=NeuralHTTP):

    server_address = ("0.0.0.0", 8000)
    httpd = server_class(server_address, handler_class)
    print("Launching server...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()