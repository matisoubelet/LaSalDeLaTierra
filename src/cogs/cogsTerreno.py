from discord.ext import commands
from discord import app_commands, Interaction

from negocio import TerrenoNegocio
from ui.views import ViewTerreno, ViewTerrenoEliminar
from ui.modals import ModalTerrenoAgregar, ModalTerrenoModificar


class CogsTerreno(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="terrenos", description="Lista de terrenos")
    async def terrenos(self, interaction: Interaction):
        negocio = TerrenoNegocio()
        terrenos = negocio.listar()

        if not terrenos:
            await interaction.response.send_message(
                "No hay terrenos registrados.", ephemeral=True
            )
            return

        view = ViewTerreno(terrenos)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )

    @app_commands.command(name="agregar_terreno", description="Agrega un terreno nuevo")
    async def agregar_terreno(self, interaction: Interaction, nombre: str):
        await interaction.response.send_modal(
            ModalTerrenoAgregar(nombre)
        )

    @app_commands.command(name="modificar_terreno", description="Modifica un terreno")
    async def modificar_terreno(self, interaction: Interaction, nombre: str):
        negocio = TerrenoNegocio()
        terreno = negocio.buscarXnombre(nombre)

        if terreno is None:
            await interaction.response.send_message(
                "El terreno no existe", ephemeral=True
            )
            return

        await interaction.response.send_modal(
            ModalTerrenoModificar(terreno)
        )

    @app_commands.command(name="eliminar_terreno", description="Elimina un terreno")
    async def eliminar_terreno(self, interaction: Interaction, nombre: str):
        negocio = TerrenoNegocio()
        terreno = negocio.buscarXnombre(nombre)

        if terreno is None:
            await interaction.response.send_message(
                "El terreno no existe", ephemeral=True
            )
            return

        view = ViewTerrenoEliminar(terreno)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )
