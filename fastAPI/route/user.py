# from fastapi import 
from fastapi.responses import JSONResponse
from model.user import *
from Core.db import *
from fastapi import FastAPI, APIRouter



router = APIRouter()



@router.post('/contact')
async def cont(mod:Contact):
    a=contactdb.find_one({"Email":mod.email})
    if a:
        return JSONResponse({'error':'Same email'},status_code=400)
    data={'Name':mod.name,
          'Email':mod.email,
          'Phone':mod.phone,
          'Message':mod.message}
    contactdb.insert_one(data)
    return JSONResponse({'mess':'Conatact Saved'},status_code=200)






@router.post('/join')
async def join(mod:Join):
    a=['male','female','others']
    if mod.gender not in  a:
        return JSONResponse({'error':'Select form the list'},status_code=400)
    data={
        'Fname':mod.fname,
        'Lname':mod.lname,
        'Gender':mod.gender,
        'About':mod.about}
    joindb.insert_one(data)
    return JSONResponse({'mess':'Success'},status_code=200)
    



@router.post('/donation')
async def donation(mod:Donation):
    if mod.amount<0:
        return JSONResponse({'error':'Enter number greater than 0'},status_code=400)
    data={
        'Name':mod.name,
        'Email':mod.email,
        'Phone':mod.phone,
        'Amount':mod.amount
    }   
    donationdb.insert_one(data)
    return JSONResponse({'mess':'Success '},status_code=200)
