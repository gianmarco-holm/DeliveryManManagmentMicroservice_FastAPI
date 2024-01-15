from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.repartidorSchema import RepartidorSchema
from services.repartidorService import RepartidorService
from utils.dependencies import get_db

repartidor_router = APIRouter()

@repartidor_router.get('/repartidores', tags=['Repartidores'], response_model=List[RepartidorSchema])
def obtener_repartidores(db: Session = Depends(get_db)) -> List[RepartidorSchema]:
    try:
        resultado = RepartidorService(db).obtener_repartidores()
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener repartidores: {str(e)}")


@repartidor_router.get('/repartidores/{id_repartidor}', tags=['Repartidores'], response_model=RepartidorSchema)
def obtener_repartidor_por_id(id_repartidor: int, db: Session = Depends(get_db)) -> RepartidorSchema:
    try:
        resultado = RepartidorService(db).obtener_repartidor_por_id(id_repartidor)
        if resultado:
            return resultado
        else:
            raise HTTPException(status_code=404, detail=f"No se encontró un repartidor con el ID {id_repartidor}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener repartidor por ID: {str(e)}")

@repartidor_router.post('/repartidores', tags=['Repartidores'], response_model=RepartidorSchema, status_code=201)
def crear_repartidor(repartidor: RepartidorSchema, db: Session = Depends(get_db)) -> RepartidorSchema:
    try:
        nuevo_repartidor = RepartidorService(db).crear_repartidor(repartidor)
        return nuevo_repartidor
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear repartidor: {str(e)}")

@repartidor_router.put('/repartidores/{id_repartidor}', tags=['Repartidores'], response_model=RepartidorSchema)
def actualizar_repartidor(id_repartidor: int, repartidor_actualizado: RepartidorSchema, db: Session = Depends(get_db)) -> RepartidorSchema:
    try:
        resultado = RepartidorService(db).actualizar_repartidor(id_repartidor, repartidor_actualizado)
        if resultado:
            return resultado
        else:
            raise HTTPException(status_code=404, detail=f"No se encontró un repartidor con el ID {id_repartidor}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar repartidor: {str(e)}")

@repartidor_router.delete('/repartidores/{id_repartidor}', tags=['Repartidores'], status_code=204)
def eliminar_repartidor(id_repartidor: int, db: Session = Depends(get_db)):
    try:
        eliminado_exitosamente = RepartidorService(db).eliminar_repartidor(id_repartidor)
        if not eliminado_exitosamente:
            raise HTTPException(status_code=404, detail=f"No se encontró un repartidor con el ID {id_repartidor}.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar repartidor: {str(e)}")
