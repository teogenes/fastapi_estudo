"""_summary_"""
from typing import Optional, List

from pydantic import BaseModel as SCBaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema

class UsuarioSchemaBase(SCBaseModel):
    """_summary_"""
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False

    class Config:
        """_summary_"""
        orm_mode = True


class UsuarioSchemaCreate(UsuarioSchemaBase):
    """_summary_"""
    senha: str


class UsuarioSchemaUp(UsuarioSchemaBase):
    """_summary_"""
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]


class UsuarioSchemaArtigos(UsuarioSchemaBase):
    """_summary_"""
    artigos: Optional[List[ArtigoSchema]]
