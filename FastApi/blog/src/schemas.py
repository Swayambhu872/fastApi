from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel) :
    title:str
    author:str
    body:str
    publishedStatus:Optional[bool] = False
    class Config():
        orm_mode=True


class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs : List[Blog] =[]
    class Config():
        orm_mode=True

class ShowOwner(BaseModel):
    name:str
    email:str
    class Config():
        orm_mode=True

class ShowBlog(BaseModel):
    title:str
    author:str
    owner:ShowOwner
    class Config():  #Pydantic models can be created from arbitrary class instances to support models that map to ORM objects
        orm_mode=True #The Config property orm_mode must be set to True.

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
    