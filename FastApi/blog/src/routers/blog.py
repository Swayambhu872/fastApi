from fastapi import APIRouter, Depends,status
from typing import List
from .. import schemas
from sqlalchemy.orm import Session
from ..database import get_db
from..repository import blogRepository
from ..oauth2 import get_current_user
router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)



@router.get('/getblog/', response_model=List[schemas.ShowBlog])           #pydantic models means are schemas model, since response model is in operation decorator , it will be a pydantic model
def getAllBlogs(db:Session=Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
 return blogRepository.getAllBlogs(db)



@router.post('/', status_code=status.HTTP_201_CREATED)
def create(blog:schemas.Blog, db:Session = Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)): #"blog:schemas.Blog" here blog is a request body of type Blog from schemas file
    return blogRepository.createBlog(blog, db)




@router.get('/getById/{id}', response_model=schemas.ShowBlog)
def getBlogById(id:int, db:Session=Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
    return blogRepository.getBlogByID(id, db)



@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteBlog(id:int, db:Session=Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)) :
  return blogRepository.deleteBlog(id,db)


@router.put("/update/{id}")
def updateBlog(id:int, request:schemas.Blog, db:Session=Depends(get_db),get_current_user:schemas.User=Depends(get_current_user)):
   return blogRepository.updateBlog(id, request, db)
