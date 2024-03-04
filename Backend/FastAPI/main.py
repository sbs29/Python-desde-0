# Para ejecutar el server usa (python -m uvicorn main:app --reload)
# Para parar el server usa (Ctrl + C)

# Documentacion online con swagger      http://127.0.0.1:8000/docs
# Documentacion online con redocli      http://127.0.0.1:8000/redoc

from fastapi import FastAPI
from routers import products
from routers import users
from routers import basic_auth_users
from routers import jwt_auth_users
from routers import user_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

app.include_router(user_db.router)

app.mount("/static",StaticFiles(directory="static"), name="static")

# url local http://127.0.0.1:8000
@app.get("/")   # ("/") es la ruta a la raiz solo una peticion get
async def root():
    return {"message": "Hola python"}

# url local http://127.0.0.1:8000/url
@app.get("/url")
async def url():
    return {"url_curso":"https://mouredev.com/python"}


