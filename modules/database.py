import os

from sqlmodel import Session, create_engine

engine = create_engine(os.getenv("DATABASE_URL", "sqlite:///database.db"), echo=False)


def get_session():
    """Provide a transactional SQLAlchemy session."""
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    """Create database tables based on SQLModel definitions."""
    from sqlmodel import SQLModel  # noqa: PLC0415

    SQLModel.metadata.create_all(engine)
