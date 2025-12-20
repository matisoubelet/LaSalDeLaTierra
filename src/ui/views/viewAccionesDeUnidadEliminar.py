import discord
from dominio.accionesDeUnidad import AccionesDeUnidad
from negocio.accionesDeUnidadNegocio import AccionesDeUnidadNegocio


class ViewAccionesDeUnidadEliminar(discord.ui.View):

    def __init__(self, accion: AccionesDeUnidad, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.accion = accion

    def crear_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title="Confirmar eliminación",
            description="Estás a punto de eliminar la siguiente accion:",
            color=discord.Color.red()
        )

        embed.add_field(
                name=f"{self.accion.getNombre().upper()}\n" + "‾" * (len(self.accion.getNombre()) + 3),
                value=self.accion.getDescripcion(),
                inline=False
            )

        if self.accion.getTipo() == 0:

            embed.add_field(
                name="Tipo:",
                value=f"Militar ({self.accion.getTipo()})",
                inline=True
            )

        elif self.accion.getTipo() == 1:

            embed.add_field(
                name="Tipo:",
                value=f"Caravana ({self.accion.getTipo()})",
                inline=True
            )

        elif self.accion.getTipo() == 2:

                embed.add_field(
                    name="Tipo:",
                    value=f"Explorador ({self.accion.getTipo()})",
                    inline=True
                )
            
        else:

            embed.add_field(
                name="Tipo:",
                value=f"Cualquiera ({self.accion.getTipo()})",
                inline=True
            )

        embed.add_field(
            name="Industria:",
            value=str(self.accion.getIndustria()),
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
        
        accionDeUnidadNegocio = AccionesDeUnidadNegocio()
        resultado = accionDeUnidadNegocio.eliminar(self.accion.getNombre(), self.accion.getTipo())

        if resultado == -1:
            await interaction.response.edit_message(content="Hubo un error al intentar eliminar.", embed=None, view=None)
            return
        
        await interaction.response.edit_message(content="¡Accion eliminada exitosamente!.", embed=None, view=None)