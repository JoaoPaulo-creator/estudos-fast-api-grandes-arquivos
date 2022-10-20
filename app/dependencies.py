from fastapi import Header, HTTPException

async def pegar_token_header(token_: str = Header()):
    if token_ != 'fake-super-secret-token':
        raise HTTPException(status_code=400, detail='Token header inválido')

async def pegar_query_token(token_: str):
    if token_ != 'jessica':
        raise HTTPException(status_code=400, detail='Token jessica não fornecido')

