from discord.ext import commands
from discord import app_commands, Interaction

from negocio import EdificacionNegocio
from ui.views import ViewEdificacion, ViewEdificacionEliminar
from ui.modals import ModalEdificacionAgregar, ModalEdificacionModificar


class CogsEdificacion(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name="edificaciones", description="Lista de edificaciones")
    async def edificaciones(self, interaction: Interaction):
        negocio = EdificacionNegocio()
        edificaciones = negocio.listar(0)

        if not edificaciones:
            await interaction.response.send_message(
                "No hay edificaciones registradas.", ephemeral=True
            )
            return

        view = ViewEdificacion(edificaciones)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )
        

    @app_commands.command(name="agregar_edificacion", description="Agrega una edificacion")
    async def agregar_edificacion(self, interaction: Interaction, nombre: str):
        await interaction.response.send_modal(
            ModalEdificacionAgregar(nombre)
        )


    @app_commands.command(name="modificar_edificacion", description="Modifica una edificacion")
    async def modificar_edificacion(self, interaction: Interaction, nombre: str):
        negocio = EdificacionNegocio()
        edificacion = negocio.buscarXnombre(nombre)

        if edificacion is None:
            await interaction.response.send_message(
                "La edificacion no existe", ephemeral=True
            )
            return

        await interaction.response.send_modal(
            ModalEdificacionModificar(edificacion)
        )


    @app_commands.command(name="eliminar_edificacion", description="Elimina una edificacion")
    async def eliminar_edificacion(self, interaction: Interaction, nombre: str):
        negocio = EdificacionNegocio()
        edificacion = negocio.buscarXnombre(nombre)

        if edificacion is None:
            await interaction.response.send_message(
                "La edificacion no existe", ephemeral=True
            )
            return

        view = ViewEdificacionEliminar(edificacion)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )
