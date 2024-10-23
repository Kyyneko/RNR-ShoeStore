import os

class Config:
    # Mengatur jalur ke database SQLite
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    INSTANCE_PATH = os.path.join(BASE_DIR, 'instance')
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(INSTANCE_PATH, "site.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
