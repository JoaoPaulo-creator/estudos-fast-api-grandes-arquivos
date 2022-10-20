from fastapi import APIRouter



router = APIRouter()

@router.get('/users/', tags=['users'])
async def ler_usuarios():
    return [{'username': 'Joao'}, {'username': 'Rafael'}]


@router.get('/users/me', tags=['users'])
async def ler_meu_usuario():
    return {'username': 'Joao'}

@router.get('/users/{username}', tags=['user'])
async def ler_usuario(username: str):
    return {'username': username}
