from flask import Blueprint, request, jsonify
from ..service.imagem import ImagemService

imagem_bp = Blueprint(
    "imagens",
    __name__,
    url_prefix="/imagem"
)

@imagem_bp.get("/")
def select_all():

    imagens = ImagemService.get_all()

    return jsonify([
        {
            "id": img.id,
            "descricao": img.descricao,
            "url": img.url,
            "idNoticia": img.idNoticia
        }
        for img in imagens
    ])
    
@imagem_bp.get("/<int:imagem_id>")
def select_by_id(imagem_id):

    imagem = ImagemService.get_by_id(
        imagem_id
    )

    if not imagem:
        return jsonify({
            "erro": "Imagem não encontrada"
        }), 404

    return jsonify({
        "id": imagem.id,
        "descricao": imagem.descricao,
        "url": imagem.url,
        "idNoticia": imagem.idNoticia
    })
    
@imagem_bp.get("/noticia/<int:noticia_id>")
def get_by_noticia(noticia_id):

    imagens = ImagemService.get_by_noticia(
        noticia_id
    )

    return jsonify([
        {
            "id": img.id,
            "descricao": img.descricao,
            "url": img.url
        }
        for img in imagens
    ])

@imagem_bp.post("/")
def create():

    dados = request.get_json()

    imagem = ImagemService.create(
        dados
    )

    return jsonify({
        "mensagem": "Imagem criada",
        "id": imagem.id
    }), 201

@imagem_bp.delete("/<int:imagem_id>")
def delete(imagem_id):

    sucesso = ImagemService.delete(
        imagem_id
    )

    if not sucesso:
        return jsonify({
            "erro": "Imagem não encontrada"
        }), 404

    return jsonify({
        "mensagem": "Imagem removida"
    })