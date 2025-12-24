import discord
from dominio.bosque import Bosque
from negocio.bosqueNegocio import BosqueNegocio


class ViewBosqueEliminar(discord.ui.View):

    def __init__(self, bosque: Bosque, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.bosque = bosque

    def crear_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title="Confirmar eliminación",
            description="Estás a punto de eliminar el siguiente bosque:",
            color=discord.Color.red()
        )

        embed.add_field(
            name=f"{self.bosque.getNombre().upper()}\n" + "‾" * (len(self.bosque.getNombre()) + 3),
            value= f"Grupo: {self.bosque.getGrupo()}",
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
        
        bosqueNegocio = BosqueNegocio()
        resultado = bosqueNegocio.eliminar(self.bosque.getNombre())

        if resultado == -1:
            await interaction.response.edit_message(content="Hubo un error al intentar eliminar.", embed=None, view=None)
            return
        
        await interaction.response.edit_message(content="Bosque eliminado exitosamente!.", embed=None, view=None)