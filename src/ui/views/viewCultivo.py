import discord
from math import ceil
from typing import List
from dominio.cultivo import Cultivo


MAX_CULTIVO_POR_PAGINA = 12


class ViewCultivo(discord.ui.View):

    def __init__(self, cultivo: List[Cultivo], timeout: int = 120):
        super().__init__(timeout=timeout)
        self.cultivo = cultivo
        self.pagina_actual = 0
        self.total_paginas = ceil(len(cultivo) / MAX_CULTIVO_POR_PAGINA) #ceil redondea para arriba, de forma que nunca nos falte espacio en el embed.

    def crear_embed(self) -> discord.Embed:
        inicio = self.pagina_actual * MAX_CULTIVO_POR_PAGINA
        fin = inicio + MAX_CULTIVO_POR_PAGINA
        chunk = self.cultivo[inicio:fin]

        embed = discord.Embed(
            title="CULTIVOS",
            description="La tierra fértil es el terreno más abundante del mapa, y por eso sólo se consigue un sólo producto de ellas. Tirás 1d12  y luego 1d4 para determinar el producto.",
            color=discord.Color.green()
        )

        embed.set_author(
            name="Click aqui para ir a la documentacion oficial.",
            url="https://docs.google.com/document/d/1wnPvT7RU1o_hiH1Z-FabJDJ1SyXkV00c9YKCcsU3P9Q/edit"
        )

        embed.set_footer(
            text=f"Página {self.pagina_actual + 1} / {self.total_paginas}"
        )

        for c in chunk:

            if c.getEstacion() == 0:

                embed.add_field(
                    name=f"{c.getNombre().upper()}\n" + "‾" * (len(c.getNombre()) + 3),
                    value= "Estacion: Primavera (0)",
                    inline=False
                )

            elif c.getEstacion() == 1:

                embed.add_field(
                    name=f"{c.getNombre().upper()}\n" + "‾" * (len(c.getNombre()) + 3),
                    value= "Estacion: Verano (1)",
                    inline=False
                )

            else:

                embed.add_field(
                    name=f"{c.getNombre().upper()}\n" + "‾" * (len(c.getNombre()) + 3),
                    value= "Estacion: Otoño (2)",
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