const logado = localStorage.getItem("logado");

if (logado !== "true") {
  window.location.href = "login.html";
}

const logout = document.getElementById("logout");

logout.addEventListener("click", () => {
  localStorage.removeItem("logado");
  window.location.href = "/index.html";
});

async function carregarNoticias() {
  const response = await fetch("http://127.0.0.1:5000/noticias/");
  const responseInativas = await fetch(
    "http://127.0.0.1:5000/noticias/inactive",
  );

  noticias = await response.json();
  noticiasInativas = await responseInativas.json();

  renderNoticias(noticias, noticiasInativas);
}

let noticias = [];
let noticiasInativas = [];

function renderNoticias(noticias, noticiasInativas) {
  const container = document.getElementById("lista-noticias");
  container.innerHTML = "";

  const containerInativo = document.getElementById("lista-noticias-inativa")
  containerInativo.innerHTML = "";

  noticias.forEach((noticia) => {
    const card = document.createElement("article");
    card.classList.add("noticia-card");

    card.innerHTML = `
            <div aria-label="noticias ativas" class="container-noticias-ativas content">

                <h3>${noticia.titulo}</h3>

                <p>${noticia.descricao ?? ""}</p>

                <div class="actions">
                    <button class="edit">
                        Editar
                    </button>

                    <button class="delete" onclick="arquivarNoticia(${noticia.id})">
                        Arquivar
                    </button>
                </div>

            </div>
        `;

    container.appendChild(card);
  });
  noticiasInativas.forEach((noticiaInativa) =>{
    const card = document.createElement("article");
    card.innerHTML = ""
    card.classList.add("noticia-card");

    card.innerHTML = `
    <div aria-label="noticias inativas" class="container-noticias-inativas content">
        <h3>${noticiaInativa.titulo}</h3>

        <p>${noticiaInativa.descricao ?? ""}</p>

        <div class="actions">
            <button class="edit" onclick="desarquivarNoticia(${noticiaInativa.id})">
                Desarquivar
            </button>

            <button class="delete" onclick="deletarNoticia(${noticiaInativa.id})">
                Deletar
            </button>
        </div>
    </div>
    `;

    containerInativo.appendChild(card)
  });
}

async function arquivarNoticia(id) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/noticias/archive/${id}`, {
      method: "PATCH",
    });
    if (!response.ok) {
      throw new Error("Erro ao arquivar noticia");
    }

    await carregarNoticias();
  } catch (error) {
    console.log(error);
    alert(error.message);
  }
}

async function desarquivarNoticia(id) {
    try {
        const response = await fetch(`http://127.0.0.1:5000/noticias/unarchive/${id}`, {
            method: "PATCH",
        });
        if (!response.ok) {
            throw new Error("Erro ao desarquivar noticia");
        }
        await carregarNoticias();
    } catch (error) {
        console.log(error);
        alert(error.message);
    }
}

async function deletarNoticia(id) {
  try {
    const response = await fetch(`http://127.0.0.1:5000/noticias/${id}`, {
      method: "DELETE",
    });
    if (!response.ok) {
      throw new Error("Erro ao excluir noticia");
    }

    await carregarNoticias();
  } catch (error) {
    console.log(error);
    alert(error.message);
  }
}

const formNoticia = document.getElementById("form-noticia");

formNoticia.addEventListener("submit", async (event) => {
  event.preventDefault();

  console.log("Submit disparado");

  const titulo = document.getElementById("titulo").value;
  const subtitulo = document.getElementById("subtitulo").value;
  const descricao = document.getElementById("descricao").value;
  const conteudo = document.getElementById("conteudo").value;
  const idCategoria = Number(document.getElementById("categoria").value);
  const imagemUrl = document.getElementById("imagem").value;
  const noticia = {
    titulo,
    subtitulo,
    descricao,
    conteudo,
    idAdmin: 1,
    idCategoria,
  };

  try {
    const response = await fetch("http://127.0.0.1:5000/noticias/", {
      method: "POST",
      headers: {
        "content-type": "application/json",
      },
      body: JSON.stringify(noticia),
    });
    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.erro || "Erro ao cadastrar notícia");
    }
    alert("Noticia publicada com sucesso!");
    console.log(data);

    formNoticia.reset();
    await carregarNoticias();
  } catch (error) {
    console.error(error);
    alert(error.message);
  }
});

carregarNoticias();
