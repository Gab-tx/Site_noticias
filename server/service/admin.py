from sqlalchemy import select

from connection import SessionLocal
from models.models import Admin

class AdminService:
    
    @classmethod
    def create(cls, dados:dict):
        with SessionLocal() as session:
            
            admin = Admin(**dados)
            
            session.add(admin)
            session.commit()
            session.refresh(admin)
            
            return admin
        
    @classmethod
    def select_all(cls):
        with SessionLocal() as session:
            
            return session.scalars(select(Admin)).all()
        
    @classmethod
    def select_by_id(cls, id:int):
        with SessionLocal() as session:
            
            return session.get(Admin, id)
        
    @classmethod
    def select_by_email(cls, email:str):
        with SessionLocal() as session:
            
            stmt = select(Admin).where(Admin.email == email)
            
            return session.scalar(statement=stmt)
        
    @classmethod
    def delete(cls, id:int):
        with SessionLocal() as session:
            
            admin = session.get(Admin, id)
            if not admin:
                return False
            
            session.delete(admin)
            session.commit()
                        
            return True
