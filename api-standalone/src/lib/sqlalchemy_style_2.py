import urllib 
from sqlalchemy import create_engine
from sqlalchemy import Column, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
import logging

logging.info("importing sql_alchemy_style_2")
db_user = "lin1000"
db_pass = urllib.parse.quote_plus('98sc@SAenv')
db_string = "postgresql://"+db_user+":"+db_pass+"@rm-3ns40d8hp7xi206z48o.pg.rds.aliyuncs.com:3432/postgres"

db = create_engine(db_string,pool_recycle=7200, pool_size=10,pool_timeout=30,logging_name="alibaba postgreSQL")
base = declarative_base()

class Film(base):  
    __tablename__ = 'films'

    title = Column(String, primary_key=True)
    #title = Column(String)
    director = Column(String)
    year = Column(String)

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)


# Create 
# db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")  
# db.execute("INSERT INTO films (title,   director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

i_am_bueaty = Film(title="I Feel Pretty", director="Abby", year="2018")  
session.add(i_am_bueaty)  
session.commit()


# Read
# result_set = db.execute("SELECT * FROM films")  
# for r in result_set:  
#     logging.info(r)


films = session.query(Film)  
for film in films:  
    logging.info("Printing film")
    logging.info(film.title)
    logging.info(film.director)
    logging.info(film.year)

# Update
# db.execute("UPDATE films SET title='Any2016Film' WHERE year='2016'")
i_am_bueaty.title = "I AM Beauty update by Tony"  
session.commit()


# Delete
#   db.execute("DELETE FROM films WHERE year='2016'")  
session.delete(i_am_bueaty)  
session.commit()  

logging.info("importing sql_alchemy_style_2_end")