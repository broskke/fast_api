from app.queries.posts import (
    get_all_films,
    get_film_by_id,
    create_post
)
from fastapi import APIRouter
from app.schemes.posts import PostCreateSchema

router = APIRouter()
@router.get('/posts')
def get_films():
    return get_all_films()

@router.post('/create-post')
def create_film(film: PostCreateSchema):
    return create_post(film)


#TODO: 

