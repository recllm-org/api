from api import App
from api.config import Config
from fastapi.middleware.cors import CORSMiddleware
from pgvector.sqlalchemy import Vector
from fastapi import Body
from pydantic import BaseModel



config = Config(reqd_tables={'recllm_users': 'RecLLMUsers', 'recllm_items': 'RecLLMItems'})
app = App(config)
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)


def recommendations(user_id, user_tablename, already_shown, top_k):
  with app.db.Session() as session:
    RecLLMUsers = app.db.RecLLMUsers
    RecLLMItems = app.db.RecLLMItems
    recllm_user = session.query(RecLLMUsers).filter(RecLLMUsers.tablename==user_tablename and RecLLMUsers.row_id==user_id).first()
    recllm_items = (
      session.query(RecLLMItems)
      .filter(RecLLMItems.id.notin_(already_shown))
      .order_by(Vector.comparator_factory.cosine_distance(RecLLMItems.embedding, recllm_user.embedding))
      .limit(top_k)
      .all()
    )
    return [{'table': item.tablename, 'id': item.row_id} for item in recllm_items]


class RecommendationsRequest(BaseModel):
  already_shown: list[str] = []


@app.get('/recommendations/{user_id}')
def get_recommendations(
    user_id: str,
    user_tablename: str,
    top_k: int,
    request: RecommendationsRequest
):
  return recommendations(
    user_id=user_id,
    user_tablename=user_tablename,
    already_shown=request.already_shown,
    top_k=top_k
  )