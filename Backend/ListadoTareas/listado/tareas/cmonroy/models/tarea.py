from pydantic import BaseModel, Field, EmailStr

class Tarea(BaseModel):
    id: int | None = None
    descripcion_tarea: str = Field(..., min_length=8,
                                   max_length=200,
                                   description='Descripción de la tarea con longitud entre 8 a '
                                                                     '200 caracteres')
    responsable: str | None = Field(default=None,
                                    description='Responsable de la tarea. No es necesaria pues sobre la marcha'
                                                              'se puede decidir')
    prioridad: int = Field(...,
                           ge=1,
                           le=5,
                           description='Prioridad de la tarea entre 1 (muy baja) y 5 (muy alta)')