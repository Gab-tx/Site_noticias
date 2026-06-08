def test_fluxo_noticia(client):

    categoria = client.post(
        "/categorias/",
        json={
            "Nome": "Tecnologia"
        }
    )
    
    admin = client.post(
        "/admins/",
        json={
            "nome": "Gabriel",
            "email": "gabriel@email.com",
            "senha_hash": "123"
        }
    )
    
    noticia = client.post(
        "/noticias/",
        json={
            "titulo": "Teste",
            "conteudo": "Conteúdo",
            "idAdmin": 1,
            "idCategoria": 1
        }
    )
    
    assert noticia.status_code == 201
    
    resposta = client.get(
        "/noticias/1"
    )
    
    assert resposta.status_code == 200
    assert resposta.json["titulo"] == "Teste"