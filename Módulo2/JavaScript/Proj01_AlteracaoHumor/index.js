const pessoa = {
    nome: "Este é Chico...", 
    serio: true,
    imagemSerio: "img/Chico_Bolado.png",
    imagemDeboa: "img/Chico_Deboa.png",
}

const botao = {
    botao1: "... SEM uma carreira BLUEMER",
    botao2: "... COM uma carreira BLUEMER",
} 

const alt_nome = document.getElementById("nome");
const alt_situacao = document.getElementById("situacao");
const alt_botao = document.getElementById("alteraHumor");

alt_nome.innerHTML = pessoa.nome;
alt_botao.innerHTML = botao.botao1;

function alteraHumor() {
    const alt_img = document.getElementById("imagem");
    const alt_humor = document.getElementById("bloco_humor");
    const alt_botao = document.getElementById("alteraHumor");
    const alt_situacao = document.getElementById("situacao");

    if (pessoa.serio) {
        alt_img.src = pessoa.imagemSerio;
        alt_humor.innerHTML = "Emprego ameaçado. Não consegue bons salários. Não tem plano de carreira. Não consegue se atualizar no mercado. Nunca será feliz de verdade.";
        alt_botao.innerHTML = botao.botao1;
        alt_situacao.innerHTML = "Assim como tantos milhares, um profissional em desvalorização.";
    }

    else {
        alt_img.src = pessoa.imagemDeboa;
        alt_humor.innerHTML = "Ama o que faz. Seu retorno é ótimo. Tem uma carreria com infinitas possibilidades. Alinhado com o mercado corporativo. Felicidade chegou aqui e parou.";
        alt_botao.innerHTML = botao.botao2;
        alt_situacao.innerHTML = "Um DEV de respeito sendo disputado no mercado.";
    }
}

alteraHumor()

const butAltHumor = document.getElementById("alteraHumor");
butAltHumor.addEventListener("click", function (){
    pessoa.serio = !pessoa.serio;
    alteraHumor();
})

window.alert("Para interagir, apenas aperte o BOTÃO AZUL.")