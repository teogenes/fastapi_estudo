# pylint: disable=C0116
from typing import Optional, Any
from pydantic import BaseModel, validator

class Curso(BaseModel):
    """_summary_"""
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    @validator('titulo')
    def titulo_validar(cls, valor: str) -> Any:
        palavras = valor.split(' ')
        #validação Um
        if len(palavras) < 3:
            raise ValueError('O titulo deve ter pelo menos 3 palavras!')
        
        #validação Dois
        if valor.islower():
            raise ValueError('O titulo deve ser Capitalizado!')
        
        return valor


cursos = [
    Curso(
        id=1,
        titulo='Programação para Leigos',
        aulas= 112,
        horas= 58,
    ),
    Curso(
        id=2,
        titulo= 'Algoritmos e Lógica de Programação',
        aulas= 87,
        horas= 67,
    )
]