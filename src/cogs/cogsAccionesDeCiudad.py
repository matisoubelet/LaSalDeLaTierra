from discord.ext import commands
from discord import app_commands, Interaction

from negocio import AccionesDeCiudadNegocio
from ui.views import ViewAccionesDeCiudad
from ui.modals import ModalAccionesDeCiudadModificar


class CogsAccionesDeCiudad(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="acciones_de_ciudad", description= "Lista de las acciones que puede tomar una ciudad.")
    async def accionesDeCiudad(self, interaction: Interaction):

        accionesDeCiudadNegocio = AccionesDeCiudadNegocio()
        listAcciones = accionesDeCiudadNegocio.listar()

        if not listAcciones:
            await interaction.response.send_message("No hay acciones registradas.", ephemeral=True)
            return

        view = ViewAccionesDeCiudad(listAcciones)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


    @app_commands.command(name="modificar_accion_de_ciudad", description="Modifica una accion de ciudad")
    async def modificar_accion_de_ciudad(self, interaction: Interaction, nombre: str):
        negocio = AccionesDeCiudadNegocio()
        accion = negocio.buscarXnombre(nombre)

        if accion is None:
            await interaction.response.send_message("La accion no existe", ephemeral=True)
            return

        await interaction.response.send_modal(ModalAccionesDeCiudadModificar(accion))