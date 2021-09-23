from fastapi import HTTPException,status
from .. import model
from sqlalchemy.orm import Session
from .. import schemas

def getAllData(db,entity):
     print(f"the value of ------>{entity}")
     data = db.query(entity).all()
     return data


def createData(db,newEntity):
    db.add(newEntity)
    db.commit()
    db.refresh(newEntity)
    return newEntity
  