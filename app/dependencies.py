from .db import BasicDatabase

db = BasicDatabase({'recllm_users': 'UserTable', 'recllm_items': 'ItemTable'})

def get_db():
	try:
		yield db
	finally:
		pass  # Connection handling is managed by BasicDatabase class