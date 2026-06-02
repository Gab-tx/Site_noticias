
const logado = localStorage.getItem("logado");

if (logado !== "true") {
    window.location.href = "login.html";
}

const logout = document.getElementById("logout")

logout.addEventListener("click", () =>{
    localStorage.removeItem("logado");
    window.location.href = "/index.html";
});

let dados = null;

fetch('/mockup.json')
    .then(res => res.json())
    .then(json => {
        dados = json;
        renderNoticias();
    });

function renderNoticias() {
    const container = document.getElementById("lista-noticias")

    container.innerHTML = "";

    dados.noticia.forEach(noticia => {
        
        const imagem = dados.imagem.find(img => img.idNoticia === noticia.idNoticia);
        const card = document.createElement("article");
        card.classList.add("noticia-card");

        card.innerHTML = `
        <img src="${imagem ? imagem.url : ''}" alt="${noticia.titulo}"/>
        <div aria-label="corpo do conteúdo" class="content">
            <h3>${noticia.titulo}</h3>
            <p>${noticia.descricao}</p>

            <div class="actions">
                <button class="edit">Editar</button>
                <button class="delete" onclick="deletarNoticia(${noticia.idNoticia})">Excluir</button>
            </div>
        </div>
        `;

        container.appendChild(card)
    });
};

function deletarNoticia(id) {
    dados.noticia = dados.noticia.filter(n => n.idNoticia !== id);
    renderNoticias();
}