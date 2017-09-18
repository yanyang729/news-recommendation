"""Backend service"""

import pyjsonrpc
import operations
import os
import json

with open(os.path.join(os.path.dirname(__file__),'..','config','backend_server_config.json')) as f:
    config = json.load(f)['server']

SERVER_HOST = config['SERVER_HOST']
SERVER_PORT = config['SERVER_PORT']

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    """RPC requst handler"""
    @pyjsonrpc.rpcmethod
    def add(self, num1, num2): # pylint: disable=no-self-use
        """ Test method"""
        print " add is called with %d and %s" % (num1, num2)
        return num1 + num2

    @pyjsonrpc.rpcmethod
    def getNewsSummariesForUser(self, user_id, page_num):
        return operations.getNewsSummariesForUser(user_id, page_num)

    @pyjsonrpc.rpcmethod
    def logNewsClickForUser(self, user_id, news_id):
        return operations.logNewsClickForUser(user_id, news_id)


HTTP_SERVER = pyjsonrpc.ThreadingHttpServer(
    server_address=(SERVER_HOST,SERVER_PORT),
    RequestHandlerClass=RequestHandler
)

print "Starting HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT)

HTTP_SERVER.serve_forever()
