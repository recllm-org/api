from api import App
from api.config import Config



config = Config(reqd_tables={'recllm_users': 'UserTable', 'recllm_items': 'ItemTable'})
app = App(config)
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)


@app.get("/")
def root():
  return {"message": "Welcome to the API"}