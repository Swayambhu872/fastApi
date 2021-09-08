from fastapi import HTTPException,status
from .. import model
from sqlalchemy.orm import Session
from .. import schemas



def getAllBlogs(db):
     blogs = db.query(model.Blog).all()
     return blogs

def createBlog(blog:schemas.Blog, db:Session  ):
    new_blog =  model.Blog(title=blog.title, author=blog.author, body=blog.body, publishedStatus=blog.publishedStatus, owner_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def getBlogByID(id:int,db:Session ):
     blog = db.query(model.Blog).filter(model.Blog.id==id).first()
     if not blog:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"the blog with id {id} does not exit")
     return blog


def deleteBlog(id:int, db:Session):
     blog = db.query(model.Blog).filter(model.Blog.id==id)
     if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'blog with id {id} not found')
     else:
        blog.delete(synchronize_session=False)
     db.commit()
     return {'detail':'the blog is successfully deleted'}


def updateBlog(id:int, request:schemas.Blog, db:Session):
      blog= db.query(model.Blog).filter(model.Blog.id == id).first()
   
      if not blog:
             raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'blog with id {id} not found')
      else:
            db.query(model.Blog).filter(model.Blog.id == id).update(request.dict())

      db.commit()
      db.refresh(blog)
      return blog