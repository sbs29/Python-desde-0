from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "fa990e3cc519b21f1514dd4e6aefd7b5" # num hex 32

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "sebas":{
        "username":"sebas",
        "fullname":"Sebastian Solano",
        "email":"sbs@sbs.com",
        "disabled":False,
        "password":"$2y$12$Cx.ID9a/WN76w4lGa5RMZ.wFvWzKeukqIo.nIcGXGrBad5cmKxCte"
    },
    "sbs2":{
        "username":"jose",
        "fullname":"Sebastian Buitrago",
        "email":"sbs2@sbs.com",
        "disabled":True,
        "password":"$2a$12$qcJctYFh4UOvjWOMlRlcUOvCm0YeAOBk7.7BdRB7IEnNyWXijH64q"
    }
}

def search_user_db(username: str):
    for username in users_db:
        return UserDB(**users_db[username])     # ** multiples parametros
    
def search_user(username: str):
    for username in users_db:
        return User(**users_db[username])

async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas", 
        headers={"WWW-Authenticate":"Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=ALGORITHM).get("sub")
        if username is None:
            raise exception
    except JWTError:
        raise exception
    
    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Usuario invalido")
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto")
    
    user = search_user_db(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta")

    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user