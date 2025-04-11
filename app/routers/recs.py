from fastapi import APIRouter



router = APIRouter(prefix='/recs', tags=['recs'])


@router.get('/')
def get_recs():
	return {'message': 'Here are your recommendations!'}