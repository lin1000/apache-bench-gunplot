# -*- coding: utf-8 -*-
"""

.. module:: api_standalone
   :synopsis: An API service module 

"""
import logging
logging.basicConfig(filename='/app/data/var/log/api_standalone.log', level=logging.DEBUG)

from  lib.socket_io_base import SocketIOBase
import amqpstorm
import threading
from time import sleep
import time
from datetime import datetime
from flask import Flask, render_template, url_for, session, request, send_from_directory
import json
from flask_socketio import SocketIO 
from jinja2 import Environment
import jinja2
import sys, os
import pprint
from lib import sqlalchemy_style_1

PP = pprint.PrettyPrinter(indent=4)


#jinja2 template environment settings
def to_json(value):
    return json.dumps(value)
jinja2.filters.FILTERS['to_json'] = to_json


class ApiStandaloneService(SocketIOBase):
    """This class in inherited from SocketIOBase to get the capability of providing websocket capability.

    .. note::

        For dockerized deployment, listening on `host` 0.0.0.0 is suggested.

    :param host: Hostname or IP address the server will listen on.
    :param port: Port the server will listen on.

    :returns: an ApiStandaloneService instance.

    """    

    def __init__(self, host, port):
        super().__init__( host, port)

    @SocketIOBase.app.route('/simulate',  methods=['POST'])
    def simulate():
        """A simulate function to inject a mocked message from request.body
        Accepting Request Route from "/simulate" (POST) with body in `application/json` content type


        .. warning::

            This method should only used for develpment and testing purpose

        """        

        logging.debug("=====simulate======")    
        logging.debug(request.get_data().decode("utf-8","ignored"))    
        logging.debug(type(request.get_data().decode("utf-8","ignored")))
        
        #req_json = request.get_json()
        req_str = request.get_data().decode("utf-8","ignored")

        return req_str

    @SocketIOBase.socketio.on('register')
    def register(json):
        """Accepting websocket incoming event : register

        .. note::

            Whenever users are connected view aoi_view, a register event will be generated and send back to servere.

        """                    
        logging.info("received json: {myjson}".format(myjson=str(json)))


    @SocketIOBase.app.route("/api_view")                      
    def aoi_view():
        """Dasboard View of this Service
        Accepting Request Route from "/api_view"

        """                
        return render_template('api.html')

    @SocketIOBase.app.route("/")
    def index():
        """Serving for convenient redirection to /aoi_view
        Accepting Request Route from "/"

        """                
        return ApiStandaloneService.doc("index.html")

    @SocketIOBase.app.route("/<path:path>")
    def doc(path):
        """Rendering Servie Document /index.html

        Accepting Request Route from "/index.html"
        """                
        logging.debug("====================")
        return send_from_directory('../static', path)                       


if __name__ == '__main__':
    #logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    ApiStandaloneService(host="0.0.0.0", port=8081)
