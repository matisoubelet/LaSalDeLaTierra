import discord
from dominio.terreno import Terreno
from negocio.terrenoNegocio import TerrenoNegocio


class ViewTerrenoEliminar(discord.ui.View):

    def __init__(self, terreno: Terreno, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.terreno = terreno

    def crear_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title="Confirmar eliminación",
            description="Estás a punto de eliminar el siguiente terreno:",
            color=discord.Color.red()
        )

        embed.add_field(
            name=self.terreno.getNombre().upper(),
            value=self.terreno.getDescripcion(),
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
        
        terrenoNegocio = TerrenoNegocio()
        resultado = terrenoNegocio.eliminar(self.terreno.getNombre())

        if resultado == -1:
            await interaction.response.edit_message(content="Hubo un error al intentar eliminar.", embed=None, view=None)
            return
        
        await interaction.response.edit_message(content="¡Terreno eliminado exitosamente!.", embed=None, view=None)