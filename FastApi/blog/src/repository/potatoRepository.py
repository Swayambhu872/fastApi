from fastapi import HTTPException,status
from .. import model
from sqlalchemy.orm import Session
from .. import schemas

def getBlogByID(id:int,db:Session ):
     potato = db.query(model.Potato).filter(model.Potato.id==id).first()
     return potato