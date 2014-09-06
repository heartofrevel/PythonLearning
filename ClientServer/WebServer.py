import SocketServer
import SimpleHTTPServer





class HTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/admin':
			self.wfile.write('Forbidden \n')
			self.wfile.write(self.headers)
		else :
			SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


httpServer = SocketServer.TCPServer(('', 10000), HTTPHandler)
httpServer.serve_forever()