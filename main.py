from enum import Enum
from pydantic import BaseModel
from fastapi import *
from fastapi.staticfiles import StaticFiles
import uvicorn
from starlette.middleware.sessions import SessionMiddleware




class Body(BaseModel):
    name: str
    price: float
    tax: float | None = None

app = FastAPI()

app.add_middleware(SessionMiddleware,https_only=True,secret_key="some-random-string")#to use session stock un id dans un cookie puis garde dans le server les data important lier a cette id gense username :pass
#order est impotant
@app.get("/")
async def root(request:Request,inotsavailable : bool,ismandatory :bool | None = None):
    request.session['test'] = "acher"
    return {"message": inotsavailable}

#@app.get("/{test2}")
#async def PathVar(test2 : str):
#    return {"message2": test2}

@app.get("/{test}")
async def PathVar(request:Request,res:Response,test : str):
    print(request.session['test'])
    return {"message": test}

@app.post("/postMethod",status_code=201)
async def PathVar(postParam : Body):
    return {"message": postParam}


@app.post("/login")
async def login(username: str = Form(), password: str = Form()):
    print(username,password)
    return {}

@app.post("/uploadfiles")
async def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}

@app.post("/uploadfile")
async def create_upload_files(files: UploadFile):
    return {"filenames": [file.filename for file in files]}

app.mount("/static", StaticFiles(directory="static"), name="static")


uvicorn.run(app, port=80)

