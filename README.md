 # 🏥 Sistema Clínico MVP

Este pequeno projeto faz parte do material didático da disciplina **Desenvolvimento Full Stack Básico**.

O objetivo é ilustrar, na prática, o desenvolvimento de uma API simples utilizando Python, aplicando os conceitos de backend, banco de dados e integração com frontend.

O sistema consiste em um **MVP (Minimum Viable Product)** para gerenciamento de pacientes, contendo apenas funcionalidades essenciais para validação da proposta.

---

## 🚀 Funcionalidades

* Cadastro de pacientes
* Listagem de pacientes
* Exclusão de pacientes
* Registro de consultas

---

## 🛠️ Tecnologias utilizadas

* Python
* Flask
* Flask OpenAPI3 (Swagger)
* SQLAlchemy
* SQLite
* JavaScript

---

## 💻 Como executar

Será necessário ter todas as bibliotecas Python listadas no arquivo `requirements.txt` instaladas.

Após clonar o repositório, acesse a pasta do projeto pelo terminal:

```
cd meu_app_api
```

> É fortemente recomendado o uso de ambiente virtual (virtualenv).

### 1. Criar ambiente virtual

```
python -m venv .venv
```

### 2. Ativar ambiente virtual (Windows)

```
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar dependências

```
pip install -r requirements.txt
```

---

## ▶️ Executando a API

Para executar a aplicação:

```
python app.py
```

---

## 🌐 Acessando a API

Abra o navegador e acesse:

```
http://127.0.0.1:5000/openapi
```

Neste endereço é possível visualizar e testar os endpoints da API utilizando o Swagger.

---

## 📡 Endpoints

### Paciente

* `POST /paciente` → Criar paciente
* `GET /paciente` → Listar pacientes
* `DELETE /paciente/{paciente_id}` → Deletar paciente

### Consulta

* `POST /consulta` → Criar consulta




