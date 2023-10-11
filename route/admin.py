from fastapi import APIRouter
from fastapi.responses import JSONResponse
from model.admin import *
from Core.db import *
from Core.tele import *
import hashlib

router =APIRouter()

@router.post("/register")
async def regis(mod:Register):
    try:
        exist_user=admindb.find_one({'username':mod.username})
        if exist_user:
            return JSONResponse({'error':'Username already exist'},status_code=400)
        if mod.password!=mod.cpassword:
            return JSONResponse({'error':'Password does not match'},status_code=400)
        hash_pass=hashlib.sha256(bytes(mod.password,'utf-8')).hexdigest()
        data={
            'name':mod.name,
            'username': mod.username,
            'password': hash_pass,
            'visible_pass':mod.password
            }
        admindb.insert_one(data)
        sendmsg(f'New user register \nUsername:{mod.username}')
        return JSONResponse({'data':'Register Successful'},status_code=200)
    except Exception as e:
        sendmsg(f'Error:{e}\n Project: Janhit\nFunction: Register ')
        return JSONResponse({'error':'Something went wrong'},status_code=400)



@router.post('/login')
async def login(mod:Login):
    pass

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


@router.post('/show_donation')
async def don():
    data = list(donationdb.find({}, {'_id': 0}))
    if not data:
        return JSONResponse({'data': []}, status_code=200)
    return JSONResponse({'data': data}, status_code=200)