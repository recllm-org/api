from fastapi import FastAPI
from .routers import recs



app = FastAPI()

# routers
app.include_router(recs.router)

# root
@app.get('/')
def home():
	return {'message': 'Hello World'}