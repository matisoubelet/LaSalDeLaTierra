import discord
from dominio.yacimiento import Yacimiento
from negocio.yacimientoNegocio import YacimientoNegocio


class ViewYacimientoEliminar(discord.ui.View):

    def __init__(self, yacimiento: Yacimiento, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.yacimiento = yacimiento

    def crear_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title="Confirmar eliminación",
            description="Estás a punto de eliminar el siguiente yacimiento:",
            color=discord.Color.red()
        )

        if self.yacimiento.getTipo() == 0:

                embed.add_field(
                    name=f"{self.yacimiento.getNombre().upper()}\n" + "‾" * (len(self.yacimiento.getNombre()) + 3),
                    value= "Tipo: Piedra (0)",
                    inline=False
                )

        elif self.yacimiento.getTipo() == 1:

                embed.add_field(
                    name=f"{self.yacimiento.getNombre().upper()}\n" + "‾" * (len(self.yacimiento.getNombre()) + 3),
                    value= "Tipo: Gema (1)",
                    inline=False
                )
            
        else:

                embed.add_field(
                    name=f"{self.yacimiento.getNombre().upper()}\n" + "‾" * (len(self.yacimiento.getNombre()) + 3),
                    value= "Tipo: Metal (2)",
                    inline=False
                )

        return embed
    

    @discord.ui.button(label="❌ Cancelar", style=discord.ButtonStyle.secondary)
    async def cancelar(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            content="Eliminación cancelada.",
            embed=None,
            view=None
        )

    @discord.ui.button(label="🗑️ Eliminar", style=discord.ButtonStyle.danger)
    async def eliminar(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        yacimientoNegocio = YacimientoNegocio()
        resultado = yacimientoNegocio.eliminar(self.yacimiento.getNombre())

        if resultado == -1:
            await interaction.response.edit_message(content="Hubo un error al intentar eliminar.", embed=None, view=None)
            return
        
        await interaction.response.edit_message(content="Yacimiento eliminado exitosamente!.", embed=None, view=None)