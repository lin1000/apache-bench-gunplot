# -*- coding: utf-8 -*-
"""

.. module:: flask_base
   :synopsis: This reusable module for providing flask capability to service implementation
.. moduleauthor:: Tony Lin

"""

from flask import Flask
import urllib 
from sqlalchemy import create_engine
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import logging
import yaml
import os
import base64

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
    logging.info("FlaskBase")
    
    app = Flask(__name__, template_folder="../templates", static_folder='../static')


    cur_path = os.path.dirname(os.path.realpath(__file__))
    logging.info("cur_path="+ cur_path)
    yaml_path = os.path.join(cur_path,"config.yaml")
    config_file = open(yaml_path, 'r', encoding='utf-8')
    config = config_file.read()
    config_dict = yaml.load(config) 
    db_string = "postgresql://"+config_dict['db']['username']+":"+base64.b64decode(config_dict['db']['password']).decode("utf-8")+"@"+config_dict['db']['hostname']+":"+str(config_dict['db']['port'])+"/"+config_dict['db']['db']
    db = create_engine(db_string,pool_recycle=7200, pool_size=config_dict['sqlalchemy']['pool_size'],pool_timeout=30,logging_name="alibaba postgreSQL")
    #db = create_engine(db_string,poolclass=NullPool)
    
    Session = sessionmaker(db) 

    base = declarative_base()
    base.metadata.create_all(db)         

    def __init__(self, host, port):
        logging.debug("Flask Constructor Executing")
        logging.debug("Listening on host="+ str(host))
        logging.debug("Listening on port="+ str(port))
        self.app.run(host=host, port=port)

