const API_URL = "http://127.0.0.1:5000";

/*
GET
*/
const getList = () => {
    fetch(`${API_URL}/paciente`)
        .then(res => res.json())
        .then(data => {
            console.log("RETORNO BACKEND:", data);

            const tabela = document.getElementById("listaPacientes");
            tabela.innerHTML = "";

            data.pacientes.forEach(p => insertList(p));
        })
        .catch(err => console.error(err));
};

/*
POST
*/
const postItem = (nome, idade, peso) => {
    const data = { nome, idade: Number(idade), peso: Number(peso) };

    fetch(`${API_URL}/paciente`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(() => getList())
    .catch(err => console.error(err));
};

/*
DELETE
*/
const deleteItem = (id) => {
    fetch(`${API_URL}/paciente/${id}`, {
        method: "DELETE"
    })
    .then(() => getList())
    .catch(err => console.error(err));
};

/*
INSERT TABLE
*/
const insertList = (p) => {
    const tabela = document.getElementById("listaPacientes");

    const row = tabela.insertRow();

    row.insertCell(0).innerHTML = p.nome;
    row.insertCell(1).innerHTML = p.idade;
    row.insertCell(2).innerHTML = p.peso;

    row.insertCell(3).innerHTML =
        `<button class="close" onclick="deleteItem(${p.id})">X</button>`;
};

/*
CREATE
*/
const criarPaciente = () => {
    const nome = document.getElementById("nome").value;
    const idade = document.getElementById("idade").value;
    const peso = document.getElementById("peso").value;

    if (!nome || !idade || !peso) {
        alert("Preencha todos os campos!");
        return;
    }

    postItem(nome, idade, peso);

    document.getElementById("nome").value = "";
    document.getElementById("idade").value = "";
    document.getElementById("peso").value = "";
};

/*
INIT
*/
getList();

window.onload = () => {
    getList();
};