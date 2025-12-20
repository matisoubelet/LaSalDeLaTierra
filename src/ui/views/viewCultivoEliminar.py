import discord
from dominio.cultivo import Cultivo
from negocio.cultivoNegocio import CultivoNegocio


class ViewCultivoEliminar(discord.ui.View):

    def __init__(self, cultivo: Cultivo, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.cultivo = cultivo

    def crear_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title="Confirmar eliminación",
            description="Estás a punto de eliminar el siguiente cultivo:",
            color=discord.Color.red()
        )

        if self.cultivo.getEstacion() == 0:

            embed.add_field(
                name=f"{self.cultivo.getNombre().upper()}\n" + "‾" * (len(self.cultivo.getNombre()) + 3),
                value= "Estacion: Primavera (0)",
                inline=False
            )

        elif self.cultivo.getEstacion() == 1:

            embed.add_field(
                name=f"{self.cultivo.getNombre().upper()}\n" + "‾" * (len(self.cultivo.getNombre()) + 3),
                value= "Estacion: Verano (1)",
                inline=False
            )

        else:

            embed.add_field(
                name=f"{self.cultivo.getNombre().upper()}\n" + "‾" * (len(self.cultivo.getNombre()) + 3),
                value= "Estacion: Otoño (2)",
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
        
        cultivoNegocio = CultivoNegocio()
        resultado = cultivoNegocio.eliminar(self.cultivo.getNombre())

        if resultado == -1:
            await interaction.response.edit_message(content="Hubo un error al intentar eliminar.", embed=None, view=None)
            return
        
        await interaction.response.edit_message(content="Cultivo eliminado exitosamente!.", embed=None, view=None)