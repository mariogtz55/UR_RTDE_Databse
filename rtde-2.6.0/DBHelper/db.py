from sqlalchemy import create_engine
import configparser as cp
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

ini = cp.ConfigParser()
ini.read(os.getcwd()+"/config.ini")
# HOST = ini["postgresql"]["host"]
# USER = ini["postgresql"]["user"]
# PSW = ini["postgresql"]["psw"]
# NAME = ini["postgresql"]["dbname"]

# url = "postgresql://{}:{}@{}/{}".format(USER, PSW, HOST, NAME)
url = "postgresql://{}:{}@{}/{}".format("postgres", "7b878d4842f1066bdce43d28", "127.0.0.1:5432", "robot")
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

