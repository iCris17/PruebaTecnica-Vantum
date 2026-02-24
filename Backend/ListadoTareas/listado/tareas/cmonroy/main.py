from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from listado.tareas.cmonroy.routers import tareas

api = FastAPI()

api.include_router(tareas.router, prefix='/tareas', tags=['tareas'])
@api.get('/')
def welcoming():
    return {
        'message': 'La API está funcionando.'
    }

@api.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    custom_errors = []
    for error in exc.errors():
        loc = error.get('loc', [])
        field_name = loc[-1] if loc else 'unknown'

        custom_errors.append({
            'message': error.get('msg', 'Error de validacion'),
            'field': str(field_name),
            'type': error.get('type', 'validation_error'),
        })

    return JSONResponse(status_code=422,
                        content={'errors': custom_errors})