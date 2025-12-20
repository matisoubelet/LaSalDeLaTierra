import discord
from math import ceil
from typing import List
from dominio.accionesDeUnidad import AccionesDeUnidad


MAX_ACCIONES_POR_PAGINA = 5  #Este numero es especifico para las edificaciones, dado que cada una ocupa 3 fields. Cuando hagas otra paginacion, revisalo.


class ViewAccionesDeUnidad(discord.ui.View):

    def __init__(self, acciones: List[AccionesDeUnidad], timeout: int = 120):
        super().__init__(timeout=timeout)
        self.acciones = acciones
        self.pagina_actual = 0
        self.total_paginas = ceil(len(acciones) / MAX_ACCIONES_POR_PAGINA) #ceil redondea para arriba, de forma que nunca nos falte espacio en el embed.

    def crear_embed(self) -> discord.Embed:
        inicio = self.pagina_actual * MAX_ACCIONES_POR_PAGINA
        fin = inicio + MAX_ACCIONES_POR_PAGINA
        chunk = self.acciones[inicio:fin]

        embed = discord.Embed(
            title="ACCIONES DE UNIDAD",
            description="Todas las unidades pueden desplazarse por el mapa una cantidad de casilleros determinada en las estadísticas de la unidad. Luego de ese primer movimiento, cada Unidad puede tomar una sola Acción de Unidad de la lista que se muestra a continuación. Algunas tienen costo, otras son gratis:",
            color=discord.Color.blue()
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

            if a.getTipo() == 0:

                embed.add_field(
                    name="Tipo:",
                    value=f"Militar ({a.getTipo()})",
                    inline=True
                )

            elif a.getTipo() == 1:

                embed.add_field(
                    name="Tipo:",
                    value=f"Caravana ({a.getTipo()})",
                    inline=True
                )

            elif a.getTipo() == 2:

                embed.add_field(
                    name="Tipo:",
                    value=f"Explorador ({a.getTipo()})",
                    inline=True
                )
            
            else:

                embed.add_field(
                    name="Tipo:",
                    value=f"Cualquiera ({a.getTipo()})",
                    inline=True
                )

            embed.add_field(
                name="Industria:",
                value=str(a.getIndustria()),
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