# Back end

O Back End do sistema é a parte responsável por toda a lógica da aplicação e pelo gerenciamento dos dados. Ele foi desenvolvido utilizando o Flask, um framework em Python, junto com Flask-OpenAPI3, que permite criar uma API documentada automaticamente com Swagger.

## Como executar

### 1. Clonar o repositório

```bash

cd Documents\fullstack-mvp-flask-api
cd meu_app_api

```

### 2. Criar ambiente virtual

```bash

python -m venv venv

```
### Windows

```bash

venv\Scripts\activate

```
### 3. Instalar dependência

```bash

pip install -r requirements.txt

```
### 4. Executar a aplicação

```bash

python app.py

```

## Acessar no Navegador

Com o servidor devidamente iniciado, você pode interagir com a API e o sistema através dos endereços abaixo:

| Recurso | URL | Descrição |
| :--- | :--- | :--- |
| **Swagger (OpenAPI)** | [http://127.0.0.1:5000/openapi/](http://127.0.0.1:5000/openapi/) | Interface interativa para testar todos os endpoints da API. |
| **Página Base** | [http://127.0.0.1:5000/](http://127.0.0.1:5000/) | Endpoint raiz da aplicação. |
| **Frontend (HTML)** | [http://127.0.0.1:5000/app](http://127.0.0.1:5000/app) | Interface visual simples para interação com o sistema. |

---

## Rotas Principais

Abaixo estão listados os principais endpoints disponíveis na API. Para detalhes sobre os parâmetros de entrada (JSON), consulte o Swagger no tópico anterior.

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/paciente` | Lista todos os pacientes cadastrados na base. |
| `POST` | `/paciente` | Cadastra um novo paciente no sistema. |
| `DELETE` | `/paciente/<id>` | Remove um paciente específico através do ID. |
| `POST` | `/consulta` | Realiza o agendamento de uma nova consulta. |

---


## Guia de Solução de Problemas

Se você encontrar algum erro durante a execução, verifique as situações comuns abaixo:

### Erro de comando (Terminal)
* **Problema:** Erros de sintaxe ao copiar comandos.
* **Solução:** No Windows ou Linux, não inclua o símbolo `$` ao digitar os comandos. O `$` é apenas um indicador de que o comando deve ser digitado no terminal. Use diretamente `pip` ou `python`.

### Arquivo não encontrado (File Not Found)
* **Problema:** O terminal diz que não encontrou o arquivo `app.py` ou `requirements.txt`.
* **Solução:** Verifique se você está dentro da pasta correta do projeto. Utilize o comando `cd` para navegar:

  ```bash
  cd meu_app_api
  ```





