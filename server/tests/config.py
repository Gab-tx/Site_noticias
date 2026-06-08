import pytest 
import tempfile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..app import app
from ..models.models import Base

@pytest.fixture
def client():
    
    app.config["TESTING"] = True
    
    with app.test_client() as client:
        yield client
        
@pytest.fixture
def database():
    db_file = tempfile.NamedTemporaryFile()
    
    engine = create_engine(
        f"sqlite:///{db_file.name}"
    )
    
    Base.metadata.create_all(engine)
    
    yield engine
    
    Base.metadata.create_all(engine)