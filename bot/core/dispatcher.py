from __future__ import annotations

import logging

from bot.agents.base import Agent, IncomingMessage

logger = logging.getLogger(__name__)


class Dispatcher:
    """Roteia mensagens recebidas para o agent responsavel pelo comando.

    Cada agent se registra com um prefixo (ex.: "!pk" para pokemon_rpg). O dispatcher
    identifica o comando na mensagem e encaminha para o agent correto.

    TODO: definir regra real de matching (prefixo unico por agent, comandos globais tipo
    !help, fallback quando nenhum agent reconhece o comando, etc).
    """

    def __init__(self) -> None:
        self._agents: dict[str, Agent] = {}

    def register(self, prefix: str, agent: Agent) -> None:
        self._agents[prefix] = agent

    async def dispatch(self, message: IncomingMessage) -> None:
        """Identifica o agent responsavel e delega o tratamento da mensagem.

        TODO: implementar parsing real do comando (extrair prefixo/comando do texto)
        e roteamento para o agent correspondente.
        """
        logger.debug("Dispatch stub: mensagem recebida de %s: %r", message.sender, message.text)
        raise NotImplementedError("TODO: implementar logica de roteamento comando -> agent")
