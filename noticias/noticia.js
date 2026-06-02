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
          <div id="not-found">
               <h1>Notícia não encontrada</h1>
               <p>A notícia solicitada não existe ou foi apagada.</p>
               <img src="/img/not.png" alt="Um X indicando negação"></img>
          </div>`;
          return;
     }

     const imagem = dados.imagem.find(img => img.idNoticia === id);

     const texto = noticia.conteudo.split(".").filter(Boolean).map(paragrafo => `<p>${paragrafo.trim()}.</p>`).join("");

     document.getElementById("noticia").innerHTML = `
          <section>
               <div id="titulo-container">
                    <h1 id="titulo">${noticia.titulo}</h1>
                    <p id="descricao">${noticia.descricao}</p>

                    <p id="data" >Atualizado em ${new Date(noticia.data_atualizacao).toLocaleDateString("pt-BR", { day: "2-digit", month: "long", year: "numeric" })}</p>
               </div>

               <div id="imagem-container">
                    <img src="${imagem?.url}" alt="${imagem?.descricao || noticia.titulo}" id="imagem">
               </div>

               <article id="conteudo">
                    ${texto}
               </article>
          </section>`;
};

carregarNoticia();