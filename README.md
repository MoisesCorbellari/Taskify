# Taskify - Lista de Tarefas (Em desenvolvimento)
Projeto voltado para aplicação prática de conhecimentos em desenvolvimento de APIs.  
Desenvolvido com **SQLAlchemy** para persistência de dados e **Alembic** para controle de migrações, o Taskify fornece uma API que permite ao usuário organizar suas atividades diárias por meio de operações *CRUD* (criar, ler, atualizar, excluir tarefas), além da funcionalidade de finalização de tarefas.

### Tecnologias Utilizadas
- **Python 3.14.2**: Linguagem de programação principal
- **FastAPI**: Framework para desenvolvimento de APIs
- **SQLAlchemy**: Biblioteca ORM (Object-Relational Mapping) para interação com banco de dados
- **Alembic**: Ferramenta para gerenciar migrações de banco de dados
- **Uvicorn**: Servidor ASGI (Asynchronous Server Gateway Interface) para executar aplicações FastAPI
- **DBeaver**: Gerenciador multiplataforma para bancos de dados

---

### Estrutura do Projeto
A estrutura do projeto é organizada da seguinte forma:
```plaintext
backend_taskify/
  alembic/
    versions/              
    env.py                   
    README                   
    script.py.mako           

  project_taskify/
    models/                  
      task_model.py
    routers/
      task_router.py
    schemas/
      schema.py
    
    shared/
      database.py
      dependencies.py
      exception.py
      exceptions_handler.py

  alembic.ini
  main.py
  requirements.txt -> arquivo com as dependências do projeto

frontend_taskify/
  public/
    index.html
  src/
    assets/
      img/
        logom.webp
    services/
      main.js
      message.js
  style/
    main.css
.gitignore

README.md
```
### Funcionalidades
-  A API permite que usuários possam:
    - Buscar todas as tarefas
    - Obter uma tarefa por ID
    - Criar uma nova tarefa
    - Atualizar uma tarefa por ID
    - Finalizar uma tarefa por ID
    - Excluir uma tarefa por ID
