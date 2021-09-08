from fastapi import HTTPException,status
from .. import schemas, model
from sqlalchemy.orm import Session
from ..hashing import Hash



def createUser(request:schemas.User, db:Session):
     hashedPassword = Hash.encrypt(request.password)
     new_user =  model.User(name=request.name, email=request.email, password=hashedPassword)
     db.add(new_user)
     db.commit()
     db.refresh(new_user)
     return new_user



def getAllUser(db:Session):
    users = db.query(model.User).all()
    return users


def getUserById(id:int, db:Session):
    user = db.query(model.User).filter(model.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user if id {id} does not exist")
    return user