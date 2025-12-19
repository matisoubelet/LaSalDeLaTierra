import discord
from dominio.accionesDeCiudad import AccionesDeCiudad
from negocio.accionesDeCiudadNegocio import AccionesDeCiudadNegocio

MAX_EDIFICACIONES_POR_PAGINA = 1 


class ViewAccionesDeCiudadEliminar(discord.ui.View):

    def __init__(self, accion: AccionesDeCiudad, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.accion = accion

    def crear_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title="Confirmar eliminación",
            description="Estás a punto de eliminar la siguiente accion:",
            color=discord.Color.red()
        )

        embed.add_field(
                name=self.accion.getNombre().upper(),
                value=self.accion.getDescripcion(),
                inline=False
            )

        embed.add_field(
            name="Requisito:",
            value=str(self.accion.getRequisito()),
            inline=False
        )

        embed.add_field(
            name="Industria:",
            value=str(self.accion.getIndustria()),
            inline=True
        )

        embed.add_field(
            name="Poblacion:",
            value=str(self.accion.getPoblacion()),
            inline=True
        )

        embed.add_field(
            name="Riqueza:",
            value=str(self.accion.getRiqueza()),
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
        
        accionDeCiudadNegocio = AccionesDeCiudadNegocio()
        resultado = accionDeCiudadNegocio.eliminar(self.accion.getNombre())

        if resultado == -1:
            await interaction.response.edit_message(content="Hubo un error al intentar eliminar.", embed=None, view=None)
            return
        
        await interaction.response.edit_message(content="¡Accion eliminada exitosamente!.", embed=None, view=None)