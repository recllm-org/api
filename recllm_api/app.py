from fastapi import FastAPI
from .db import BasicDatabase



class App(FastAPI):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.db = BasicDatabase()
	
	def add_routers(self, routers):
		for router in routers:
			self.include_router(router)