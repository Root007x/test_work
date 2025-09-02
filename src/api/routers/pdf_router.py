from fastapi import FastAPI, File, UploadFile, APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel



router = APIRouter()

class JobDescription(BaseModel):
    job_des : str


@router.post("/pdf_upload")
async def pdf_file_upload(
    file : UploadFile = File(...),
    job_des : JobDescription
):
    
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are Accepted")
    
    pdf_file = await file.read()
    job_description = job_des
    
    
