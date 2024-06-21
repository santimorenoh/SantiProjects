from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'My first FastAPI app'
app.version = '0.0.1'

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "Here the sinopsis",
        "year": "2009",
        "rating": 7.8,
        "category": "Action"
    },

    {
        "id": 2,
        "title": "Other Avatar",
        "overview": "Here the other sinopsis",
        "year": "other 2009",
        "rating": 7.8,
        "category": "Action"
    }
]


@app.get('/', tags = ['home'])
def message():
    return HTMLResponse('<h1>Hello World in HTML</h1>')

@app.get('/movies', tags = ['movies'])
def get_movies():
    return movies

@app.get('/movie/{id}', tags = ['movie'])
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {}