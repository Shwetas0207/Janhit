from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.admin import *
from Core.db import *

router =APIRouter()


@router.post('/show_contact')
async def cont():
    data = list(contactdb.find({}, {'_id': 0}))
    if not data:
        return JSONResponse({'data': []}, status_code=200)
    return JSONResponse({'data': data}, status_code=200)


@router.post('/show_join')
async def joi():
    data = list(joindb.find({}, {'_id': 0}))
    if not data:
        return JSONResponse({'data': []}, status_code=200)
    return JSONResponse({'data': data}, status_code=200)