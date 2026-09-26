from __future__ import annotations

from types import TracebackType

import httpx

from bot.core.config import get_settings


class WhatsMiauClient:
    """Client async para a API WhatsMiau (REST em Go, compativel com rotas Evolution API).

    TODO: implementar chamadas reais aos endpoints do WhatsMiau (payloads, headers de
    autenticacao, tratamento de erros especificos da API, retries, etc).
    """

    def __init__(self, base_url: str | None = None, api_key: str | None = None, instance: str | None = None) -> None:
        settings = get_settings()
        self._base_url = base_url or settings.whatsmiau_base_url
        self._api_key = api_key or settings.whatsmiau_api_key
        self._instance = instance or settings.whatsmiau_instance
        self._client: httpx.AsyncClient | None = None

    async def __aenter__(self) -> "WhatsMiauClient":
        self._client = httpx.AsyncClient(
            base_url=self._base_url,
            headers={"apikey": self._api_key},
            timeout=10.0,
        )
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if self._client is not None:
            await self._client.aclose()
            self._client = None

    async def send_text(self, to: str, message: str) -> dict:
        """Envia mensagem de texto para o numero `to`.

        TODO: implementar chamada real (rota tipo /message/sendText/{instance}).
        """
        raise NotImplementedError("TODO: implementar envio de texto via WhatsMiau API")

    async def send_image(self, to: str, image_bytes: bytes, caption: str | None = None) -> dict:
        """Envia imagem (ex.: card de Pokemon) para o numero `to`.

        TODO: implementar chamada real (rota tipo /message/sendMedia/{instance}).
        """
        raise NotImplementedError("TODO: implementar envio de imagem via WhatsMiau API")
