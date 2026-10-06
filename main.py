from fastapi import FastAPI, Request, UploadFile, File
from typing import Optional

app = FastAPI()

@app.get("/")
def health():
    return {
        "status": "OK",
        "message": "HelpNow File Test API"
    }


@app.post("/api/test")
async def test_request(request: Request):
    """
    HelpNow에서 어떤 요청이 오는지 확인하기 위한 API
    """
    body = await request.body()

    return {
        "success": True,
        "contentType": request.headers.get("content-type"),
        "contentLength": len(body),
        "bodyPreview": body[:1000].decode("utf-8", errors="replace")
    }


@app.post("/api/upload")
async def upload_file(
    file: UploadFile = File(...)
):
    """
    multipart/form-data 파일 업로드 테스트
    """
    content = await file.read()

    return {
        "success": True,
        "fileName": file.filename,
        "contentType": file.content_type,
        "fileSize": len(content)
    }