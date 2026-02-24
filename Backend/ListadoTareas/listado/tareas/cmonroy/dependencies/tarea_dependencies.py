from anyio.functools import lru_cache
from fastapi import Depends

from listado.tareas.cmonroy.repositories.tarea_repository import TareaRepository
from listado.tareas.cmonroy.services.tarea_service import TareaService


@lru_cache
def get_tarea_repository() -> TareaRepository:
    return TareaRepository()

def get_tarea_service(tarea_repository: TareaRepository = Depends(get_tarea_repository)) -> TareaService:
    return TareaService(tarea_repository)