import os
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from urllib.parse import quote_plus
from database.models import Base
from threading import Lock
from contextlib import contextmanager


class DBManager:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DBManager, cls).__new__(cls)
                    cls._instance._init_instance()
        return cls._instance

    def _init_instance(self):
        self.engine = None
        self._SessionLocal = None

    def configure_engine(self):
        """
        Configure the database engine
        """
        user = os.getenv("DB_USER", "postgres")
        pwd = quote_plus(os.getenv("DB_PASSWORD", "2005_Gokul"))  # match your Docker password
        name = os.getenv("DB_NAME", "vectordb")                   # match your Docker DB name
        host = os.getenv("DB_HOST", "localhost:5435")             # your new port

        db_url = f"postgresql+psycopg2://{user}:{pwd}@{host}/{name}"
        self.engine = create_engine(db_url, echo=False, pool_size=10, max_overflow=20)
        self._SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def init_db(self):
        """
        Initialize the database and create tables.
        """
        if self.engine is None:
            raise ValueError("Database engine is not configured.")
        Base.metadata.create_all(self.engine)

    def drop_all(self):
        """Delete all tables."""
        if self.engine is None:
            self.configure_engine()
        Base.metadata.drop_all(bind=self.engine)

    @contextmanager
    def session(self) -> Generator[Session, None, None]:
        """
        Provide a transactional scope around a series of operations.
        """
        if self.engine is None:
            self.configure_engine()
        db = self._SessionLocal()
        try:
            yield db
        finally:
            db.commit()
            db.close()
if __name__ == "__main__":
    db_manager = DBManager()
    db_manager.configure_engine()
    db_manager.drop_all()  # Optional: drop all tables if needed
    print("Database engine configured successfully.")
    db_manager.init_db()
    print("Database initialized successfully.")