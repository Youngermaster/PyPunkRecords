from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.routes.files import router as FilesRouter
from fastapi.staticfiles import StaticFiles
from decouple import config

is_production = config("PROJECT_ENVIRONMENT", default="DEVELOPMENT")

if is_production == "RELEASE":
    app = FastAPI(
        docs_url=None,  # Disable docs (Swagger UI)
        redoc_url=None,  # Disable redoc
    )
else:
    app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(FilesRouter, tags=["Files"], prefix="/files")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to PyPunk Records API!"}
