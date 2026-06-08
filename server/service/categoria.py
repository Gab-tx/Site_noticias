from sqlalchemy import select

from connection import SessionLocal
from models.models import Categoria

class CategoriaService:
    
    @classmethod
    def create(cls, dados:dict):
        with SessionLocal() as session:
            obj_categoria = Categoria(**dados)
            
            session.add(obj_categoria)
            session.commit()
            session.refresh(obj_categoria)
            
            return obj_categoria
        
    @classmethod
    def select_all(cls):
        with SessionLocal() as session:
            
            return session.scalars(select(Categoria).all())
        
    @classmethod
    def select_by_id(cls, id:int):
        with SessionLocal() as session:
            
            return session.get(Categoria, id)
    
    @classmethod
    def update(cls, id:int, dados:dict):
        with SessionLocal() as session:
            
            categoria = session.get(Categoria, id)
            if not categoria:
                raise None
            
            for campo, valor in dados.items():
                setattr(Categoria, campo, valor)
                
            session.commit()
            session.refresh(Categoria)
            
            return Categoria
        
    @classmethod
    def delete(cls, id:int):
        with SessionLocal() as session:
            
            categoria = session.get(Categoria, id)
            if not categoria:
                return False
            
            session.delete(categoria)
            session.commit()
            
            return True