from pydantic import BaseModel, Field
from typing import Optional


class Contact(BaseModel):
    name:str = Field(...,description='Enter Your name',example='Abcd')
    email:str = Field(...,description='Enter your email',example='abc@gmail.com')
    phone:str = Field(...,description='Enter Your phone no.',example='9876543210')
    message:str = Field(...,description='Enter your message',example='hiiii')

class Join(BaseModel):
    fname: str = Field(..., description='Enter your First Name', example='Abcd')
    lname: str = Field(..., description='Enter your Last Name', example='xyz')
    gender: str = Field(..., description='Enter Your Gender (male/female/others)', example='male')
    about: str = Field(..., description='Enter your message', example='dcfvgbhnj')


class Donation(BaseModel):
    name:str = Field(...,description='Enter your Name',example='abcs')
    email:str = Field(...,description='Enter your email',example='abc@gmail.com')
    phone:str = Field(...,description="Enter your Phone ",example='3456789087')
    amount:float = Field(...,description="Enter your amount",example=100.00)