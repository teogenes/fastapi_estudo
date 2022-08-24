"""_summary_"""
from typing import Optional, List
from datetime import  datetime, timedelta

from pytz import timezone
from fastapi.security import OAuth2PasswordBearer

from pydantic import EmailStr
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from jose import jwt

from models.usuario_model import UsuarioModel
from core.configs import Settings, settings
from core.security import verificar_senha

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/usuarios/login"
)

async def autenticar(email: EmailStr, senha: str, db: AsyncSession) -> Optional[UsuarioModel]:
    """_summary_"""
    async with db as session:
        query = select(UsuarioModel).filter(UsuarioModel.email == email)
        result = await session.execute(query)
        usuario: UsuarioModel = result.scalars().unique().one_or_none()

        if not usuario:
            return None

        if not verificar_senha(senha, usuario.senha):
            return None

        return usuario

def _criar_token(tipo_token: str, tempo_vida: timedelta, sub: str) -> str:
    payload = {}

    ceara = timezone('America/Fortaleza')
    expira = datetime.now(tz=ceara) + tempo_vida

    payload['type'] = tipo_token
    payload['exp'] = expira
    payload['iat'] = datetime.now(tz=ceara)
    payload['sub'] = str(sub)

    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.ALGORITHM)

def criar_token_acesso(sub: str) -> str:
    """_summary_"""
    return _criar_token(
        tipo_token = 'access_token',
        tempo_vida= timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub = sub
    )
