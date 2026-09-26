from __future__ import annotations

import random

from sqlalchemy import select

from bot.agents.pokemon_rpg.models import Pokemon, Trainer
from bot.core.db import get_session

POKEMON_INICIAL = "Eevee"
POKEBOLAS_INICIAIS = 5
MOEDAS_INICIAIS = 100

POKEMONS_SELVAGENS = ["Pikachu", "Bulbasaur", "Charmander", "Squirtle", "Caterpie", "Pidgey"]
CHANCE_CAPTURA = 0.60


class PokemonRpgService:
    """Regras de negocio do RPG de Pokemon (captura, perfil, cadastro de treinador)."""

    async def iniciar(self, whatsapp_id: str) -> str:
        async with get_session() as session:
            existente = await session.scalar(select(Trainer).where(Trainer.whatsapp_id == whatsapp_id))
            if existente:
                return "Você já iniciou!"

            trainer = Trainer(
                whatsapp_id=whatsapp_id,
                pokebolas=POKEBOLAS_INICIAIS,
                moedas=MOEDAS_INICIAIS,
            )
            session.add(trainer)
            await session.flush()

            session.add(Pokemon(trainer_id=trainer.id, nome=POKEMON_INICIAL))
            await session.commit()

            return (
                f"Bem-vindo! Você ganhou 1x {POKEMON_INICIAL} e {POKEBOLAS_INICIAIS}x Pokébolas.\n"
                "Use *!perfil* e *!capturar*"
            )

    async def perfil(self, whatsapp_id: str) -> str:
        async with get_session() as session:
            trainer = await session.scalar(select(Trainer).where(Trainer.whatsapp_id == whatsapp_id))
            if not trainer:
                return "Digite *!iniciar* primeiro."

            pokemons = (
                await session.scalars(select(Pokemon).where(Pokemon.trainer_id == trainer.id))
            ).all()
            nomes = ", ".join(p.nome for p in pokemons) or "-"

            return (
                "*PERFIL*\n"
                f"Pokébolas: {trainer.pokebolas}\n"
                f"Moedas: {trainer.moedas}\n"
                f"Pokémon: {nomes}"
            )

    async def capturar(self, whatsapp_id: str) -> str:
        async with get_session() as session:
            trainer = await session.scalar(select(Trainer).where(Trainer.whatsapp_id == whatsapp_id))
            if not trainer:
                return "Digite *!iniciar* primeiro."
            if trainer.pokebolas <= 0:
                return "Sem Pokébolas!"

            trainer.pokebolas -= 1

            if random.random() < CHANCE_CAPTURA:
                sorteado = random.choice(POKEMONS_SELVAGENS)
                session.add(Pokemon(trainer_id=trainer.id, nome=sorteado))
                await session.commit()
                return f"Capturou um *{sorteado}*!\nPokébolas: {trainer.pokebolas}"

            await session.commit()
            return f"O Pokémon fugiu!\nPokébolas: {trainer.pokebolas}"
