import discord
from math import ceil
from typing import List
from dominio.bosque import Bosque
from dominio.animal import Animal


MAX_BOSQUES_POR_PAGINA = 10


class ViewBosque(discord.ui.View):

    def __init__(self, bosques: List[Bosque], animales: List[Animal], timeout: int = 120):
        super().__init__(timeout=timeout)
        self.bosques = bosques
        self.animales = animales
        self.pagina_actual = 0
        self.total_paginas = ceil(len(bosques) / MAX_BOSQUES_POR_PAGINA) #ceil redondea para arriba, de forma que nunca nos falte espacio en el embed.

    def crear_embed(self) -> discord.Embed:
        inicio = self.pagina_actual * MAX_BOSQUES_POR_PAGINA
        fin = inicio + MAX_BOSQUES_POR_PAGINA
        chunk = self.bosques[inicio:fin]

        embed = discord.Embed(
            title="BOSQUES",
            description="Cada bosque tiene un tipo de árbol o planta en abundancia, y un animal salvaje característico. Cuando construyas o explores un bosque, 1d10+1d4 para árboles; lo mismo para animales salvajes.",
            color=discord.Color.green()
        )

        embed.set_author(
            name="Click aqui para ir a la documentacion oficial.",
            url="https://docs.google.com/document/d/1wnPvT7RU1o_hiH1Z-FabJDJ1SyXkV00c9YKCcsU3P9Q/edit"
        )

        embed.set_footer(
            text=f"Página {self.pagina_actual + 1} / {self.total_paginas}"
        )

        for b in chunk:

            animales_lista = []

            for a in self.animales:

                if a.getGrupo() == b.getGrupo():

                    animales_lista.append(a.getNombre())

            animales = ", ".join(animales_lista) #De esta forma concatenamos todos los animales, separados por ","

            embed.add_field(
                name=f"{b.getNombre().upper()}\n" + "‾" * (len(b.getNombre()) + 3),
                value= f"Grupo: {str(b.getGrupo())}",
                inline=False
            )

            embed.add_field(
                name="Animales que pueden aparecer:",
                value= animales,
                inline=False
            )

        return embed

    @discord.ui.button(label="◀️", style=discord.ButtonStyle.secondary)
    async def anterior(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.pagina_actual > 0:
            self.pagina_actual -= 1
            await interaction.response.edit_message(
                embed=self.crear_embed(),
                view=self
            )
        else:
            await interaction.response.defer()

    @discord.ui.button(label="▶️", style=discord.ButtonStyle.secondary)
    async def siguiente(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.pagina_actual < self.total_paginas - 1:
            self.pagina_actual += 1
            await interaction.response.edit_message(
                embed=self.crear_embed(),
                view=self
            )
        else:
            await interaction.response.defer()