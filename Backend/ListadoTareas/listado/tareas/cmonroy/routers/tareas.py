from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from listado.tareas.cmonroy.dependencies.tarea_dependencies import get_tarea_service
from listado.tareas.cmonroy.models.tarea import Tarea
from listado.tareas.cmonroy.services.tarea_service import TareaService

router = APIRouter()

@router.get('/', response_model=List[Tarea])
def find_all_tareas(tarea_service: TareaService = Depends(get_tarea_service)):
    return tarea_service.find_all_tareas()

@router.get('/{tarea_id}', response_model=Optional[Tarea])
def find_tarea_by_id(tarea_id: int, tarea_service: TareaService = Depends(get_tarea_service)):
    tarea = tarea_service.find_tarea_by_id(tarea_id)
    if tarea is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f'Tarea con id={tarea_id} no existe en el sistema'
        )
    return tarea

@router.post('/', response_model=Tarea, status_code=status.HTTP_201_CREATED)
def create_tarea_by_id(nueva_tarea: Tarea, tarea_service: TareaService = Depends(get_tarea_service)):
    return tarea_service.create_tarea(nueva_tarea)

@router.put('/{tarea_id}', response_model=Tarea)
def update_tarea(tarea_id: int, tarea: Tarea, tarea_service: TareaService = Depends(get_tarea_service)):
    tarea_updated = tarea_service.update_tarea(tarea_id, tarea)
    if tarea_updated is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail=f'Tarea id={tarea_id} no existe en el sistema'
        )
    return tarea_service.update_tarea(tarea_id, tarea)

@router.delete('/{tarea_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_tarea(tarea_id: int, tarea_service: TareaService = Depends(get_tarea_service)):
    tarea_deleted = tarea_service.delete_tarea(tarea_id)
    if not tarea_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tarea id={tarea_id} no existe en el sistema')