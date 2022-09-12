
import enum


class Status(enum.Enum):
    NOVO: int = 1
    EM_ANDAMENTO: int = 2
    CONCLUIDO: int = 3
    ERRO: int = 4