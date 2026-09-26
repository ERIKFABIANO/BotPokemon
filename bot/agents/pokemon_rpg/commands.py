from __future__ import annotations

from collections.abc import Awaitable, Callable

from bot.agents.base import IncomingMessage
from bot.agents.pokemon_rpg.service import PokemonRpgService

# Handler recebe a mensagem e retorna o texto de resposta (envio real fica a cargo
# de quem chama o handler, ex.: o Agent/dispatcher, via WhatsMiauClient).
CommandHandler = Callable[[IncomingMessage], Awaitable[str]]

COMMANDS: dict[str, CommandHandler] = {}

_service = PokemonRpgService()


def register(command: str) -> Callable[[CommandHandler], CommandHandler]:
    def decorator(func: CommandHandler) -> CommandHandler:
        COMMANDS[command] = func
        return func

    return decorator


@register("!iniciar")
async def handle_iniciar(message: IncomingMessage) -> str:
    return await _service.iniciar(message.sender)


@register("!perfil")
async def handle_perfil(message: IncomingMessage) -> str:
    return await _service.perfil(message.sender)


@register("!capturar")
async def handle_capturar(message: IncomingMessage) -> str:
    return await _service.capturar(message.sender)
