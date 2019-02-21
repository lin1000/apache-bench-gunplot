from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  

base = declarative_base()


class Film(base):  
    __tablename__ = 'films'

    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)    