from fastapi import APIRouter, HTTPException
from server.models.response import ResponseModel, ErrorResponseModel
from typing import List

router = APIRouter()

# Dummy Data - this would eventually be replaced by actual file storage logic
files = ["shakira.mp3", "file1.txt", "file2.txt", "image1.png"]


@router.get("/", response_description="List all files in the directory")
async def list_files() -> dict:
    """
    Endpoint to list available files.
    """
    if files:
        return ResponseModel(files, "Files retrieved successfully")
    return ErrorResponseModel("An error occurred", 404, "Files were not found.")


@router.post("/{file_name}", response_description="Upload a file from the client")
async def upload_file(file_name: str) -> dict:
    """
    Dummy endpoint to simulate file upload.
    """
    # In real implementation, you would save file to disk or process it.
    # Assuming the dummy upload is always successful for the example:
    try:
        files.append(file_name)
        return ResponseModel(file_name, "File uploaded successfully")
    except Exception as e:
        return ErrorResponseModel(e, 400, "An error occurred uploading the file.")


@router.get(
    "/download/{file_name}", response_description="Download a file from the server"
)
async def download_file(file_name: str) -> dict:
    """
    Dummy endpoint to simulate file download.
    """
    # In real implementation, you would fetch the file and return its content.
    # Check if the file is in our dummy list
    if file_name in files:
        # Simulate a successful download response
        return ResponseModel(file_name, "File downloaded successfully")
    # File isn't in our dummy list, so return an error response
    return ErrorResponseModel("An error occurred", 404, "File not found.")
