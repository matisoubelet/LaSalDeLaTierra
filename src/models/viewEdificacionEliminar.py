import discord
from models.edificacion import Edificacion
from negocio.edificacionNegocio import EdificacionNegocio

MAX_EDIFICACIONES_POR_PAGINA = 1 


class ViewEdificacionEliminar(discord.ui.View):

    def __init__(self, edificacion: Edificacion, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.edificacion = edificacion

    def crear_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title="Confirmar eliminación",
            description="Estás a punto de eliminar la siguiente edificación:",
            color=discord.Color.red()
        )

        embed.add_field(
            name=self.edificacion.getNombre().upper(),
            value=self.edificacion.getDescripcion(),
            inline=False
        )

        embed.add_field(
            name="Industria",
            value=str(self.edificacion.getIndustria()),
            inline=True
        )

        embed.add_field(
            name="Riqueza",
            value=str(self.edificacion.getRiqueza()),
            inline=True
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
        
        edificacionNegocio = EdificacionNegocio()
        resultado = edificacionNegocio.eliminar(self.edificacion.getNombre())

        if resultado == -1:
            await interaction.response.edit_message(content="Hubo un error al intentar eliminar.", embed=None, view=None)
            return
        
        await interaction.response.edit_message(content="¡Edificacion eliminada exitosamente!.", embed=None, view=None)