from pydantic import BaseModel,Field,EmailStr
from emails import Email
class SignUp(BaseModel):
    username: EmailStr = Field(default=None)
    password : str = Field(default = None)
    REpassword : str  = Field(default = None)

    class Config:
        the_schema = {
            "user_demo": {
                "Username" : "exide",
                "password":"exide@123",
                "REpassword":"exide@123"
            }   
        }    

class Login(BaseModel):

    username :EmailStr = Field(default=None)
    password : str = Field(default = None)
    class Config:
        the_schema = {
            "user_demo": {
                "Username" : "exide",
                "password":"exide@123"
            }   
        }