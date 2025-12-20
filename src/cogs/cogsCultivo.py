from discord.ext import commands
from discord import app_commands, Interaction

from negocio import CultivoNegocio
from ui.views import ViewCultivo, ViewCultivoEliminar
from ui.modals import ModalCultivoAgregar, ModalCultivoModificar


class CogsCultivo(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="cultivos", description="Lista de cultivos")
    async def cultivos(self, interaction: Interaction):
        negocio = CultivoNegocio()
        cultivo = negocio.listar()

        if not cultivo:
            await interaction.response.send_message(
                "No hay cultivos registrados.", ephemeral=True
            )
            return

        view = ViewCultivo(cultivo)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )

    @app_commands.command(name="agregar_cultivo", description="Agrega un cultivo nuevo")
    async def agregar_cultivo(self, interaction: Interaction, nombre: str):
        await interaction.response.send_modal(
            ModalCultivoAgregar(nombre)
        )

    @app_commands.command(name="modificar_cultivo", description="Modifica un cultivo")
    async def modificar_cultivo(self, interaction: Interaction, nombre: str):
        negocio = CultivoNegocio()
        cultivo = negocio.buscarXnombre(nombre)

        if cultivo is None:
            await interaction.response.send_message(
                "El cultivo no existe", ephemeral=True
            )
            return

        await interaction.response.send_modal(
            ModalCultivoModificar(cultivo)
        )

    @app_commands.command(name="eliminar_cultivo", description="Elimina un cultivo")
    async def eliminar_cultivo(self, interaction: Interaction, nombre: str):
        negocio = CultivoNegocio()
        cultivo = negocio.buscarXnombre(nombre)

        if cultivo is None:
            await interaction.response.send_message(
                "El cultivo no existe", ephemeral=True
            )
            return

        view = ViewCultivoEliminar(cultivo)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )
