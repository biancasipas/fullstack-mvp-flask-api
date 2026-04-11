# 🏥 Sistema Clínico MVP

Olá,eu fiz trbalho MVP sobre banco de dados SQLite, SQLALchemy, Flask OpeAPI3 (Swagger), Pyhton , HTML , CSS e Java Script para que fucnoinar rota API sistema clinico Nome do pacienite, idaide e peso, rota para ver as tebalas como banco de dados,http://127.0.0.1:5000/paciente  mostra lista do paciente. Como funcionar Front end e banck end. Por exempl o GET pegar lista paciente, POST como colocar mais novo pandiente e DELET remver panciente. 

---

## 🚀 Funcionalidades

O sistema integra Frontend e Backend, funcionando de forma completa.

- Cadastro de pacientes
- Listagem de pacientes
- Exclusão de pacientes
- Registro de consultas

---

## 🛠️ Tecnologias Utilizadas

* Python
* Flask
* Flask OpenAPI3 (Swagger)
* SQLAlchemy
* SQLite
* HTML, CSS e JavaScript

---

Front end : 

![alt text](img/image.png)

Eu fiz o codigo como HTML, CSS E JavaSCRIPT. Digitar nome paciente , clicar o botão casatar e mostra a tabela e tambem remover na tabela. 


Banckend:

![alt text](img/image-1.png)

AQUI CHATGTP ARRUMAR SOBRE : {
  "pacientes": [
    {
      "id": 3, 
      "idade": 23, 
      "nome": "Julia", 
      "peso": 71.0
    }, 
    {
      "id": 4, 
      "idade": 24, 
      "nome": "Bianca", 
      "peso": 60.0
    }, 
    {
      "id": 6, 
      "idade": 23, 
      "nome": "Clara", 
      "peso": 65.0
    }
  ], 
  "sucesso": true, 
  "total": 3
}

SWAGGER: 

![alt text](img/image-2.png)

SOBRE POST GET DELET (ARRUMAR O TEXTO)





## 🧱 Estrutura do Projeto

```
Meu_app_api/
  model/
    base.py
    paciente.py
    consulta.py
  schemas/
    __init__.py
    paciente.py
    error.py
  database/
  log/
  app.py
  logger.py

meu_app_front/
  index.html
  scripts.js
  styles.css
```

---

## 💻 Como Executar o Projeto

### 🔧 Backend

#### 1. Acessar a pasta

```bash
cd Meu_app_api
```

#### 2. Criar ambiente virtual

```bash
python -m venv venv
```

#### 3. Ativar (Windows)

```bash
venv\Scripts\activate
```

---

## ⚠️ Problema de Dependências

### ❌ Erro comum

```bash
ModuleNotFoundError: No module named 'werkzeug.datastructures.structures'
```

ou

```bash
TypeError: LocalProxy.__init__() got an unexpected keyword argument
```

---

## 📌 Causa

Esse erro ocorre devido a **conflito de versões** entre:

* Flask
* Werkzeug
* flask-openapi3

---

## ✅ Solução

#### 1. Remover dependências incompatíveis

```bash
pip uninstall flask werkzeug flask-openapi3 -y
```

#### 2. Instalar versões compatíveis

```bash
pip install flask==2.0.3 werkzeug==2.0.3 flask-openapi3==2.3.2
```

#### 3. Instalar demais dependências

```bash
pip install flask-cors sqlalchemy pydantic
```

---

#### 4. Executar a aplicação

```bash
python app.py
```

---

## 🌐 Acessando a API

* Swagger (documentação interativa):
  http://127.0.0.1:5000/openapi

* Endpoint de pacientes:
  http://127.0.0.1:5000/paciente

---

## 💻 Executar o Frontend

#### 1. Acessar pasta

```bash
cd meu_app_front
```

#### 2. Rodar servidor local

```bash
python -m http.server 5500
```

#### 3. Abrir no navegador

http://localhost:5500

---

## 📡 Endpoints

### Paciente

* `POST /paciente` → Criar paciente
* `GET /paciente` → Listar pacientes
* `DELETE /paciente/{paciente_id}` → Deletar paciente

### Consulta

* `POST /consulta` → Criar consulta

---

## 🗄️ Banco de Dados

* Utiliza SQLite
* Criado automaticamente em:

```
database/db.sqlite3
```

---

## ⚠️ Observações

* Criar a pasta `database/` caso não exista
* O sistema roda localmente (ambiente de desenvolvimento)
* Logs são armazenados na pasta `log/`

---

## 🎯 Objetivo do MVP

O projeto tem como objetivo validar uma solução simples para gerenciamento clínico, focando em:

* Entrega rápida de valor
* Funcionalidades essenciais
* Estrutura pronta para evolução

---

## 🧠 Conclusão

O sistema atende aos requisitos de um MVP ao ser:

* Simples
* Funcional
* Extensível

Além disso, foram tratados problemas reais de ambiente (dependências), demonstrando conhecimento prático no desenvolvimento fullstack.

---
