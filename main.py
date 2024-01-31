from app.auth.jwt_handler import *
from app.models import SignUp,Login
from db import *
from fastapi import FastAPI, Request,Body,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(request=request, name="sign_up.html")

@app.post("/user/signup")
def user_signup(user :  SignUp=Body):
    id =create_for_userdetails_db(user)
    print(id)


# @app.get("/")
# def root():
#     return {"data":"Hello Exide"}

# @app.post("/user/signup")
# def user_signup(user :  SignUp=Body):
#     id =create_for_userdetails_db(user)
    

# def check_user(credentials: Login):
#     user = collection2.find_one({"email": credentials.email, "password": credentials.password})
#     return user is not None
    
# @app.post("/user/login")
# def user_login(user: Login):
#     if check_user(user):
#         return signJWT(user.email)
#     else:
#         return{ "error":"Invalid login details!"}