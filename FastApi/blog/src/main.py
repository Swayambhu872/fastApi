
from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import session
from sqlalchemy.sql.expression import outerjoin
from starlette.routing import Route, Router
from . import model
from .routers import blog, user,authentication
from fastapi_crudrouter import MemoryCRUDRouter as CRUDRouter
from .schemas import Potato
from fastapi import APIRouter
from .database import get_db
from .repository import potatoRepository
router = APIRouter()


from .database import engine


model.Base.metadata.create_all(engine)

app = FastAPI()
# app.include_router(CRUDRouter(schema=Potato))

# @router.get('/find/{id}',response_model=Potato)
# def overloaded_get_one(id:int, db:session=Depends(get_db)):
#     return  potatoRepository.deleteBlog(id,db)

app.include_router(blog.router)
app.include_router(user.router)
#app.include_router(authentication.router)

