from fastapi import FastAPI, status, HTTPException
from typing import Optional, List
from fastapi.responses import JSONResponse
from models.Developer import Developer
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
import motor.motor_asyncio

app = FastAPI()
developers = []

async def connection():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://127.0.0.1:27017")
    db = client["bdbeta"]
    return db


@app.get("/developers")
async def get_developers():
    try:
        db = await connection()
        developers = await db.developers.find().to_list(1000)
        for developers in developers:developers["_id"] = str(developers["_id"])
        return JSONResponse(status_code=200, content={"data": developers})
    except Exception as error:
        print(error)
        return JSONResponse(status_code=500, content={"message": "Ha ocurrido un error"})


@app.post("/developers")
async def create_developer(developer: Developer):
    try:
        db = await connection()
        await db.developers.insert_one(jsonable_encoder(developer))
        return JSONResponse(status_code=201, content={"message": "Registro Ingresado"})
    except:
        return JSONResponse(status_code=500, content={"message": "Error al ingresar el registro"})


@app.put("developers")
async def update_developer(data: Developer, id: str):
    try:
        db = await connection()
        developer = await db.developer.find_one({"_id":ObjectId(id)})
        if not developer:
            return JSONResponse(status_code=400, content={"message": "No se encontro el registro"})
        await db.developer.update_one({"_id": ObjectId(id)},{"$set":jsonable_encoder(data)})
    except Exception as error:
        return JSONResponse(status_code=500, content={"message": "Error al actualizar el registro"})
    

@app.delete("/developers/{developer_id}")
async def delete_developer(developer_id: str):
    try:
        db = await connection()
        result = await db.developers.delete_one({"_id": ObjectId(developer_id)})
        
        if result.deleted_count == 0:
            return JSONResponse(status_code=404, content={"message": "No se encontró el registro"})
        
        return JSONResponse(status_code=200, content={"message": "Registro eliminado"})
    except Exception as error:
        return JSONResponse(status_code=500, content={"message": "Error al eliminar el registro"})
    

@app.get("/developers/{developer_id}")
async def get_developer_by_id(developer_id: str):
    try:
        db = await connection()
        developer = await db.developers.find_one({"_id": ObjectId(developer_id)})
        
        if not developer:
            return JSONResponse(status_code=404, content={"message": "No se encontró el desarrollador"})
        
        # Convertir el ObjectId a una cadena para que sea serializable en JSON
        developer["_id"] = str(developer["_id"])
        
        return JSONResponse(status_code=200, content={"data": developer})
    except Exception as error:
        return JSONResponse(status_code=500, content={"message": "Error al buscar el desarrollador"})
