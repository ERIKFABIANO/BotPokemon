from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(slots=True)
class IncomingMessage:
    """Representacao normalizada de uma mensagem recebida via webhook do WhatsMiau.

    TODO: ajustar campos conforme payload real do WhatsMiau (ids de mensagem, tipo de
    midia, metadata de grupo, etc).
    """

    sender: str
    chat_id: str
    text: str
    raw_payload: dict


class Agent(ABC):
    """Interface base para todos os agents (pokemon_rpg, e futuros agents).

    Cada agent trata um conjunto de comandos (prefixo "!") e implementa `handle` para
    processar uma mensagem ja roteada pelo dispatcher.
    """

    name: str

    @abstractmethod
    async def handle(self, message: IncomingMessage) -> None:
        """Processa a mensagem recebida. TODO: implementar logica de cada agent concreto."""
        raise NotImplementedError
