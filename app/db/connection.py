from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONNECTION_URL = "sqlite:///../../app.db"
engine = create_engine(CONNECTION_URL)
Base = declarative_base(bind=engine)
SessionLocal = sessionmaker(bing=engine)
