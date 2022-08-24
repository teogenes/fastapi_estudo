"""_summary_"""
from passlib.context import CryptContext


CRIPTO = CryptContext( schemes=['bcrypt'], deprecated='auto')


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """_summary_"""
    return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str) -> str:
    """_summary_"""
    return CRIPTO.hash(senha)
