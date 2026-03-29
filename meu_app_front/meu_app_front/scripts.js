/*
  --------------------------------------------------------------------------------------
  Função para obter a lista existente do servidor via requisição GET
  --------------------------------------------------------------------------------------
*/
const getList = async () => {
  let url = 'http://127.0.0.1:5000/pacientes';

  fetch(url, {
    method: 'get',
  })
    .then((response) => response.json())
    .then((data) => {
      data.pacientes.forEach(item => 
        insertList(item.nome, item.cpf, item.data_registro)
      );
    })
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Carregamento inicial dos dados
  --------------------------------------------------------------------------------------
*/
getList();

/*
  --------------------------------------------------------------------------------------
  POST: adicionar paciente no servidor
  --------------------------------------------------------------------------------------
*/
const postItem = async (inputNome, inputCpf, inputData) => {
  const formData = new FormData();

  formData.append('nome', inputNome);
  formData.append('cpf', inputCpf);
  formData.append('data_registro', inputData);

  let url = 'http://127.0.0.1:5000/paciente';

  fetch(url, {
    method: 'post',
    body: formData
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Botão de remover (X)
  --------------------------------------------------------------------------------------
*/
const insertButton = (parent) => {
  let span = document.createElement("span");
  let txt = document.createTextNode("\u00D7");

  span.className = "close";
  span.appendChild(txt);
  parent.appendChild(span);
}

/*
  --------------------------------------------------------------------------------------
  DELETE paciente
  --------------------------------------------------------------------------------------
*/
const deleteItem = (nome) => {
  console.log(nome);

  let url = 'http://127.0.0.1:5000/paciente?nome=' + nome;

  fetch(url, {
    method: 'delete'
  })
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error:', error);
    });
}

/*
  --------------------------------------------------------------------------------------
  Remover item da tabela
  --------------------------------------------------------------------------------------
*/
const removeElement = () => {
  let close = document.getElementsByClassName("close");

  for (let i = 0; i < close.length; i++) {
    close[i].onclick = function () {

      let row = this.parentElement.parentElement;
      const nomePaciente = row.getElementsByTagName('td')[0].innerHTML;

      if (confirm("Tem certeza que deseja remover este paciente?")) {
        row.remove();
        deleteItem(nomePaciente);
        alert("Paciente removido!");
      }
    }
  }
}

/*
  --------------------------------------------------------------------------------------
  Adicionar novo paciente
  --------------------------------------------------------------------------------------
*/
const newItem = () => {
  let inputNome = document.getElementById("newInput").value;
  let inputCpf = document.getElementById("newQuantity").value;
  let inputData = document.getElementById("newPrice").value;

  if (inputNome === '') {
    alert("Digite o nome do paciente!");
  }
  else if (inputCpf === '') {
    alert("Digite o CPF do paciente!");
  }
  else if (inputData === '') {
    alert("Selecione a data de registro!");
  }
  else {
    insertList(inputNome, inputCpf, inputData);
    postItem(inputNome, inputCpf, inputData);
    alert("Paciente adicionado!");
  }
}

/*
  --------------------------------------------------------------------------------------
  Inserir paciente na tabela
  --------------------------------------------------------------------------------------
*/
const insertList = (nome, cpf, data) => {
  var item = [nome, cpf, data];

  var table = document.getElementById('myTable');
  var row = table.insertRow();

  for (var i = 0; i < item.length; i++) {
    var cel = row.insertCell(i);
    cel.textContent = item[i];
  }

  insertButton(row.insertCell(-1));

  // limpar campos
  document.getElementById("newInput").value = "";
  document.getElementById("newQuantity").value = "";
  document.getElementById("newPrice").value = "";

  removeElement();
}