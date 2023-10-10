# from fastapi import 
from fastapi.responses import JSONResponse
from model.user import *
from Core.db import *
from fastapi import FastAPI, APIRouter
from fastapi import HTTPException, requests
import json, pydantic



router = APIRouter()

@router.post("/contact", response_model=dict)
async def contact_form(contact: Contact):  
    # Check if an entry with the same email exists in the database
    existing_contact = contactdb.find_one({"Email": contact.email})  
    if existing_contact:
        return JSONResponse({'error': 'Same email'}, status_code=400)   
    # Create a dictionary to insert into the database
    data = {
        'Name': contact.name,
        'Email': contact.email,
        'Phone': contact.phone,
        'Message': contact.message
    }   
    # Insert the data into the database
    contactdb.insert_one(data)    
    return JSONResponse({'message': 'Contact Saved'}, status_code=200)


@router.post("/user/join", response_model=dict)
async def join_user(join: Join):
    try:
        allowed_genders = ['male', 'female', 'other']
        if join.gender.lower() not in allowed_genders:
            return JSONResponse({'error': 'Invalid gender'}, status_code=400)
        join_data = {
            'First Name': join.fname,
            'Last Name': join.lname,
            'Gender': join.gender,
            'About': join.about
        }
        joindb.insert_one(join_data)
        # Here, we're just returning the data as a response
        return JSONResponse({'message': 'Join request submitted successfully', 'data': join_data}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/donation", response_model=dict)
async def donation_form(donation: Donation):  
    if donation.amount <= 0:
        return JSONResponse({'error': 'Same email'}, status_code=400)    
    data = {
        'Name': donation.name,
        'Email': donation.email,
        'Phone': donation.phone,
        'Amount': donation.amount
    }    
    donationdb.insert_one(data)    
    return JSONResponse({'message': 'Contact Saved'}, status_code=200)

