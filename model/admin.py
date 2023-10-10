from pydantic import BaseModel, Field
from typing import Optional

class Contact(BaseModel):
    username:str = Field(...,description='Enter Your name',example='Abcd')
    password:str = Field(...,description='Enter your email',example='abc@gmail.com')