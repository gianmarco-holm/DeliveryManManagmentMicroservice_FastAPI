from pydantic import BaseModel, EmailStr, Field
from datetime import date, datetime
from typing import Optional

# Este schema sirve para validar los datos que ingresan
class RepartidorSchema(BaseModel):
    idRepartidor: Optional[int] = Field(None, description="ID del repartidor (opcional)")
    nombre: str = Field(..., description="Nombre del repartidor")
    apellidoPaterno: str = Field(..., description="Apellido paterno del repartidor")
    apellidoMaterno: str = Field(..., description="Apellido materno del repartidor")
    dni: str = Field(..., min_length=8, max_length=8, description="DNI del repartidor (8 caracteres)")
    correo: EmailStr = Field(..., description="Correo electrónico del repartidor")
    telefono: Optional[str] = Field(None, pattern=r'^\d{9}$', description="Número de teléfono del repartidor (opcional, 9 dígitos)")
    licenciaConducir: str = Field(..., description="Licencia de conducir del repartidor")
    direccion: Optional[str] = Field(None, max_length=100, description="Dirección del repartidor (opcional, hasta 100 caracteres)")
    fechaNacimiento: Optional[date] = Field(None, description="Fecha de nacimiento del repartidor (sin hora)")
    sexo: Optional[str] = Field(None, description="Sexo del repartidor")
    created_at: Optional[datetime] = Field(None, description="Fecha de creación del repartidor")

    class Config:
        title = "Esquema de Repartidor"
        description = "Modelo para representar un repartidor"
        json_schema_extra = {
            "examples": [
                {
                    "nombre": "Ana",
                    "apellidoPaterno": "González",
                    "apellidoMaterno": "Martínez",
                    "dni": "76543210",
                    "correo": "ana@example.com",
                    "telefono": "987654321",
                    "licenciaConducir": "XYZ789",
                    "direccion": "Calle Principal 123 - Miraflores",
                    "fechaNacimiento": "1985-05-22",
                    "sexo": "femenino"
                }
            ]
        }
