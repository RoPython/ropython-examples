#! /usr/bin/env python


import cherrypy

from myserver.config import HOST, PORT, LOG


class Server(object):

    @cherrypy.expose
    def index(self):
        return "RoPython"


def start_server(host=HOST, port=PORT, log=LOG):
    """Start web server and mount rest api"""

    cherrypy.config.update({
        "server.socket_host": host,
        "server.socket_port": port,
        # configurari aditionale
        #"log.error_file": log,
        #"request.show_tracebacks": False,
        #"environment": "production"
    })

    # pornim server-ul folosind clasa principala
    cherrypy.quickstart(Server())


if __name__ == "__main__":
    start_server()
