from flask import Blueprint, request, jsonify
from ..service.admin import AdminService

admin_bp = Blueprint(
    "admins",
    __name__,
    url_prefix="/admin"
)

@admin_bp.get("/email/<str:email>")
def select_by_email(email):
    
    admin = AdminService.select_by_email(email)
    
    resultado = {
        "id": admin.id,
        "nome": admin.nome,
        "email": admin.email
    }
    
    if not admin:
        return jsonify({
                "erro": "Admin não encontrado"
            }),404
        
    return jsonify({
        "message": "Admin encontrado",
        "dados": resultado
    })

@admin_bp.post("/")
def create():
    
    dados = request.get_json()
    
    admin = AdminService.create(dados)
    
    resultado = {
        "id": admin.id,
        "nome": admin.nome,
        "email": admin.email
    }
    
    return jsonify({
        "message": "Admin criado com sucesso",
        "dados": resultado
    })

@admin_bp.delete("/<int:id>")
def delete(id):
    
    admin = AdminService.delete(id)
    
    if not admin:
        return jsonify({
            "message": "Admin não encontrado"
        })
        
    return jsonify({
        "message": "Admin removido com sucesso"
    })
