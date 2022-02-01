from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from app import oauth2
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from sqlalchemy import func
from ..database import engine, get_db
from typing import List, Optional

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# def find_index(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

@router.get('/',
        response_model = List[schemas.PostOut])
def get_posts( db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), Limit: int = 10, Skip: int = 0, Search: Optional[str] = ""):
    # cursor.execute(""" SELECT * FROM posts """)
    # posts = cursor.fetchall()
    
    # posts = db.query(models.Post).filter(models.Post.title.contains(Search)).limit(Limit).offset(Skip).all()
    
    posts = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(
        models.Post.title.contains(Search)).limit(Limit).offset(Skip).all()
    
    return posts

# @app.get('/posts')
# def get_posts():
#     return {"data" : my_posts}

# @app.post('/posts', status_code = status.HTTP_201_CREATED)
# def create_posts(post : Post):
#     print(post)
#     post_dict = post.dict()
#     post_dict['id'] = randrange(0, 1000000)
#     my_posts.append(post_dict)
#     return {"data" : post_dict}
# title str, content str

@router.post('/', 
          status_code = status.HTTP_201_CREATED,
          response_model = schemas.Post)
def create_posts(post : schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title, post.content, post.published))
    # post = cursor.fetchone()
    # conn.commit()
    post =  models.Post(user_id=current_user.id, **post.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

        
# @router.get("/posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)-1]
#     return {"post_detail" : post}

# @app.get("/posts/{id}")
# def get_post(id : int, response: Response):
#     post = find_post(int(id))
#     if not post:
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"message" : f"Post with id {id} was not found"}
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id: {id} was not found")
#     return {"post_detail" : post}

@router.get("/{id}", 
        response_model = schemas.PostOut)
def get_post(id : int, response: Response, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id),))
    # post = cursor.fetchone()
    # print(post)
    
    # post = db.query(models.Post).filter(models.Post.id == id).first()
      
    post = db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).first()
        
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} was not found" )
    
    return post

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id : int):
#     index = find_index(id)
#     if index == None:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id: {id} was not found")
#     my_posts.pop(index)
    
#     return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id : int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING * """, (str(id),))
    # post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id: {id} was not found")
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized to perform requested action.")
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}")
# def update_post(id : int, post: Post):
#     index = find_index(id)
#     if index == None:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id: {id} was not found")
    
#     post_dict = post.dict()
#     post_dict['id'] = id
#     my_posts[index] = post_dict
    
#     return {"data" : post_dict}

@router.put("/{id}",
        response_model = schemas.Post)
def update_post(id : int, post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING * """, (post.title, post.content, post.published, str(id)))
    # post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    updated_post = post_query.first()
    
    if updated_post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id: {id} was not found")

    if updated_post.user_id != current_user.id:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Not authorized to perfom requested action")
    
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()


    return updated_post
