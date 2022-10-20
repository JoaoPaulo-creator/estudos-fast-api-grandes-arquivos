from fastapi import APIRouter

router = APIRouter()

@router.post('/')
async def atualizar_admin():
    return {'message': 'Admin aoihsefioh'}