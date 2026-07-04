from fastapi import FastAPI, UploadFile, File
from cv_parser import extract_text_from_pdf
from ai_resume_parser import parse_resume
import shutil

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = extract_text_from_pdf(f"uploads/{file.filename}")
    resume_json = parse_resume(text)
    return {"resume": resume_json}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
