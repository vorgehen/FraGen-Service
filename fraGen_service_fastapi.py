from importlib.resources import contents
from typing import List

from fastapi import FastAPI, HTTPException
import toml
import uvicorn
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from starlette.responses import JSONResponse

import fraGen_langchain

app = FastAPI()
# TODO Dokument Dictionary wird noch nicht gespeichert
#
# TODO collection auch löschen in chromaDB wenn aus Dictionary entfernt
documents = [{"document_id": 1, "document_name":"swebok-v4.pdf"},
             {"document_id": 2, "document_name":"allgemeine-pathologie-humanmedizin-skript.pdf"}]

class Document(BaseModel):
   document_id: int
   document_name: str


class Message(BaseModel):
    message: str

def get_entry_from_list (document_list, entry_id):
    entry = [i for i, j in enumerate(document_list) if j.get('document_id') == entry_id]
    return entry[0]

@app.get("/documents/{document_id}", response_model=Document)
async def read_document(document_id: int):
    try:
        entry = get_entry_from_list(documents, document_id)
        json_compatible_item_data = jsonable_encoder(documents[entry])
        return JSONResponse(content= json_compatible_item_data)
    except IndexError as ie:
        raise HTTPException(status_code=404, detail="Dokument mit ID {document_id} not found")

@app.get("/documents", response_model = List[Document])
async def read_documents():
    json_compatible_item_data = jsonable_encoder(documents)
    return JSONResponse(content= json_compatible_item_data)

def check_document_in_list (document_list, entry_id):
    entry = [i for i, j in enumerate(document_list) if j.get('document_id') == entry_id]

    if entry:
        return True
    else:
        return False

@app.post("/document/{document_id}/{document_name}" , response_model=Document)
async def post_document(document_id:int, document_name:str):
    try:
        entry_exists = check_document_in_list(documents, document_id)
        new_id = max(map(lambda x: x[0], documents)) + 1

        if not entry_exists:
            documents.append({"document_id": document_id, "document_name": document_name})
            entry = get_entry_from_list(documents, document_id)


            doc = fraGen_langchain.document_to_collection(document_name)
            json_compatible_item_data = jsonable_encoder(documents[entry])
            return JSONResponse(content= json_compatible_item_data)
        else:
            raise HTTPException(status_code=405, detail="Document {document_id} exists")
    except IndexError as ie:
        raise HTTPException(status_code=404, detail="Document {document_id} does not exist")
@app.post("/document/{document_name}" , response_model=Document)
async def post_document(document_id:int, document_name:str):
    try:

        new_id = max(map(lambda x: x[0], documents)) + 1
        documents.append({"document_id": new_id, "document_name": document_name})
        entry = get_entry_from_list(documents, document_id)


        doc = fraGen_langchain.document_to_collection(document_name)
        json_compatible_item_data = jsonable_encoder(documents[entry])
        return JSONResponse(content= json_compatible_item_data)

    except IndexError as ie:
        raise HTTPException(status_code=404, detail="Document {new_id} does not exist")
@app.put("/document/{document_id}/{document_name}", response_model=Document)
async def put_document(document_id:int, document_name:str):
    try:
        entry= get_entry_from_list(documents, document_id)
        documents[entry].update({"document_name": document_name})
        doc = fraGen_langchain.document_to_collection(document_name)
        json_compatible_item_data = jsonable_encoder(documents[entry])
        return JSONResponse(content= json_compatible_item_data)
    except IndexError as ie:
        raise HTTPException(status_code=404, detail="Document {document_id} does not exist")

@app.delete("/document/{document_id}", response_model=Message)
async def delete_document(document_id:int):
    try:
        entry = get_entry_from_list(documents, document_id)
        documents.pop(entry)
        return { "message": "Document {document_id} deleted" }
    except IndexError as ie:
        raise HTTPException(status_code=404, detail="Document {document_id} does not exist")
@app.get("/document/{document_id}/{anweisung}",  response_model=Message)
async def ask(document_id:int, anweisung:str):
    try:
        import fraGen_langchain

        entry = get_entry_from_list(documents, document_id)
        json_compatible_item_data = jsonable_encoder(documents[entry])
        doc = json_compatible_item_data["document_name"]
        result = fraGen_langchain.ask_question(doc, anweisung)
        return {"message": result}
    except IndexError as ie:
        raise HTTPException(status_code=404, detail="Document {document_id} does not exist")

if __name__ == "__main__":
    config = toml.load("fraGen_service_config.toml")
    env= config["SETUP"]["env"]
    host = config["PROJECT"][env]["host"]
    port = config["PROJECT"][env]["port"]
    protocol = config["PROJECT"][env]["protocol"]

    print(f"{protocol}://{host}:{port}")
    uvicorn.run(app, host=host, port=port)




