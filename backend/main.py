from fastapi import FastAPI, UploadFile, File
from cv_parser import extract_text_from_pdf
import shutil

app = FastAPI()

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    return {"filename": file.filename}
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = extract_text_from_pdf(f"uploads/{file.filename}")
    return {"text": text, "filename": file.filename}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
