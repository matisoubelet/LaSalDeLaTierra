from discord.ext import commands
from discord import app_commands, Interaction

from negocio import AccionesDeUnidadNegocio
from ui.views import ViewAccionesDeUnidad, ViewAccionesDeUnidadEliminar
from ui.modals import ModalAccionesDeUnidadModificar, ModalAccionesDeUnidadAgregar


class CogsAccionesDeUnidad(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="acciones_de_unidad", description= "Lista de las acciones que puede tomar una unidad.")
    async def accionesDeUnidad(self, interaction: Interaction):

        accionesDeUnidadNegocio = AccionesDeUnidadNegocio()
        listAcciones = accionesDeUnidadNegocio.listar()

        if not listAcciones:
            await interaction.response.send_message("No hay acciones registradas.", ephemeral=True)
            return

        view = ViewAccionesDeUnidad(listAcciones)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


    @app_commands.command(name="modificar_accion_de_unidad", description="Modifica una accion de unidad")
    async def modificar_accion_de_unidad(self, interaction: Interaction, nombre: str, tipo: int):
        negocio = AccionesDeUnidadNegocio()
        accion = negocio.buscarXnombre(nombre, tipo)

        if accion is None:
            await interaction.response.send_message("La accion no existe", ephemeral=True)
            return

        await interaction.response.send_modal(ModalAccionesDeUnidadModificar(accion))


    @app_commands.command(name="agregar_accion_de_unidad", description="Agrega una accion de unidad")
    async def agregar_accion_de_unidad(self, interaction: Interaction, nombre: str):

        await interaction.response.send_modal(ModalAccionesDeUnidadAgregar(nombre))


    @app_commands.command(name="eliminar_accion_de_unidad", description="Elimina una accion de unidad.")
    async def eliminar_accion_de_unidad(self, interaction: Interaction, nombre: str, tipo: int):
        negocio = AccionesDeUnidadNegocio()
        accion = negocio.buscarXnombre(nombre, tipo)

        if accion is None:
            await interaction.response.send_message(
                "La accion no existe", ephemeral=True
            )
            return

        view = ViewAccionesDeUnidadEliminar(accion)
        await interaction.response.send_message(
            embed=view.crear_embed(),
            view=view,
            ephemeral=True
        )