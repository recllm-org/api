from fastapi import APIRouter, Depends
from typing import Dict
from ..dependencies import get_db
from ..db import BasicDatabase


router = APIRouter(prefix='/recs', tags=['recs'])


@router.get('/', response_model=Dict[str, str])
def get_recs(db: BasicDatabase = Depends(get_db)) -> Dict[str, str]:
	return {'message': 'Here are your recommendations!'}