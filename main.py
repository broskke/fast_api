from app.models.posts.post_model import Genre, Post, PostGenres
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre,delete_genre,get_genres
from app.queries.posts import create_post, get_all_films, get_film_by_id
from app.schemes.posts import PostCreateSchema
from app.routes.posts import router
from fastapi import FastAPI


@db
def create_tables():
    db_connection.create_tables([Genre,Post,PostGenres])
create_tables()
app = FastAPI()
app.include_router(router)
# create_tables()
# delete_genre('Детектив')
# create_genre('Ужас')
# print(get_genres())

# create_post('Судья Дред','Фильм про судью','1988','Америка',['Ужас','Детектив'])
# print(get_film_by_id(1))
# from datetime import date
# create_post(PostCreateSchema(title='Бетмен',description='Темный рыцарь вернулся в готем',year=date(2004, 1, 1),country='Америка',genre=['Ужас']))