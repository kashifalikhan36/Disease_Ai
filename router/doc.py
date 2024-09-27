from fastapi import APIRouter, File, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from database.database import get_db
from datetime import datetime
from pydantic import BaseModel
from datetime import datetime
from bless import Bless_ai

router = APIRouter(
    prefix="/audio",
    tags=["Audio"]
)

class AudioUploadResponse(BaseModel):
    id: int
    timestamp: datetime

class AudioCreate(BaseModel):
    audio: bytes



@router.post("/upload")
async def upload_audio(audio: bytes = File(...), db: Session = Depends(get_db)):
    with open("audios/input.wav", "wb") as audio_file:
        audio_file.write(audio)
    Bless_ai()
    

@router.get("/get")
async def get_audio():
    return FileResponse("audios/output.wav", media_type="audio/mpeg")