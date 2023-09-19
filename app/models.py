import uuid
from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, text, Integer
from sqlalchemy.dialects.postgresql import UUID


class CashBook(Base):
    __tablename__ = 'cash_book'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    titulo = Column(String,  nullable=False)
    criacao_dt = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    lancamento_dt = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text("now()"))
    valor = Column(Integer, nullable=False, default=0)
    status = Column(String, nullable=True)
