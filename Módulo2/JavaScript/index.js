const elementoPorId = document.getElementById("elemento1");
elementoPorId.innerHTML = 'Eu represento o elemento com ID "elemento1"';

const elementoPorClasse = document.getElementsByClassName("classe-exemplo");
for (const elemento of elementoPorClasse){
    elemento.innerHTML = 'Eu represento o elemento com a classe "classe-exemplo"';
} 