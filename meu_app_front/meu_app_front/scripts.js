const API_URL = "http://127.0.0.1:5000";

/*
GET - LISTAR PACIENTES
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
        .catch(err => console.error("ERRO GET:", err));
};


/*
POST - CRIAR PACIENTE
*/
const postItem = (nome, idade, peso) => {

    const data = {
        nome: nome.trim(),
        idade: parseInt(idade),
        peso: parseFloat(peso)
    };

    console.log("ENVIANDO:", data);

    if (!data.nome || isNaN(data.idade) || isNaN(data.peso)) {
        alert("Preencha corretamente todos os campos!");
        return;
    }

    fetch(`${API_URL}/paciente_json`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(async (res) => {

        const text = await res.text();
        console.log("STATUS:", res.status);
        console.log("RESPOSTA:", text);

        if (!res.ok) {
            alert("Erro ao criar paciente");
            return;
        }

        getList();
    })
    .catch(err => console.error("ERRO POST:", err));
};


/*
DELETE - REMOVER PACIENTE
*/
const deleteItem = (id) => {

    fetch(`${API_URL}/paciente/${id}`, {
        method: "DELETE"
    })
    .then(async (res) => {

        const text = await res.text();
        let data;

        try {
            data = JSON.parse(text);
        } catch {
            console.error("Resposta inválida:", text);
            alert("Erro inesperado no servidor");
            return;
        }

        if (!res.ok) {
            alert(data.erro || "Erro ao deletar paciente");
            return;
        }

        getList();
    })
    .catch(err => console.error("ERRO DELETE:", err));
};


/*
INSERIR NA TABELA
*/
const insertList = (p) => {

    const tabela = document.getElementById("listaPacientes");

    const row = tabela.insertRow();

    row.insertCell(0).innerHTML = p.nome;
    row.insertCell(1).innerHTML = p.idade;
    row.insertCell(2).innerHTML = p.peso;

    row.insertCell(3).innerHTML =
        `<button onclick="deleteItem(${p.id})">X</button>`;
};


/*
CRIAR PACIENTE (FORM)
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
window.onload = () => {
    getList();
};