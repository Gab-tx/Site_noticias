from models.models import Noticia
from connection import SessionLocal

class NoticiaService:
    
    @classmethod
    def create(cls, noticia:dict):
        with SessionLocal() as session:
            obj_noticia = Noticia(**noticia)

            session.add(obj_noticia)
            session.commit()
            session.refresh(obj_noticia)
            
            return obj_noticia
        
    @classmethod
    def select_all(cls):
        with SessionLocal() as session:
            return session.query(Noticia).filter(Noticia.ativo == True).all()

    @classmethod
    def select_all_inactive(cls):
        with SessionLocal() as session:
            return session.query(Noticia).filter(Noticia.ativo == False).all()
        
    @classmethod
    def select_by_id(cls, id:int):
        with SessionLocal() as session:
            return session.query(Noticia).filter(Noticia.id == id).filter(Noticia.ativo == True).first()
        
    @classmethod
    def select_by_categoria(cls, categoria:str):
        with SessionLocal() as session:
            return session.query(Noticia).where(Noticia.categoria == categoria).filter(Noticia.ativo == True).all()
        
    @classmethod
    def select_by_title(cls, titulo:str):
        with SessionLocal() as session:
            return session.query(Noticia).where(Noticia.title == titulo).filter(Noticia.ativo == True).all()
        
    @classmethod
    def update(cls, id:int, dados:dict):
        with SessionLocal() as session:
            noticia = session.query(Noticia).filter(Noticia.id == id).first()
            
            if not noticia:
                raise ValueError("Notícia não encontrada")
            
            for campo, valor in dados.items():
                setattr(noticia, campo, valor)
                
            session.commit()
            session.refresh(Noticia)
            
            return Noticia
        
    @classmethod
    def delete(cls, id:int):
        with SessionLocal() as session:
            noticia = session.query(Noticia).filter(Noticia.id == id).first()
            if not noticia:
                raise ValueError("Noticia não encontrada")
            
            session.delete(noticia)
            session.commit()
            
            return "Notícia deletada com sucesso"
        
    @classmethod
    def soft_delete(cls, id:int):
        with SessionLocal() as session:
            
            noticia = session.query(Noticia).filter(Noticia.id == id).first()
            if not noticia:
                raise ValueError("Noticia não encontrada")
            
            noticia.ativo = False
            
            session.commit()
            
            return noticia
        
    @classmethod
    def unarchive(cls, id:int):
        with SessionLocal() as session:

            noticia = session.query(Noticia).filter(Noticia.id == id).first()
            if not noticia:
                raise ValueError("Noticia não encontrada")

            noticia.ativo = True

            session.commit()

            return noticia
            