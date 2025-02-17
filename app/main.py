from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.config import SessionLocal
from app.models import Berita
from app.utils import get_all_news

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/berita/")
def ambil_berita(keyword: str, db: Session = Depends(get_db)):
    berita_baru = get_all_news(keyword)

    for berita in berita_baru:
        if not db.query(Berita).filter(Berita.url == berita["url"]).first():
            new_berita = Berita(
                judul=berita["judul"],
                sumber=berita["sumber"],
                url=berita["url"],
                tanggal=berita["tanggal"],
                isi=berita["isi"],
            )
            db.add(new_berita)

    db.commit()

    return db.query(Berita).all()
