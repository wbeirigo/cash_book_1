from datetime import datetime
import decimal
from typing import List
import uuid
from pydantic import BaseModel, EmailStr, constr, validator


class CashBookBaseSchema(BaseModel):
    titulo: str    
    lancamento_dt: datetime
    valor: int
    status: str

    class Config:
        orm_mode = True


class CashBookPostchema(CashBookBaseSchema):
    @validator('titulo')
    def titulo_match(cls, v, values, **kwargs):
        if v == "" :
            raise ValueError('O titulo deve ser informado.')
        return v


    @validator('valor')
    def valor_match(cls, v, values, **kwargs):
        if v <= 0 :
            raise ValueError('O valor informado deve ser inteiro positivo.')
        return v


    @validator('status')
    def status_match(cls, v, values, **kwargs):
        if v not in ['Crédito', "Debito"] :
            raise ValueError('Status inválido, deverá informar [Crédito] ou [Débito]')
        return v

class CashBookResponseSchema(CashBookBaseSchema):
    id: uuid.UUID
    criacao_dt: datetime


class CashBookListResponse(BaseModel):
    records: List[CashBookResponseSchema]