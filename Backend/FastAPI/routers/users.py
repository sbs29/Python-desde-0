from fastapi import APIRouter, HTTPException
from pydantic import BaseModel


router = APIRouter()

# BaseModel nos permite crear una entidad
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1,name="Sebas",surname="Solano",url="https:/youtube.com",age=28),
            User(id=2,name="Juan",surname="Buitrago",url="https:/google.com",age=26),
            User(id=3,name="Yolanda",surname="Garcia",url="https:/tiktok.com",age=24)]

# Iniciar server: python -m uvicorn users:app --reload
@router.get("/usersjson")
async def usersjson():
    return [{"name": "Sebastian", "surname": "Solano", "url":"http://google.es", "age": 28},
            {"name": "Juan", "surname": "Buitrago", "url":"http://youtube.es","age": 22},
            {"name": "Yolanda", "surname": "Garcia", "url":"http://tiktok.es","age": 24}]

### GET
# forma para listar los usuarios
@router.get("/users")
async def users():
    return users_list

# forma para buscar user por id (Path)
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# forma para buscar user por id (Query)
@router.get("/user/")
async def user(id:int):
    return search_user(id)
    
def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}

### POST
# forma de insertar un nuevo user
@router.post("/user/", status_code=201)    # Status code manual forma 1
async def user(user: User):
    if type(search_user(user.id)) == User: 
        raise HTTPException(status_code=204, detail="Ya existe el usuario")     
        # Status code manual forma 2 (uso de raise para lanzar exception)
    else:
        users_list.append(user)
        return user

### PUT para actualizar el user completo
### PATCH para actualizar una parte del user
# forma de actualizar un registro
@router.put("/user/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

    if not found:
        return {"error":"No se ha podido actualizar el usuario"}
    else:
        return user
    
### DELETE para eliminar un user
@router.delete("/user/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            return {"info":"Usuario eliminado correctamente"}


    if not found:
        return {"error":"No se ha podido eliminar el usuario"}
