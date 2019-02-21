import urllib 
from sqlalchemy import create_engine
import logging

print("importing sql_alchemy_style_1")
db_user = "lin1000"
db_pass = urllib.parse.quote_plus('98sc@SAenv')
db_string = "postgresql://"+db_user+":"+db_pass+"@rm-3ns40d8hp7xi206z48o.pg.rds.aliyuncs.com:3432/postgres"

db = create_engine(db_string)

# Create 
db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")  
db.execute("INSERT INTO films (title,   director, year) VALUES ('Doctor Strange', 'Scott Derrickson', '2016')")

print("importing sql_alchemy_style_1_end")

# Read
result_set = db.execute("SELECT * FROM films")  
for r in result_set:  
    logging.info(r)


# Update
db.execute("UPDATE films SET title='Any2016Film' WHERE year='2016'")


# Delete
#   db.execute("DELETE FROM films WHERE year='2016'")  