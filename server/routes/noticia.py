from flask import Blueprint, request, jsonify
from service.noticia import NoticiaService

noticia_bp = Blueprint(
    "noticias",
    __name__,
    url_prefix="/noticias"
)

@noticia_bp.get("/")
def select_all():
    noticias = NoticiaService.select_all()
    
    resultado = []
    
    for noticia in noticias:
        resultado.append({
            "id":noticia.id,
            "titulo":noticia.titulo,
            "subtitulo":noticia.subtitulo,
            "descricao": noticia.descricao,
            "conteudo": noticia.conteudo,
            "data_publicacao": noticia.data_publicacao,
            "data_atualizacao": noticia.data_atualizacao,
            "idAdmin": noticia.idAdmin,
            "idCategoria": noticia.idCategoria
        })
        
    return jsonify(resultado), 200

@noticia_bp.get("/inactive")
def select_all_inactive():
    noticias = NoticiaService.select_all_inactive()
        
    resultado = []
        
    for noticia in noticias:
        resultado.append({
            "id":noticia.id,
            "titulo":noticia.titulo,
            "subtitulo":noticia.subtitulo,
            "descricao": noticia.descricao,
            "conteudo": noticia.conteudo,
            "data_publicacao": noticia.data_publicacao,
            "data_atualizacao": noticia.data_atualizacao,
            "idAdmin": noticia.idAdmin,
            "idCategoria": noticia.idCategoria
        })
        
    return jsonify(resultado), 200


@noticia_bp.get("/<int:noticia_id>")
def select_by_id(noticia_id):
        noticia = NoticiaService.select_by_id(noticia_id)
        
        if not noticia:
            return jsonify({
                "erro": "Noticia não encontrada"
            }), 404
            
        return jsonify({
            "id":noticia.id,
            "titulo":noticia.titulo,
            "subtitulo":noticia.subtitulo,
            "descricao": noticia.descricao,
            "conteudo": noticia.conteudo,
            "data_publicacao": noticia.data_publicacao,
            "data_atualizacao": noticia.data_atualizacao,
            "idAdmin": noticia.idAdmin,
            "idCategoria": noticia.idCategoria
        })
        
@noticia_bp.post("/")
def create():
    
    dados = request.get_json()
    
    noticia = NoticiaService.create(dados)
    
    return jsonify({
        "message":"Notícia criada",
        "id": noticia.id
    }), 201

@noticia_bp.put("/<int:noticia_id>")
def update(noticia_id):
    
    dados = request.json()
    
    noticia = NoticiaService.update(noticia_id, dados)
    
    if not noticia: 
        return jsonify({
            "erro": "Noticia não encontrada"
        }), 404
        
    return jsonify({
        "message": "Notícia atualizada"
    })
    
@noticia_bp.delete("/<int:noticia_id>")
def delete(noticia_id):
    
    noticia = NoticiaService.soft_delete(noticia_id)
    if not noticia:
        return jsonify({
            "erro": "noticia não encontrada"
        })
    return jsonify({
        "message": "Noticia removida"
    })
@noticia_bp.patch("/<int:noticia_id>")
def unarchive(noticia_id):

    noticia = NoticiaService.unarchive(noticia_id)
    if not noticia:
        return jsonify({
            "erro": "noticia não encontrada"
        })
    return jsonify({
        "message": "Noticia desarquivada"
    })