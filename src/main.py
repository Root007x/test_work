from langchain_groq import ChatGroq
from fastapi import FastAPI, File, UploadFile, APIRouter, HTTPException, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from config.config import GROQ_API_KEY, LLM_MODEL_NAME
from models.preprocessing import Preprocess
from models.score import GenerateScore
from models.rewrite_cv import ReWrite



# # File Location
# PDF_FILE = "data/people_resume.pdf"
# JOB_DES = """ We are looking for a UI/UX Designer with experience in Figma, Adobe XD, and responsive design principles. The candidate should be able to create wireframes,          prototypes, and collaborate closely with developers."""


# 1. Model Setup
# 2. Preprocessing
# 3. score
# 4. rewrite_cv


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




# Fast APi
app = FastAPI()

class JobDescription(BaseModel):
    job_des : str


@app.post("/pdf_upload")
async def pdf_file_upload(
    # file : UploadFile = File(...),
    job_des : JobDescription = Form(...)
):
    
    # if file.content_type != "application/pdf":
    #     raise HTTPException(status_code=400, detail="Only PDF files are Accepted")
    
    # pdf_file = await file.read()
    job_description = job_des
    
    # print(pdf_file)
    print(job_description)
    
    # output = final_call(
    #     pdf_file=pdf_file,
    #     job_des=job_description
    # )
    
    # return JSONResponse({
    #     "File Name" : file.filename,
    #     "result" : output
    # })
    
    return JSONResponse({
        "filename": file.filename,
        "message": "File received"
    })
    
    