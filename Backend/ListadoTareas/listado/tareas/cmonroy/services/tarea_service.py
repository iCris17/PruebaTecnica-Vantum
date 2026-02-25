from typing import List, Optional

from listado.tareas.cmonroy.models.tarea import Tarea
from listado.tareas.cmonroy.repositories.tarea_repository import TareaRepository


class TareaService():
    def __init__(self, tarea_repository: TareaRepository):
        self._tarea_repository = tarea_repository

    def find_all_tareas(self) -> List[Tarea]:
        return self._tarea_repository.find_all_tareas()

    def find_tarea_by_id(self, tarea_id: int) -> Optional[Tarea]:
        return self._tarea_repository.find_tarea_by_id(tarea_id)

    def create_tarea(self, nueva_tarea: Tarea) -> Tarea:
        return self._tarea_repository.create_tarea(nueva_tarea)

    def update_tarea(self, tarea_id: int, tarea: Tarea) -> Optional[Tarea]:
        return self._tarea_repository.update_tarea(tarea_id, tarea)

    def delete_tarea(self, tarea_id) -> bool:
        return self._tarea_repository.delete_tarea(tarea_id)