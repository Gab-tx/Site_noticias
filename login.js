const form = document.getElementById("login-form");

form.addEventListener("submit", (event) => {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;
    const mensagem = document.getElementById("mensagem");

    const admsenha = "admin"
    const admemail = "admin@gmail.com"

    if (email === admemail && senha === admsenha) {
        localStorage.setItem("logado", "true")
        window.location.href = "admin.html";
    } else {
        mensagem.textContent = "Email ou senha inválidos.";
    }

});