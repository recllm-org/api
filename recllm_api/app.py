from fastapi import FastAPI
from .db import BasicDatabase



class App(FastAPI):
	def __init__(self, config, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.config = config
		self.db = BasicDatabase(config.reqd_tables)
	
	def add_routers(self, routers):
		for router in routers:
			self.include_router(router)