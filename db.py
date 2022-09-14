from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


motor = create_engine('mysql+pymysql://adminrepo:bigdata21@localhost:3306/repoejemplo')

Session = sessionmaker(bind=motor)

session = Session()
Base = declarative_base()
