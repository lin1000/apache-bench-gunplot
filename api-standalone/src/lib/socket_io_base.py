# -*- coding: utf-8 -*-
"""

.. module:: socket_io_base
   :synopsis: A reusable module for providing socketio capability to service implementation
.. moduleauthor:: Tony Lin

"""

from flask import Flask
from flask_socketio import SocketIO 
from lib.flask_base import FlaskBase
import logging

class SocketIOBase(FlaskBase):
    """This is a Base Class with SocketIO Capability to serve clients from browser.

    .. note::
        This is a base class provide flask and socketio capability. Services could inherit this base class and
        provide their own app.route or socket.on to react to events and traffics dynamically.

    .. warning::

        For dockerized deployment, listening on `host` 0.0.0.0 is suggested.

    :param host: Hostname or IP address the server will listen on.
    :param port: Port the server will listen on.        

    :returns: a SocketIOBase instance.

    """    
    socketio=SocketIO(app = FlaskBase.app, ping_interval=10, async_mode="gevent")
    
    def __init__(self, host, port):
        logging.debug("SocketIOBase Constructor Executing")
        logging.debug("Listening on host="+ str(host))
        logging.debug("Listening on port="+ str(port))
        self.socketio.run(self.app, host=host, port=port)

