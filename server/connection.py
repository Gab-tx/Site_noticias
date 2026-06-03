from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = ""

engine = create_engine(
    DATABASE_URL,
    connect_args={
        "sslmode": "require"
    },
    echo=True
    
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
) 