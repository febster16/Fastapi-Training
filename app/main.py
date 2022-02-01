from fastapi import FastAPI

from app.oauth2 import SECRET_KEY
from .database import engine
from .routers import post, user, auth, vote
from app import models
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)


app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# my_posts = [{"title" : "post 1", "content" : "content of post 1", "id" : 1},
#             {"title" : "post 2", "content" : "content of post 2", "id" : 2}]
    
app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)
app.include_router(auth.router)
                
@app.get('/')
def root():
    return {"message": "Hello World"}


