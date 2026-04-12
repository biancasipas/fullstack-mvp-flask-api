# Sistema Clínico MVP 🏥

Esta é uma API Flask com documentação Swagger usando Flask-OpenAPI3.

## 🚀 1. Pré-requisitos
Antes de começar, você precisa ter:
- Python 3.10+
- pip instalado
- (Recomendado) ambiente virtual venv

## 2. Instalação e Configuração
```bash
git clone <URL_DO_REPOSITORIO>
cd fullstack-mvp-flask-api/Meu_app_api

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt
```

## 3. Como Rodar a API

Para iniciar o servidor, execute o comando abaixo dentro da pasta raiz do projeto:

```bash
python app.py
```
## 3. Acessar no Navegador

Com o servidor iniciado, acesse:

| Recurso | URL | Descrição |
| :--- | :--- | :--- |
| **Documentação Swagger** | [http://127.0.0.1:5000/openapi/](http://127.0.0.1:5000/openapi/) | Interface interativa para testar os endpoints. |
| **Página Inicial** | [http://127.0.0.1:5000/](http://127.0.0.1:5000/) | Redirecionamento padrão da API. |

---

## 4. Rotas Principais

Abaixo estão listados os principais endpoints disponíveis na API. Para detalhes sobre os parâmetros de entrada (JSON), consulte o Swagger no tópico anterior.

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/paciente` | Lista todos os pacientes cadastrados na base. |
| `POST` | `/paciente` | Cadastra um novo paciente no sistema. |
| `DELETE` | `/paciente/<id>` | Remove um paciente específico através do ID. |
| `POST` | `/consulta` | Realiza o agendamento de uma nova consulta. |

---


## 5. Guia de Solução de Problemas

Se você encontrar algum erro durante a execução, verifique as situações comuns abaixo:

### Erro de comando (Terminal)
* **Problema:** Erros de sintaxe ao copiar comandos.
* **Solução:** No Windows ou Linux, não inclua o símbolo `$` ao digitar os comandos. O `$` é apenas um indicador de que o comando deve ser digitado no terminal. Use diretamente `pip` ou `python`.

### Arquivo não encontrado (File Not Found)
* **Problema:** O terminal diz que não encontrou o arquivo `app.py` ou `requirements.txt`.
* **Solução:** Verifique se você está dentro da pasta correta do projeto. Utilize o comando `cd` para navegar:

  ```bash
  cd Meu_app_api

## 🏁 Finalização

Tudo pronto! Com o servidor rodando, sua API está pronta para receber requisições.

### 🚀 Atalho Rápido
Tudo pronto! Após executar python app.py, acesse:

* **Swagger:** [http://127.0.0.1:5000/openapi/](http://127.0.0.1:5000/openapi/)

---



