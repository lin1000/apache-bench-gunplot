# -*- coding: utf-8 -*-
"""

.. module:: flask_base
   :synopsis: This reusable module for providing flask capability to service implementation
.. moduleauthor:: Tony Lin

"""

from flask import Flask
import logging

class FlaskBase(object):
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
    
    app = Flask(__name__, template_folder="../templates", static_folder='../static')

    def __init__(self, host, port):
        logging.debug("Flask Constructor Executing")
        logging.debug("Listening on host="+ str(host))
        logging.debug("Listening on port="+ str(port))
        self.app.run(host=host, port=port)

