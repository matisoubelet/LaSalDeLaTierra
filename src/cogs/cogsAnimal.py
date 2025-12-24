from discord.ext import commands
from discord import app_commands, Interaction

from negocio import AnimalNegocio
from ui.views import ViewAnimalEliminar
from ui.modals import ModalAnimalAgregar, ModalAnimalModificar


class CogsAnimal(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @app_commands.command(name="agregar_animal", description="Agrega un animal nuevo")
    async def agregar_animal(self, interaction: Interaction, nombre: str):
        await interaction.response.send_modal(
            ModalAnimalAgregar(nombre)
        )

    @app_commands.command(name="modificar_animal", description="Modifica un animal")
    async def modificar_animal(self, interaction: Interaction, nombre: str):
        negocio = AnimalNegocio()
        animal = negocio.buscarXnombre(nombre)

        if animal is None:
            await interaction.response.send_message(
                "El animal no existe", ephemeral=True
            )
            return

        await interaction.response.send_modal(
            ModalAnimalModificar(animal)
        )

    @app_commands.command(name="eliminar_animal", description="Elimina un animal")
    async def eliminar_animal(self, interaction: Interaction, nombre: str):
        negocio = AnimalNegocio()
        animal = negocio.buscarXnombre(nombre)

        if animal is None:
            await interaction.response.send_message(
                "El animal no existe", ephemeral=True
            )
            return

        view = ViewAnimalEliminar(animal)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )
