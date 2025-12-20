import discord
from math import ceil
from typing import List
from dominio.terreno import Terreno


MAX_TERRENOS_POR_PAGINA = 5


class ViewTerreno(discord.ui.View):

    def __init__(self, terrenos: List[Terreno], timeout: int = 120):
        super().__init__(timeout=timeout)
        self.terrenos = terrenos
        self.pagina_actual = 0
        self.total_paginas = ceil(len(terrenos) / MAX_TERRENOS_POR_PAGINA) #ceil redondea para arriba, de forma que nunca nos falte espacio en el embed.

    def crear_embed(self) -> discord.Embed:
        inicio = self.pagina_actual * MAX_TERRENOS_POR_PAGINA
        fin = inicio + MAX_TERRENOS_POR_PAGINA
        chunk = self.terrenos[inicio:fin]

        embed = discord.Embed(
            title="TERRENOS",
            description="Cada terreno tiene características que permiten la construcción de ciertos asentamientos, ventajas y desventajas para para el traslado y el combate de una unidad, entre otras cosas.",
            color=discord.Color.dark_green()
        )

        embed.set_author(
            name="Click aqui para ir a la documentacion oficial.",
            url="https://docs.google.com/document/d/1wnPvT7RU1o_hiH1Z-FabJDJ1SyXkV00c9YKCcsU3P9Q/edit"
        )

        embed.set_footer(
            text=f"Página {self.pagina_actual + 1} / {self.total_paginas}"
        )

        for t in chunk:
            embed.add_field(
                name=f"{t.getNombre().upper()}\n" + "‾" * (len(t.getNombre()) + 3),
                value=t.getDescripcion(),
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