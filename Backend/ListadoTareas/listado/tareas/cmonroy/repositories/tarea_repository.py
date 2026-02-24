from typing import List, Optional

from listado.tareas.cmonroy.models.tarea import Tarea


class TareaRepository:
    def __init__(self):
        self._tareas: List[Tarea] = [
            Tarea(id=1, descripcion_tarea='Crear proyecto back-end', responsable='Cristian Monroy', prioridad=3),
            Tarea(id=2, descripcion_tarea='Crear archivo main', responsable='Cristian Monroy', prioridad=5),
            Tarea(id=3, descripcion_tarea='Crear archivo DTO', responsable='Cristian Monroy', prioridad=5),
        ]
        self._next_id = 3

    def find_all_tareas(self) -> List[Tarea]:
        return self._tareas

    def find_tarea_by_id(self, tarea_id: int) -> Optional[Tarea]:
        return next((tarea for tarea in self._tareas if tarea.id == tarea_id), None)

    def create_tarea(self, nueva_tarea: Tarea) -> Tarea:
        self._next_id += 1
        nueva_tarea.id = self._next_id
        self._tareas.append(nueva_tarea)
        return nueva_tarea

    def update_tarea(self, tarea_id: int, tarea: Tarea) -> Optional[Tarea]:
        for index, obj_tarea in enumerate(self._tareas):
            if tarea_id == obj_tarea.id:
                actualizado = Tarea(id=obj_tarea.id,
                                    responsable=tarea.responsable,
                                    prioridad=obj_tarea.prioridad,
                                    descripcion_tarea=obj_tarea.descripcion_tarea)
                self._tareas[index] = actualizado
                return actualizado
        return None

    def delete_tarea(self, tarea_id) -> bool:
        for index, obj_tarea in enumerate(self._tareas):
            if obj_tarea.id == tarea_id:
                del self._tareas[index]
                return True
        return False