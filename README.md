# BotPokemon

Bot de WhatsApp assincrono (Python 3.12+, FastAPI) com arquitetura multi-agent.
Primeiro agent: `pokemon_rpg`. Novos agents podem ser adicionados em `bot/agents/`.

## Stack

- FastAPI (webhook que recebe eventos da API WhatsMiau)
- httpx.AsyncClient (chamadas a API WhatsMiau)
- SQLAlchemy async + asyncpg + Alembic (Postgres)
- Redis
- Pillow (geracao de cards de Pokemon)
- Docker / docker-compose

## Setup local com Docker

1. Copiar o arquivo de ambiente:

   ```bash
   cp .env.example .env
   ```

2. Subir bot + Postgres + Redis (com hot-reload):

   ```bash
   docker compose up --build
   ```

3. Verificar saude da aplicacao:

   ```bash
   curl http://localhost:8000/health
   ```

4. Rodar migrations (Alembic):

   ```bash
   docker compose exec bot alembic upgrade head
   ```

5. Criar nova migration apos alterar models:

   ```bash
   docker compose exec bot alembic revision --autogenerate -m "descricao"
   ```

## Producao

Usar o override de producao (sem hot-reload, sem expor portas de debug de banco/redis):

```bash
docker compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d
```

## Estrutura

```
bot/
├── core/              # config, db, client WhatsMiau, webhook FastAPI, dispatcher
├── agents/
│   ├── base.py        # interface Agent
│   └── pokemon_rpg/   # primeiro agent (comandos "!pk...")
└── alembic/           # migrations
```

Cada agent implementa `Agent.handle()` e se registra no `Dispatcher` (ver
`bot/core/webhook_server.py`, funcao `lifespan`) para tratar seu conjunto de comandos.

## Status

Estrutura inicial/esqueleto. Regras de jogo, parsing de comandos e integracao real
com WhatsMiau ainda **nao** implementadas — ver comentarios `TODO` no codigo.
