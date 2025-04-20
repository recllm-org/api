from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import recs




app = FastAPI()
app.add_middleware(
	CORSMiddleware,
	allow_origins=['*'],
	allow_credentials=True,
	allow_methods=['*'],
	allow_headers=['*']
)

# routers
app.include_router(recs.router)

# root
@app.get('/')
def home():
	return {'message': 'Hello World'}