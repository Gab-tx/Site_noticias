from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy import (
    Integer, String, ForeignKey, Float, DateTime, Boolean,
    Text
)
from datetime import datetime

class Base(DeclarativeBase):
    ...

# Admin ------------------------------------------------------------------------
class Admin(Base):
    __tablename__ = "Admins"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    noticias: Mapped[list["Noticia"]] = relationship(
        back_populates="admin"
    )


# Noticia ------------------------------------------------------------------------
class Noticia(Base):
    """
    id: Mapped[int]
    titulo: Mapped[str]
    subtitulo: Mapped[str]
    descricao: Mapped[str]
    conteudo: Mapped[str]
    data_publicacao: Mapped[datetime]
    data_atualizacao: Mapped[datetime] 
    idAdmin: Mapped[int]
    idCategoria: Mapped[int]
    """
    
    __tablename__ = "Noticias"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    subtitulo: Mapped[str] = mapped_column(String(200), nullable=True)
    descricao: Mapped[str] = mapped_column(String(500), nullable=True)
    conteudo: Mapped[str] = mapped_column(Text(), nullable=False)
    data_publicacao: Mapped[datetime] = mapped_column(DateTime(), default=datetime.now)
    data_atualizacao: Mapped[datetime] = mapped_column(DateTime(), nullable=True, default=datetime.now, onupdate=datetime.now)
    idAdmin: Mapped[int] = mapped_column(Integer(), ForeignKey("Admins.id"))
    idCategoria: Mapped[int] = mapped_column(Integer(), ForeignKey("Categorias.id"))

    admin : Mapped["Admin"] = relationship(
        back_populates="noticias"
    )
    categoria: Mapped["Categoria"] = relationship(
        back_populates="noticias"
    )
    imagem: Mapped[list["Imagem"]] = relationship(
        back_populates="noticia",
        cascade="all, delete-orphan"
    )


# Categoria ------------------------------------------------------------------------ 
class Categoria(Base):
    """
    id: Mapped[int]
    nome = Mapped[str]
    """
    
    __tablename__ = "Categorias"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(100),nullable=False, unique=True)

    noticias: Mapped[list["Noticia"]] = relationship(
        back_populates="categoria"
    )


# Imagem ------------------------------------------------------------------------
class Imagem(Base):
    """
    id: Mapped[int]
    descricao: Mapped[str]
    url: Mapped[str]
    idNoticia: Mapped[int] 
    """
    
    __tablename__ = "Imagens"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descricao: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(String(500), nullable=False, unique=True)
    idNoticia: Mapped[int] = mapped_column(Integer(), ForeignKey("Noticias.id"))
    
    noticia: Mapped["Noticia"] = relationship(
        back_populates="imagens"
    )