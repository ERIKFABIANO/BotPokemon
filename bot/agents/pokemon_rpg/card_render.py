from __future__ import annotations

import io

from PIL import Image


def render_pokemon_card(pokemon_data: dict) -> bytes:
    """Gera imagem (PNG) do card de Pokemon a partir dos dados fornecidos.

    TODO: implementar renderizacao real (template, sprite, stats, fonte, cores por tipo, etc)
    usando Pillow (ImageDraw, fontes, composicao de camadas).
    """
    raise NotImplementedError("TODO: implementar geracao de card com Pillow")


def _placeholder_blank_image(width: int = 512, height: int = 512) -> bytes:
    """Util interno apenas para validar o pipeline de imagem (nao usar em producao)."""
    image = Image.new("RGB", (width, height), color="white")
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return buffer.getvalue()
