# [Taskify - Lista de Tarefas](https://taskify-e767a91e.fastapicloud.dev/docs)
É um projeto voltado para aplicação prática de conceitos de desenvolvimento de APIs REST.

A aplicação utiliza o **ORM (Object-Relational Mapping) SQLAlchemy** para persistência e o gerenciamento dos dados e **Alembic** para controle das migrações do banco de dados. A API permite aos usuários organizarem suas atividades diárias por meio de operações *CRUD* (Create, Read, Update, Delete), além de disponibilizar um endpoint específico para marcar as tarefas como concluídas.

O backend da aplicação está hospedado no [FastAPI Cloud](https://fastapicloud.com/), permitindo testar a API diretamente pela documentação interativa. A documentação interativa pode ser acessada pelo link do título, permitindo visualizar e testar todos os endpoints diretamente pelo Swagger UI.

### Testando Localmente com Docker
#### Pré-requisitos
- Docker instalado

1. Acesse a página [Docker Hub](https://hub.docker.com/r/moisescorbellari/taskify)
2. Baixe a imagem: 
    ```bash 
    docker pull moisescorbellari/taskify
    ```
3. Execute o container: 
    ```bash
    docker run -d --name taskify -p 8000:8000 --add-host=host.docker.internal:host-gateway --env-file .env moisescorbellari/taskify:latest
    ```
4. Acesse a aplicação: 
    - API: [localhost:8000](http://localhost:8000/)
    - Swagger UI: [localhost:8000/docs](http://localhost:8000/docs)

### Tecnologias Utilizadas
- **Python 3.14**: Linguagem de programação principal
- **FastAPI**: Framework para desenvolvimento de APIs
- **SQLAlchemy**: Biblioteca ORM (Object-Relational Mapping) para interação com banco de dados
- **Alembic**: Ferramenta para migrações de banco de dados
- **Uvicorn**: Servidor ASGI (Asynchronous Server Gateway Interface) para executar aplicações FastAPI
- **DBeaver**: Gerenciador multiplataforma para bancos de dados

---

### Estrutura da API
```bash
├── .github
│   └── workflows
│       └── main.yml
├── backend
│   ├── .fastapicloud
│   │   ├── .gitignore
│   │   ├── README.md
│   │   ├── __init__.py
│   │   └── cloud.json
│   ├── .github
│   │   └── workflows
│   │       └── deploy.yml
│   ├── app
│   │   ├── api
│   │   │   ├── router
│   │   │   │   ├── __init__.py
│   │   │   │   ├── create.py
│   │   │   │   ├── delete.py
│   │   │   │   ├── finish.py
│   │   │   │   ├── get_all.py
│   │   │   │   ├── get_id.py
│   │   │   │   └── update.py
│   │   │   ├── __init__.py
│   │   │   └── api_router.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── task_model.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   └── schema.py
│   │   └── __init__.py
│   ├── migrations
│   │   ├── versions
│   │   │   ├── 2bb15b71ea96_rename_table_doup_to_tasks.py
│   │   │   ├── 3ba0259a5965_ajustando_nome_da_tabela_para_todo_list.py
│   │   │   ├── 73d7611a758e_mudando_nome_da_tabela.py
│   │   │   ├── 421e970e1b56_altera_campo_description.py
│   │   │   ├── b458adf3741f_rename_table_doup_to_doup_tasks.py
│   │   │   ├── e8f7add0cff4_rename_table.py
│   │   │   └── fd79eb160aa1_criando_tabela_tarefas.py
│   │   ├── README
│   │   ├── env.py
│   │   └── script.py.mako
│   ├── shared
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── exception.py
│   │   ├── exceptions_handler.py
│   │   └── types.py
│   ├── .dockerignore
│   ├── Dockerfile
│   ├── alembic.ini
│   ├── main.py
│   ├── pyproject.toml
│   └── uv.lock
├── frontend
│   ├── public
│   │   ├── services
│   │   │   └── message.js
│   │   └── src
│   │       ├── assets
│   │       │   └── img
│   │       │       └── logo.webp
│   │       └── styles
│   │           └── main.css
│   └── index.html
├── .gitignore
└── README.md
```
### Funcionalidades
-  A API permite que usuários possam:
    - Buscar todas as tarefas
    - Obter uma tarefa por ID
    - Criar uma nova tarefa
    - Atualizar uma tarefa por ID
    - Finalizar uma tarefa por ID
    - Excluir uma tarefa por ID
