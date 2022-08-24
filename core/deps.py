"""_summary_"""
from typing import Generator, Optional

from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel

from core.database import Session
from core.auth import oauth2_schema
from core.configs import settings
from models.usuario_model import UsuarioModel


class TokenData(BaseModel):
    """_summary_"""
    username: Optional[str] = None


async def get_session() -> Generator:
    """_summary_"""
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()


async def get_corrent_user(db: Session = Depends(get_session), token: str = Depends(oauth2_schema)) -> UsuarioModel:
    """_summary_"""
    credetial_exception: HTTPException = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Não foi possível autenticar a credencial',
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.ALGORITHM],
            options={'verify_aud': False}
        )

        username: str = payload.get('sub')

        if username is None:
            raise credetial_exception

        token_data: TokenData = TokenData(username=username)

    except JWTError as err:
        raise credetial_exception from err

    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.id == int(token_data.username))
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if not usuario:
            raise credetial_exception
        return usuario
    