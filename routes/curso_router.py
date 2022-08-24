# pylint: disable=C0116
from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/cursos')
async def getdois_cursos():
    return {'infor': "todos os cursos"}
