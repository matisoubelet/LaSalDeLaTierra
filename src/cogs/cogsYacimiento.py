from discord.ext import commands
from discord import app_commands, Interaction

from negocio import YacimientoNegocio
from ui.views import ViewYacimiento, ViewYacimientoEliminar
from ui.modals import ModalYacimientoAgregar, ModalYacimientoModificar


class CogsYacimiento(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="yacimientos", description="Lista de yacimientos")
    async def yacimientos(self, interaction: Interaction):
        negocio = YacimientoNegocio()
        yacimientos = negocio.listar()

        if not yacimientos:
            await interaction.response.send_message(
                "No hay yacimientos registrados.", ephemeral=True
            )
            return

        view = ViewYacimiento(yacimientos)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )

    @app_commands.command(name="agregar_yacimiento", description="Agrega un yacimiento nuevo")
    async def agregar_yacimiento(self, interaction: Interaction, nombre: str):
        await interaction.response.send_modal(
            ModalYacimientoAgregar(nombre)
        )

    @app_commands.command(name="modificar_yacimiento", description="Modifica un yacimiento")
    async def modificar_yacimiento(self, interaction: Interaction, nombre: str):
        negocio = YacimientoNegocio()
        yacimiento = negocio.buscarXnombre(nombre)

        if yacimiento is None:
            await interaction.response.send_message(
                "El yacimiento no existe", ephemeral=True
            )
            return

        await interaction.response.send_modal(
            ModalYacimientoModificar(yacimiento)
        )

    @app_commands.command(name="eliminar_yacimiento", description="Elimina un yacimiento")
    async def eliminar_yacimiento(self, interaction: Interaction, nombre: str):
        negocio = YacimientoNegocio()
        yacimiento = negocio.buscarXnombre(nombre)

        if yacimiento is None:
            await interaction.response.send_message(
                "El yacimiento no existe", ephemeral=True
            )
            return

        view = ViewYacimientoEliminar(yacimiento)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )
