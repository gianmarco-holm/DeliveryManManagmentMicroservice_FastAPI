from sqlalchemy.orm import Session
from models.repartidorModel import RepartidorModel
from schemas.repartidorSchema import RepartidorSchema

class RepartidorService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def obtener_repartidores(self):
        return self.db.query(RepartidorModel).all()

    def obtener_repartidor_por_id(self, id_repartidor: int):
        return self.db.query(RepartidorModel).filter_by(idRepartidor=id_repartidor).first()

    def crear_repartidor(self, repartidor: RepartidorSchema):
        nuevo_repartidor = RepartidorModel(**repartidor.dict())
        self.db.add(nuevo_repartidor)
        self.db.commit()
        self.db.refresh(nuevo_repartidor)  # Para cargar completamente los datos desde la base de datos
        return nuevo_repartidor

    def actualizar_repartidor(self, id_repartidor: int, repartidor_actualizado: RepartidorSchema):
        repartidor_existente = self.obtener_repartidor_por_id(id_repartidor)
        if repartidor_existente:
            for key, value in repartidor_actualizado.dict(exclude_unset=True).items():
                setattr(repartidor_existente, key, value)
            self.db.commit()
            self.db.refresh(repartidor_existente)
            return repartidor_existente
        return None

    def eliminar_repartidor(self, id_repartidor: int):
        repartidor_existente = self.obtener_repartidor_por_id(id_repartidor)
        if repartidor_existente:
            self.db.delete(repartidor_existente)
            self.db.commit()
            return True
        return False
