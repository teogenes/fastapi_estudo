# pylint: disable=C0116
from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/usuarios')
async def get_usuarios():
    return {'infor': "todos os usuarios"}
