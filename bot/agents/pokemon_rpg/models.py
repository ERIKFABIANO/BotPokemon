from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from bot.core.db import Base


class Trainer(Base):
    """Treinador (usuario do WhatsApp) no RPG."""

    __tablename__ = "pokemon_rpg_trainers"

    id: Mapped[int] = mapped_column(primary_key=True)
    whatsapp_id: Mapped[str] = mapped_column(unique=True, index=True)
    pokebolas: Mapped[int] = mapped_column(default=5)
    moedas: Mapped[int] = mapped_column(default=100)


class Pokemon(Base):
    """Pokemon capturado por um treinador."""

    __tablename__ = "pokemon_rpg_pokemons"

    id: Mapped[int] = mapped_column(primary_key=True)
    trainer_id: Mapped[int] = mapped_column(ForeignKey("pokemon_rpg_trainers.id"), index=True)
    nome: Mapped[str]
