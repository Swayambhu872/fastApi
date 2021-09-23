# from fastapi import APIRouter, Depends,HTTPException,status
# from fastapi.security import OAuth2PasswordRequestForm

# from .. import schemas,model,token
# from ..database import get_db
# from ..hashing import Hash
# from sqlalchemy.orm import Session


# router = APIRouter


# router = APIRouter(
#     tags=['Authentication']
# )

# @router.post('/login')
# def login(request:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
#     user=db.query(model.User).filter(model.User.email == request.username).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")

#     if not Hash.verify(user.password,request.password):
#          raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="invalid credentials")
    

    
#     access_token = token.create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}