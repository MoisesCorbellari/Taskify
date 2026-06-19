# Taskify - Lista de Tarefas
Projeto voltado para aplicação prática de conhecimentos em desenvolvimento de APIs.  
Desenvolvido com **SQLAlchemy** para persistência de dados e **Alembic** para controle de migrações, o Taskify fornece uma API que permite ao usuário organizar suas atividades diárias por meio de operações *CRUD* (criar, ler, atualizar, excluir tarefas), além da funcionalidade de finalização de tarefas.

### Tecnologias Utilizadas
- **Python 3.14**: Linguagem de programação principal
- **FastAPI**: Framework para desenvolvimento de APIs
- **SQLAlchemy**: Biblioteca ORM (Object-Relational Mapping) para interação com banco de dados
- **Alembic**: Ferramenta para gerenciar migrações de banco de dados
- **Uvicorn**: Servidor ASGI (Asynchronous Server Gateway Interface) para executar aplicações FastAPI
- **DBeaver**: Gerenciador multiplataforma para bancos de dados

---

### Estrutura
A estrutura da aplicação é organizada da seguinte forma:
```
├── backend
│   ├── .github
│   │   └── workflows
│   │       └── deploy.yml
│   ├── alembic
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
│   ├── project_taskify
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   └── task_model.py
│   │   ├── routers
│   │   │   ├── service
│   │   │   │   ├── __init__.py
│   │   │   │   ├── create.py
│   │   │   │   ├── delete.py
│   │   │   │   ├── finish.py
│   │   │   │   ├── get_all.py
│   │   │   │   ├── get_id.py
│   │   │   │   └── update.py
│   │   │   ├── __init__.py
│   │   │   └── main_router.py
│   │   ├── schemas
│   │   │   ├── __init__.py
│   │   │   └── schema.py
│   │   └── __init__.py
│   ├── shared
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── exception.py
│   │   └── exceptions_handler.py
│   ├── alembic.ini
│   ├── Dockerfile
│   ├── main.py
│   ├── pyproject.toml
│   └── requirements.txt
├── frontend
│   ├── public
│   │   └── index.html
│   ├── src
│   │   ├── assets
│   │   │   └── img
│   │   │       └── logo.webp
│   │   └── services
│   │       ├── main.js
│   │       └── message.js
│   └── styles
│       └── main.css
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
