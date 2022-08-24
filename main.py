# pylint: disable=C0116
from typing import Any, Optional, List
from time import sleep
from fastapi import FastAPI, HTTPException, status
from fastapi import Path, Query, Header
from fastapi import Depends
from fastapi.responses import Response
from models import Curso, cursos
from routes import curso_router, usuario_router

app = FastAPI(
    title='Api de Teste Issec',
    version='0.0.1',
    description='Uma API para estudo de fastapi'
    )

app.include_router(curso_router.router, tags=['Cursos'])
app.include_router(usuario_router.router, tags=['Usuarios'])

def fake_db():
    try:
        print('Abrindo conexão com o banco de dados...')
        sleep(1)
    finally:
        print('fechando conexão com o banco de dados...')
        sleep(1)


@app.get('/')
async def raiz():
    return {'msg':"Fast api"}


@app.get('/cursos',
         description='Retorna todos os cursos ou uma lista vazia',
         summary='Retorna todos os cursos', response_model=List[Curso],
         response_description='Cursos encontrado com sucesso!')
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos

# Path parameter para colocar uma validação a mais nos parametros
@app.get('/cursos/{curso_id}', response_model=Curso)
async def get_curso(curso_id: int = Path(default=None, title='ID o curso',
                    description='Deve ser entre 1 e 2', gt=0, lt=4)) -> Curso:
    try:
        curso = [x for x in cursos if x.id == curso_id]
        return curso[0]
    except IndexError as ex:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail='Curso não encontrado!') from ex


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def add_curso(curso: Curso) -> Curso:
    next_id : int = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso


@app.put('/cursos/{id_curso}')
async def up_curso(id_curso: int, curso: Curso) -> Curso:
    if id_curso in cursos:
        cursos[id_curso] = curso
        del curso.id
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail=f'Curso não encontrado, id {id_curso}!')
    return curso


@app.delete('/cursos/{id_curso}')
async def del_curso(id_curso: int) -> any:
    if id_curso in cursos:
        del cursos[id_curso]
        return Response(content=None,status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail=f'Curso não encontrado, id {id_curso}!')


# Query parameter
# Header parameter
@app.get('/calculadora')
async def calcular(a:int = Query(default=None, gt=5),
                   b:int = Query(default=None, gt=10),
                   x_geek:str = Header(default=None) , # no header colocar x-geek = x_geek
                   c:Optional[int] = None):
    soma = a + b
    if c:
        soma += c

    print(f'X-GEEK: {x_geek}')

    return {'resultado': soma}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, log_level='info', debug=True)
