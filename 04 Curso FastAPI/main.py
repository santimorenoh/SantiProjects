from fastapi import FastAPI

app = FastAPI()
app.title = 'My first FastAPI app'
app.version = '0.0.1'

@app.get('/', tags = ['home'])
def message():
    return 'Hello World Two - Probando 1 2 3 probando'