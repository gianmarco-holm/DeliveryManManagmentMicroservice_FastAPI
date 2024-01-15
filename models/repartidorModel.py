from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from config.database import Base

# Realiza el modelo de la tabla de la base de datos que va a representar
class RepartidorModel(Base):
    __tablename__ = 'repartidores'

    idRepartidor = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellidoPaterno = Column(String(100), nullable=False, name= 'apellido_paterno')
    apellidoMaterno = Column(String(100), nullable=False, name='apellido_materno')
    dni = Column(String(8), nullable=False, unique=True)
    correo = Column(String(100), nullable=False, unique=True)
    telefono = Column(String(9), nullable=False)
    licenciaConducir = Column(String(9), nullable=False, name='licencia_conducir')
    direccion = Column(String(100), nullable=True)
    fechaNacimiento = Column(DateTime, nullable=True, name='fecha_nacimiento')
    sexo = Column(String(1), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
