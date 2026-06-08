from sqlalchemy import select
from connection import SessionLocal
from models.models import Imagem

class ImagemService:
    
    @classmethod
    def create(cls, dados:dict):
        with SessionLocal() as session:
            imagem = Imagem(**dict)
            
            session.add(imagem)
            session.commit()
            session.refresh(imagem)
            
            return imagem
        
    @classmethod
    def select_all(cls):
        with SessionLocal() as session:
            
            return session.scalars(select(Imagem).all())
        
    @classmethod
    def select_by_id(cls, id:int):
        with SessionLocal() as session:
            
            return session.get(Imagem, id)
        
    @classmethod
    def select_by_noticia(cls, noticia_id:int):
        with SessionLocal() as session:
            
            stmt = select(Imagem).where(Imagem.idNoticia == noticia_id)
            
            return session.scalars(stmt).all()
        
    @classmethod
    def delete(cls, id:int):
        with SessionLocal() as session:
            
            imagem = session.get(Imagem, id)
            if not imagem:
                return False
            
            session.delete(imagem)
            session.commit()
                        
            return True