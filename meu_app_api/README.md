## 💻 Como executar o projeto (via terminal)

Siga os passos abaixo para executar a aplicação corretamente:

### 🟢 1. Abrir o terminal

No Windows, pressione `Win + R`, digite:

```
powershell
```

e pressione Enter.

---

### 🟢 2. Acessar a pasta do projeto

```
cd Documents\fullstack-mvp-flask-api
cd meu_app_api
```

---

### 🟢 3. Verificar os arquivos

```
dir
```

Deve aparecer o arquivo `app.py` na listagem.

---

### 🟢 4. Criar ambiente virtual

```
python -m venv .venv
```

---

### 🟢 5. Ativar ambiente virtual (Windows)

```
.\.venv\Scripts\Activate.ps1
```

Após ativar, o terminal exibirá:

```
(.venv)
```

---

### 🟢 6. Instalar dependências

```
pip install flask==2.3.3 werkzeug==2.3.7 flask-openapi3 sqlalchemy flask-cors pydantic
```

---

### 🟢 7. Executar a aplicação

```
python app.py
```

---

### 🌐 8. Acessar no navegador

Abra o navegador e acesse:

```
http://127.0.0.1:5000/openapi
```

Neste endereço será possível visualizar e testar a API utilizando o Swagger.

