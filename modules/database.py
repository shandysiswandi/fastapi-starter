from sqlmodel import create_engine, Session

DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/fastapi"
engine = create_engine(DATABASE_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def create_db_and_tables():
    from modules.product.model import Product
    from sqlmodel import SQLModel

    SQLModel.metadata.create_all(engine)
