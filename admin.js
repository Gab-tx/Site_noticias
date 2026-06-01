const logado = localStorage.getItem("logado");

if (logado !== "true") {
    window.location.href = "login.html";
}

const logout = document.getElementById("logout")

logout.addEventListener("click", () =>{
    localStorage.removeItem("logado");
    window.location.href = "index.html";
});