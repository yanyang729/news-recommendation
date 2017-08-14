"""Backend service"""

import pyjsonrpc

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    """RPC requst handler"""
    @pyjsonrpc.rpcmethod
    def add(self, num1, num2): # pylint: disable=no-self-use
        """ Test method"""
        print " add is called with %d and %s" % (num1, num2)
        return num1 + num2


HTTP_SERVER = pyjsonrpc.ThreadingHttpServer(
    server_address=(SERVER_HOST,SERVER_PORT),
    RequestHandlerClass=RequestHandler
)

print "Starting HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT)

HTTP_SERVER.serve_forever()
