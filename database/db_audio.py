from router.shemas import AudioBase
from sqlalchemy.orm.session import Session
import datetime
from database.models import Dbaudio
from fastapi import HTTPException, status

def create(db: Session, audio_data: AudioBase):
    
    new_audio=Dbaudio(
    audio= audio_data,
    timestamp= datetime.datetime.now()
    )
    db.add(new_audio)
    db.commit()
    db.refresh(new_audio)
    return new_audio

def get_all(db: Session):
    return db.query(Dbaudio).all()

def get_by_id(id: int, db: Session):
    post = db.query(Dbaudio).filter(Dbaudio.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Audio with id {id} not found.")
    return post


def delete(id:int, db:Session):
    post = db.query(Dbaudio).filter(Dbaudio.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found.")
    db.delete(post)
    db.commit()
    return 'ok'