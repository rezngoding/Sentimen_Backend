from app.config import engine, Base

# Buat tabel dalam database
def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
    print("✅ Database & tabel berhasil dibuat!")
