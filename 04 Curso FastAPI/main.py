from fastapi import FastAPI, Body
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

@app.get('/movies/{id}', tags = ['movies'])
def get_movie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {}

@app.get('/movies/', tags = ['movies'])
def get_movies_by_category(category: str, year: int):
    return [movie for movie in movies if movie["category"] == category]

@app.post('/movies', tags = ['movies'])
def create_movie(title: str = Body(), overview: str = Body(), year: str = Body(), rating: float = Body(), category: str = Body()):

    max_id = 0
    for movie in movies:
        if movie["id"] > max_id:
            max_id = movie["id"]
    
    id = max_id + 1

    movies.append({

        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category

    })

    return movies

@app.put('/movies/{id}', tags = ['movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: str = Body(), rating: float = Body(), category: str = Body()):

    for movie in movies:
        if movie['id'] == id:
            movie['title'] = title
            movie['overview'] = overview
            movie['year'] = year
            movie['rating'] = rating
            movie['category'] = category

    return  movies


@app.delete('/movies/{id}', tags = ['movies'])
def delete_movie(id: int):

    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)

    return movies


