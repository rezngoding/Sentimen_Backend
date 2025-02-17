from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.config import Base

class Berita(Base):
    __tablename__ = "berita"

    id = Column(Integer, primary_key=True, index=True)
    judul = Column(String, nullable=False)
    sumber = Column(String, nullable=False)
    url = Column(String, nullable=False, unique=True)  # URL unik agar tidak duplikat
    tanggal = Column(DateTime, default=datetime.utcnow)
    isi = Column(Text, nullable=False)
    sentimen = Column(String, default="Belum dianalisis")  # Positif, Netral, Negatif
