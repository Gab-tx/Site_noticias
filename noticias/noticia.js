async function carregarNoticia() {
     const params = new URLSearchParams(window.location.search);
     const id = Number(params.get("id"));
     console.log("ID da notícia:", id);

     const response = await fetch("../mockup.json");
     const dados = await response.json();
     console.log("Dados carregados:", dados);
     const noticia = dados.noticia.find(n => n.idNoticia === id);

     if (!noticia) {
          document.getElementById("noticia").innerHTML = `
          <div>
               <h1>Notícia não encontrada</h1>
               <p>A notícia solicitada não existe.</p>
          </div>`;
          return;
     }

     const imagem = dados.imagem.find(img => img.idNoticia === id);

     document.getElementById("noticia").innerHTML = `
          <section>
               <h1 id="titulo">${noticia.titulo}</h1>
               <p id="descricao">${noticia.descricao}</p>
               <img src="${imagem?.url}" alt="${imagem?.descricao || noticia.titulo}" id="imagem">
               <article id="conteudo">
                    ${noticia.conteudo}
               </article>
          </section>`;
};

carregarNoticia();