from faker import Faker
from random import randint, choice
from connection import SessionLocal
from models.models import (
    Admin,
    Categoria,
    Noticia,
    Imagem
)

faker = Faker("pt_BR")

categorias_padrao = [
    "Tecnologia",
    "Ciência",
    "Agronegócio",
    "Política",
    "Economia",
    "Educação",
    "Saúde",
    "Meio Ambiente",
    "Esportes",
    "Cultura"
]

with SessionLocal() as session:
    admin = Admin(
        nome="Admin",
        email="admin@gmail.com",
        senha_hash="123456"
    )

    session.add(admin)
    session.commit()
    
    categorias = []

    for nome in categorias_padrao:

        categoria = Categoria(
            nome=nome
        )

        session.add(categoria)
        categorias.append(categoria)

    session.commit()