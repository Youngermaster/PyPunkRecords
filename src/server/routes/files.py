from fastapi import APIRouter, Body, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

router = APIRouter()

# Dummy Data
files = ["file1.txt", "file2.txt", "image1.png"]


@router.get("/files", response_description="List all files in the directory")
async def list_files() -> List[str]:
    """
    Endpoint to list available files.
    """
    return files


@router.post("/upload", response_description="Upload a file from the client")
async def upload_file(file_name: str):
    """
    Dummy endpoint to simulate file upload.
    """
    # In real implementation, you would save file to disk or process it.
    return {"status": "success", "filename": file_name}


@router.get("/download/{file_name}", response_description="Download a file from the server")
async def download_file(file_name: str):
    """
    Dummy endpoint to simulate file download.
    """
    # In real implementation, you would fetch the file and return its content.
    return {"status": "success", "filename": file_name}
