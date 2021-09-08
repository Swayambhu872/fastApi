from fastapi import APIRouter, Depends,status,HTTPException
from typing import List
from .. import schemas,model
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import userRepository

router = APIRouter(
    prefix='/user',
    tags=['Users']
)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.ShowUser)
def create_user(request:schemas.User, db:Session=Depends(get_db)):
   return userRepository.createUser(request,db)



@router.get('/get_all/', response_model=List[schemas.ShowUser])
def get_All_User(db:Session=Depends(get_db)):
    return userRepository.getAllUser(db)



@router.get('/getById/{id}', response_model=schemas.ShowUser)
def get_User_BY_Id(id:int, db:Session=Depends(get_db)):
    return userRepository.getUserById(id,db)