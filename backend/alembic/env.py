import asyncio
import os
from logging.config import fileConfig

from alembic import context
from dotenv import load_dotenv
from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_engine_from_config
from project_taskify.models.task_model import Task  # noqa: F401 - required for Alembic autogenerate
from shared.database import Base

load_dotenv()

database_url = os.getenv("TOKEN")
if not database_url:
    raise ValueError("A variável de ambiente TOKEN não foi definida!")

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

config.set_main_option("sqlalchemy.url", database_url)

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support


target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    # Cria o engine ASYNC usando as configs do alembic.ini
    # (incluindo sua TOKEN com asyncpg)
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,  # evita pool de conexões (bom pra migrations)
    )

    # Função async que realmente vai abrir a conexão
    async def run():
        # Aqui é o ponto crítico: precisa ser async with (não pode ser with normal)
        async with connectable.connect() as connection:
            # Alembic é síncrono internamente,
            # então usamos run_sync pra "traduzir" async -> sync
            await connection.run_sync(do_run_migrations)

    # Executa a função async
    asyncio.run(run())


def do_run_migrations(connection):
    # Configura o contexto do Alembic com a conexão ativa
    context.configure(
        connection=connection,
        target_metadata=target_metadata,  # seus models (Base.metadata)
    )
    # Inicia a transação das migrations
    with context.begin_transaction():
        # Aqui ele executa os scripts (upgrade/downgrade)
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
