from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
from sqlalchemy import ForeignKey, VARCHAR, create_engine, ForeignKey, DateTime, Column, Integer, String, Boolean
from sqlalchemy.dialects.mysql import LONGTEXT

host = 'localhost'
user = 'root'
password = ''
database = 'nairobi_water'

SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{user}:{password}@{host}/{database}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, echo=True)
session = sessionmaker(bind=engine)

Base = declarative_base()

class Feedback(Base):
    """
    This is a class to manage the feedback table
    """
    __tablename__ = "requests"
    request_id = Column(Integer, nullable=False, primary_key=True)
    request_title = Column(String(100), nullable=True)
    request_info = Column(LONGTEXT, nullable=False)
    # email = Column(String(100), nullable=True)
    feedback_time = Column(DateTime, default=datetime.now, nullable=False)


class User(Base):
    """
    This is a class to manage users table
    """
    __tablename__='users'
    mannumber = Column(Integer, nullable=False, primary_key=True)
    password = Column(String(100), nullable=False)
    first_name = Column(String(255), nullable=False)
    second_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    role = Column(String(50), nullable=False)
    registration_time = Column(DateTime, default=datetime.now, nullable=False)
