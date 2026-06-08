from flask import Blueprint, request, jsonify
from ..service.categoria import CategoriaService

categoria_bp = Blueprint(
    "categorias",
    __name__,
    url_prefix="/categoria"
)

categoria_bp.get("/")
def select_all():
    
    categorias = CategoriaService.select_all()

    resultado = []
    
    for categoria in categorias:
        resultado.append({
            "id": categoria.id,
            "nome": categoria.nome
        })
        
    return jsonify({
        "message":"Categorias encontradas",
        "dados": resultado
    })

categoria_bp.post("/")
def create():
    
    dados = request.get_json()
    
    categoria = CategoriaService.create(dados)
    
    resultado = {
        "id": categoria.id,
        "nome": categoria.nome
        }
    
    return jsonify({
        "message": "Categoria criada com sucesso",
        "dados": resultado
    })

categoria_bp.delete("/<int:id>")
def delete(id):
    
    categoria = CategoriaService.delete(id)
    if not categoria:
        return jsonify({
            "message": "Categoria não encontrada"
        })
    
    return jsonify({
        "message": "Categoria removida com sucesso."
    })