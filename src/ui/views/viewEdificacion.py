import discord
from math import ceil
from typing import List
from dominio.edificacion import Edificacion


MAX_EDIFICACIONES_POR_PAGINA = 5  #Este numero es especifico para las edificaciones, dado que cada una ocupa 3 fields. Cuando hagas otra paginacion, revisalo.


class ViewEdificacion(discord.ui.View):

    def __init__(self, edificaciones: List[Edificacion], timeout: int = 120):
        super().__init__(timeout=timeout)
        self.edificaciones = edificaciones
        self.pagina_actual = 0
        self.total_paginas = ceil(len(edificaciones) / MAX_EDIFICACIONES_POR_PAGINA) #ceil redondea para arriba, de forma que nunca nos falte espacio en el embed.

    def crear_embed(self) -> discord.Embed:
        inicio = self.pagina_actual * MAX_EDIFICACIONES_POR_PAGINA
        fin = inicio + MAX_EDIFICACIONES_POR_PAGINA
        chunk = self.edificaciones[inicio:fin]

        embed = discord.Embed(
            title="EDIFICACIONES",
            description="Dentro de cada Ciudad hay espacio para Edificaciones; éstas son construcciones internas que no ocupan espacio en el mapa sino en la Ciudad misma. Las Edificaciones permiten que la civilización pueda realizar nuevas acciones, o entrenar nuevos tipos de unidades.Todas las Ciudades pueden tener hasta 6 Edificaciones. Los Asentamientos pueden tener hasta 2 Edificaciones.",
            color=discord.Color.purple()
        )

        embed.set_author(
            name="Click aqui para ir a la documentacion oficial.",
            url="https://docs.google.com/document/d/1wnPvT7RU1o_hiH1Z-FabJDJ1SyXkV00c9YKCcsU3P9Q/edit"
        )

        embed.set_footer(
            text=f"Página {self.pagina_actual + 1} / {self.total_paginas}"
        )

        for e in chunk:
            embed.add_field(
                name=f"{e.getNombre().upper()}\n" + "‾" * (len(e.getNombre()) + 3),
                value=e.getDescripcion(),
                inline=False
            )

            embed.add_field(
                name="Industria:",
                value=str(e.getIndustria()),
                inline=True
            )

            if e.getRiqXturno():
                riqueza = f"{e.getRiqueza()} X turno"
            else:
                riqueza = str(e.getRiqueza())

            embed.add_field(
                name="Riqueza:",
                value=riqueza,
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