const botao = document.querySelector("#botao");
function botaoFoiClicado(){
    alert("Você clicou no botão");
}

botao.addEventListener("click", botaoFoiClicado);
botao.innerHTML = "Não clique aqui. Você foi avisado."
