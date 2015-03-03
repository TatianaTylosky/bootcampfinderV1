from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime,create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
from .database import Base, engine

engine = create_engine('postgresql://tati:tati@localhost:8080')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Bootcamp(Base):
	__tablename__ = "bootcamps"
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	description = Column(String)
    # start_time = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)