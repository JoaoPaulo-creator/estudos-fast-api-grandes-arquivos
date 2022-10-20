from fastapi import Depends, FastAPI

from .dependencies import pegar_token_header, pegar_query_token
from .internal import admin
from .rotas import items, usuarios


app = FastAPI(dependencies=[Depends(pegar_query_token)])


app.include_router(usuarios.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix='/admin',
    tags=['admin'],
    dependencies=[Depends(pegar_token_header)],
    responses={418: {'description': 'Eu sou um pote de chá'}}
)

@app.get('/')
async def roo():
    return {'message': 'Ola, grandes aplicações'}
