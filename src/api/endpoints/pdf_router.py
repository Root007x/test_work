from langchain_groq import ChatGroq
from fastapi import File, UploadFile, APIRouter, HTTPException, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from src.config.config import GROQ_API_KEY, LLM_MODEL_NAME
from src.models.preprocessing import Preprocess
from src.models.score import GenerateScore
from src.models.rewrite_cv import ReWrite


def final_call(pdf_file, job_des):

    # LLM Model Setup
    model = ChatGroq(
        model = LLM_MODEL_NAME,
        api_key=GROQ_API_KEY
    )


    # Preprocessing
    pre_process = Preprocess(
        pdf_file=pdf_file,
        model=model
    )

    pre_process.extract_pdf_data()


    # Score
    gen_score = GenerateScore(model=model)

    score = gen_score.score(job_des=job_des)

    print(score)


    # re-write-cv
    re_write = ReWrite(model=model)

    final_output = re_write.re_write_cv(
                        score=score,
                        job_des=job_des
                )

    return final_output



### FASTAPI
router = APIRouter()

# Pydantic class
class JobDescription(BaseModel):
    job_des : str

# pdf_file API
@router.post("/pdf_upload")
async def pdf_file_upload(
    file : UploadFile = File(...),
    job_des : str = Form(...)
):
    
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are Accepted")
    
    pdf_file = file.file
    job_description = JobDescription(job_des=job_des)
    
    print(pdf_file)
    print(job_description)
    
    output = final_call(
        pdf_file=pdf_file,
        job_des=job_description
    )
    
    return JSONResponse({
        "File Name" : file.filename,
        "result" : output
    })
    
    
