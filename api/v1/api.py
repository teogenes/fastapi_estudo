from fastapi import APIRouter

from api.v1.endpoints import curso, artigo, usuario


api_router = APIRouter()

#* ------------------------- Recursos ---------------------------------
api_router.include_router(artigo.router, prefix='/artigos', tags=["Artigos"])
api_router.include_router(curso.router, prefix='/cursos', tags=["Cursos"])
api_router.include_router(usuario.router, prefix='/usuarios', tags=["Usuarios"])
