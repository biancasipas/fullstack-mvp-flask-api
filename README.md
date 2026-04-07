# 🏥 Sistema Clínico MVP

Este pequeno projeto faz parte do material didático da disciplina **Desenvolvimento Full Stack Básico**.

O objetivo é demonstrar o desenvolvimento de uma API simples utilizando Python, com foco na criação de um **MVP (Minimum Viable Product)** para gerenciamento de pacientes.

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

Será necessário ter o Python instalado na máquina.

Após clonar o repositório, siga os passos abaixo no terminal:

### 1. Acessar a pasta do projeto

```bash
cd meu_app_api
```

---

### 2. Criar ambiente virtual

```bash
python -m venv .venv
```

---

### 3. Ativar ambiente virtual (Windows)

```bash
.\.venv\Scripts\Activate.ps1
```

---

### 4. Instalar dependências

```bash
pip install flask==2.3.3 werkzeug==2.3.7 flask-openapi3 sqlalchemy flask-cors pydantic
```

> ⚠️ Observação: versões específicas foram utilizadas para evitar conflitos entre Flask e Werkzeug.

---

### 5. Executar a aplicação

```bash
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

---
