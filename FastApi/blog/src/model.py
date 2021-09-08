from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import Boolean

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Blog(Base):
    __tablename__='blogs'
    id =  Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    body = Column(String)
    publishedStatus = Column(String)
    
    

class User(Base):
    __tablename__ = 'users'
    id=Column(Integer,primary_key=True, index=True)
    name = Column(String)
    email =Column(String)
    password = Column(String)
    blogs=relationship("Blog", back_populates="owner")
  