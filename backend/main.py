from fastapi import FastAPI, UploadFile, File
from cv_parser import extract_text_from_pdf
from ai_resume_parser import parse_resume
from resume_analyzer import analyze_resume
from job_matcher import match_resume_to_job
import shutil

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = extract_text_from_pdf(f"uploads/{file.filename}")
    resume_json = parse_resume(text)
    analysis = analyze_resume(resume_json)
    return {f"filename": file.filename, "resume": resume_json, "analysis": analysis}

@app.post("/job-match")
async def job_match(file: UploadFile = File(...),
    job_description: str = Form(...)
):
    resume_json = parse_resume(text)

    match = match_resume_to_job(resume_json,job_description)

    return {"resume": resume_json, "job_match": match}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
