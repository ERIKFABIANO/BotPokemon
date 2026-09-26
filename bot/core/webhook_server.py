from __future__ import annotations

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from bot.core.config import get_settings
from bot.core.db import dispose_engine
from bot.core.dispatcher import Dispatcher

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    settings = get_settings()
    app.state.dispatcher = Dispatcher()
    # TODO: registrar agents no dispatcher (ex.: dispatcher.register("!pk", PokemonRpgAgent()))
    logger.info("Aplicacao iniciada (env=%s)", settings.app_env)
    yield
    await dispose_engine()
    logger.info("Aplicacao encerrada")


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title="BotPokemon", lifespan=lifespan)

    @app.get("/health")
    async def health() -> dict:
        return {"status": "ok"}

    @app.post(settings.webhook_path)
    async def webhook(request: Request) -> dict:
        """Recebe eventos de mensagens do WhatsMiau.

        TODO: validar assinatura/secret do webhook, parsear payload real do WhatsMiau
        para `IncomingMessage` e encaminhar para `app.state.dispatcher.dispatch(...)`.
        """
        payload = await request.json()
        logger.debug("Webhook recebido: %r", payload)
        # TODO: raise NotImplementedError substituido por ack simples ate implementar parsing
        return {"status": "received"}

    return app
