from connection import engine
from models.models import  Base

Base.metadata.create_all(engine)
