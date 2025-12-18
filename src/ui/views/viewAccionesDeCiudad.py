import discord
from math import ceil
from typing import List
from dominio.accionesDeCiudad import AccionesDeCiudad


MAX_ACCIONES_POR_PAGINA = 4  #Este numero es especifico para las edificaciones, dado que cada una ocupa 3 fields. Cuando hagas otra paginacion, revisalo.


class ViewAccionesDeCiudad(discord.ui.View):

    def __init__(self, acciones: List[AccionesDeCiudad], timeout: int = 120):
        super().__init__(timeout=timeout)
        self.acciones = acciones
        self.pagina_actual = 0
        self.total_paginas = ceil(len(acciones) / MAX_ACCIONES_POR_PAGINA) #ceil redondea para arriba, de forma que nunca nos falte espacio en el embed.

    def crear_embed(self) -> discord.Embed:
        inicio = self.pagina_actual * MAX_ACCIONES_POR_PAGINA
        fin = inicio + MAX_ACCIONES_POR_PAGINA
        chunk = self.acciones[inicio:fin]

        embed = discord.Embed(
            title="ACCIONES DE CIUDAD",
            description="Lista de las acciones que puede tomar una ciudad.",
            color=discord.Color.purple()
        )

        embed.set_author(
            name="Click aqui para ir a la documentacion oficial.",
            url="https://docs.google.com/document/d/1wnPvT7RU1o_hiH1Z-FabJDJ1SyXkV00c9YKCcsU3P9Q/edit"
        )

        embed.set_footer(
            text=f"Página {self.pagina_actual + 1} / {self.total_paginas}"
        )

        for a in chunk:
            embed.add_field(
                name=f"{a.getNombre().upper()}\n" + "‾" * (len(a.getNombre()) + 3),
                value=a.getDescripcion(),
                inline=False
            )

            embed.add_field(
                name="Requisito:",
                value=str(a.getRequisito()),
                inline=False
            )

            embed.add_field(
                name="Industria:",
                value=str(a.getIndustria()),
                inline=True
            )

            embed.add_field(
                name="Poblacion:",
                value=str(a.getPoblacion()),
                inline=True
            )

            embed.add_field(
                name="Riqueza:",
                value=str(a.getRiqueza()),
                inline=True
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