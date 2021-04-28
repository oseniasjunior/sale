from argparse import ArgumentParser

import cherrypy

from sale import settings, wsgi


class DjangoApplication:
    def __init__(self, port: int, certfile: str, keyfile: str):
        self.port = port
        self.certfile = certfile
        self.keyfile = keyfile

    @staticmethod
    def make_config():
        config = {
            'tools.staticdir.on': False,
            'tools.expires.on': True,
            'tools.expires.secs': 86400,
            'tools.staticdir.dir': settings.STATIC_ROOT,
            'engine.autoreload.on': False,
            'log.screen': True,
        }

        cherrypy.tree.mount(None, script_name=settings.STATIC_URL, config={'/': config})

    def get_server_str(self):
        if not self.certfile or not self.keyfile:
            return 'tcp:%d' % self.port
        return 'ssl:%d:certKey=%s:privateKey=%s' % (self.port, self.certfile, self.keyfile)

    def run_server(self):
        # import libs
        from twisted.internet import endpoints
        from twisted.internet import reactor
        from twisted.internet import task
        from twisted.web import server
        from twisted.web.wsgi import WSGIResource

        # create default configuration
        self.make_config()

        # We will be using Twisted HTTP server so let's
        # disable the CherryPy's HTTP server entirely
        cherrypy.server.unsubscribe()

        # Publish periodically onto the 'main' channel as the bus mainloop would do
        task.LoopingCall(lambda: cherrypy.engine.publish('main')).start(0.1)

        # create SSL server from string
        https_server = endpoints.serverFromString(reactor, self.get_server_str())

        # Tie our app to Twisted
        reactor.addSystemEventTrigger('after', 'startup', cherrypy.engine.start)
        reactor.addSystemEventTrigger('before', 'shutdown', cherrypy.engine.exit)
        resource = WSGIResource(reactor, reactor.getThreadPool(), wsgi.application)
        site = server.Site(resource)
        https_server.listen(site)
        reactor.run()


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--port', type=int, action='store', dest='port', help='Port to attach server')
    parser.add_argument('--certfile', type=str, action='store', dest='certfile',
                        help='SSL certificate to attach server')
    parser.add_argument('--keyfile', type=str, action='store', dest='keyfile',
                        help='SSL private key to to attach server')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()

    print("Your app is running at 0.0.0.0:%s" % args.port)
    app = DjangoApplication(port=args.port, certfile=args.certfile, keyfile=args.keyfile)
    app.run_server()
