from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/upload_pdf")
async def upload_file(file : UploadFile = File(...)):
    
    print(await file.read())
