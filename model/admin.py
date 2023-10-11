from pydantic import BaseModel, Field
from typing import Optional


class Register(BaseModel):
    name: str = Field(...,description="Enter tou name",example="sherta")
    username:str = Field(...,description="Enter your user name",example="sherta123")
    password: str= Field(...,description="Enter Your password",example="sherta123@")
    cpassword : str = Field(...,description="Enter your Confim Password",example="sherta123@")


class Login(BaseModel):
    username:str = Field(...,description='Enter Your name',example='user')
    password:str = Field(...,description='Enter your email',example='123456')


   