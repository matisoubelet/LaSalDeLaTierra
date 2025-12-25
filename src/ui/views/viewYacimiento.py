import discord
from math import ceil
from typing import List
from dominio.yacimiento import Yacimiento


MAX_YACIMIENTO_POR_PAGINA = 10


class ViewYacimiento(discord.ui.View):

    def __init__(self, yacimientos: List[Yacimiento], timeout: int = 120):
        super().__init__(timeout=timeout)
        self.yacimientos = yacimientos
        self.pagina_actual = 0
        self.total_paginas = ceil(len(yacimientos) / MAX_YACIMIENTO_POR_PAGINA) #ceil redondea para arriba, de forma que nunca nos falte espacio en el embed.

    def crear_embed(self) -> discord.Embed:
        inicio = self.pagina_actual * MAX_YACIMIENTO_POR_PAGINA
        fin = inicio + MAX_YACIMIENTO_POR_PAGINA
        chunk = self.yacimientos[inicio:fin]

        embed = discord.Embed(
            title="YACIMIENTOS",
            description="Los yacimientos minerales contienen tres categorías de productos; piedra, gema y metales. Cuando construís un asentamiento sobre un yacimiento mineral, obtienes uno de cada categoría, determinado por 1d20. Es posible extraer más del mismo producto, o cavar más profundo para encontrar otros nuevos, con edificaciones.",
            color=discord.Color.dark_grey()
        )

        embed.set_author(
            name="Click aqui para ir a la documentacion oficial.",
            url="https://docs.google.com/document/d/1wnPvT7RU1o_hiH1Z-FabJDJ1SyXkV00c9YKCcsU3P9Q/edit"
        )

        embed.set_footer(
            text=f"Página {self.pagina_actual + 1} / {self.total_paginas}"
        )

        for y in chunk:

            if y.getTipo() == 0:

                embed.add_field(
                    name=f"{y.getNombre().upper()}\n" + "‾" * (len(y.getNombre()) + 3),
                    value= "Tipo: Piedra (0)",
                    inline=False
                )

            elif y.getTipo() == 1:

                embed.add_field(
                    name=f"{y.getNombre().upper()}\n" + "‾" * (len(y.getNombre()) + 3),
                    value= "Tipo: Gema (1)",
                    inline=False
                )
            
            else:

                embed.add_field(
                    name=f"{y.getNombre().upper()}\n" + "‾" * (len(y.getNombre()) + 3),
                    value= "Tipo: Metal (2)",
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