from discord.ext import commands
from discord import app_commands, Interaction

from negocio import BosqueNegocio, AnimalNegocio
from ui.views import ViewBosque, ViewBosqueEliminar
from ui.modals import ModalBosqueAgregar, ModalBosqueModificar

class CogsBosque(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="bosques", description="Lista de los bosques y sus animales")
    async def bosques(self, interaction: Interaction):
        bosqueNegocio = BosqueNegocio()
        animalNegocio = AnimalNegocio()

        bosques = bosqueNegocio.listar()
        animales = animalNegocio.listar()

        if not bosques:
            await interaction.response.send_message(
                "No hay bosques registrados.", ephemeral=True
            )
            return

        view = ViewBosque(bosques, animales)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )

    @app_commands.command(name="agregar_bosque", description="Agrega un bosque nuevo")
    async def agregar_bosque(self, interaction: Interaction, nombre: str):
        await interaction.response.send_modal(
            ModalBosqueAgregar(nombre)
        )

    @app_commands.command(name="modificar_bosque", description="Modifica un bosque")
    async def modificar_bosque(self, interaction: Interaction, nombre: str):
        negocio = BosqueNegocio()
        bosque = negocio.buscarXnombre(nombre)

        if bosque is None:
            await interaction.response.send_message(
                "El bosque no existe", ephemeral=True
            )
            return

        await interaction.response.send_modal(
            ModalBosqueModificar(bosque)
        )

    @app_commands.command(name="eliminar_bosque", description="Elimina un bosque")
    async def eliminar_bosque(self, interaction: Interaction, nombre: str):
        negocio = BosqueNegocio()
        bosque = negocio.buscarXnombre(nombre)

        if bosque is None:
            await interaction.response.send_message(
                "El bosque no existe", ephemeral=True
            )
            return

        view = ViewBosqueEliminar(bosque)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )
