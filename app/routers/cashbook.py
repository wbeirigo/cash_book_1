import uuid
from fastapi import Depends, HTTPException, status, APIRouter, Response
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models, schemas


router = APIRouter()

@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model=schemas.CashBookListResponse)
def get_records(db: Session = Depends(get_db)):
    records = db.query(models.CashBook).all()
    return {"records": records}

@router.get("/{id}", response_model=schemas.CashBookResponseSchema)
def get_record(id: str, db: Session = Depends(get_db)):

    try:
        uuid.UUID(id)
    except:
         raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                             detail="ID inválido")


    record = db.query(models.CashBook).filter(models.CashBook.id == id).first()
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não exise registro com o id: [{id}]")
    return record

@router.delete("/{id}")
def delete_record(id: str, db: Session = Depends(get_db)):

    try:
        uuid.UUID(id)
    except:
         raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                             detail="ID inválido")

    record_query = db.query(models.CashBook).filter(models.CashBook.id == id)
    record = record_query.first()
    if not record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não exite registro com este ID: [{id}]",
        )

    record_query.delete()
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.CashBookResponseSchema)
def update_record(
    id: str, record: schemas.CashBookPostchema, db: Session = Depends(get_db)
):
    
    try:
        uuid.UUID(id)
    except:
         raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                             detail="ID inválido")

    query = db.query(models.CashBook).filter(models.CashBook.id == id)
    qry_record = query.first()
    if not qry_record:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Não exise registros com o id [{id}]",
        )
    query.update(record.dict(exclude_unset=True),
                        synchronize_session=False)
    db.commit()
    return qry_record

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.CashBookResponseSchema
)
def create_record(
    payload: schemas.CashBookPostchema,
    db: Session = Depends(get_db),
    # owner_id: str = Depends(require_user)
):
    query = db.query(models.CashBook).filter(models.CashBook.titulo == payload.titulo)
    qry_record = query.first()
    if qry_record:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Já um registro registtro com o nome [{payload.titulo}]",
        )

    record = models.CashBook(**payload.dict())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record