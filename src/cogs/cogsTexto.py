from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
import discord
from negocio.terrenoNegocio import TerrenoNegocio
from negocio.edificacionNegocio import EdificacionNegocio
from models.terreno import Terreno
from models.edificacion import Edificacion
from models.modalEdificacionModificar import ModalEdificacionModificar
from models.modalEdificacionAgregar import ModalEdificacionAgregar
from models.viewEdificacion import ViewEdificacion


class CogsTexto(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="terrenos", description= "Lista de terrenos")
    async def terrenos(self, interaction: discord.Interaction):
        terrenoNegocio = TerrenoNegocio()
        listTerrenos = terrenoNegocio.listar()

        embed = discord.Embed(
                title = "TERRENOS",
                description = "Listado de los terrenos existentes.",
                color= discord.Color.green()
            )
        
        embed.set_author(
            name = "Click aqui para ir a la documentacion oficial.",
            url= "https://docs.google.com/document/d/1wnPvT7RU1o_hiH1Z-FabJDJ1SyXkV00c9YKCcsU3P9Q/edit?usp=sharing"
        )

        for t in listTerrenos:
            embed.add_field(
                name = f"{t.getNombre()}:",
                value = t.getDescripcion(),
                inline= False
                )
        
        await interaction.response.send_message(embed=embed)
    

    @app_commands.command(name="edificaciones", description= "Lista de edificaciones")
    async def edificaciones(self, interaction: discord.Interaction):
        edificacionNegocio = EdificacionNegocio()
        listEdificaciones = edificacionNegocio.listar(0)

        if not listEdificaciones:
            await interaction.response.send_message("No hay edificaciones registradas.", ephemeral=True)
            return

        view = ViewEdificacion(listEdificaciones)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view)


    @app_commands.command(name="industria", description= "Lista de edificaciones con costo en industria")
    async def industria(self, interaction: discord.Interaction):
        edificacionNegocio = EdificacionNegocio()
        listEdificaciones = edificacionNegocio.listar(1)

        if not listEdificaciones:
            await interaction.response.send_message("No hay edificaciones registradas.", ephemeral=True)
            return

        view = ViewEdificacion(listEdificaciones)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view)


    @app_commands.command(name="riqueza", description= "Lista de edificaciones con costo en riqueza")
    async def riqueza(self, interaction: discord.Interaction):
        edificacionNegocio = EdificacionNegocio()
        listEdificaciones = edificacionNegocio.listar(2)

        if not listEdificaciones:
            await interaction.response.send_message("No hay edificaciones registradas.", ephemeral=True)
            return

        view = ViewEdificacion(listEdificaciones)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view)


    @app_commands.command(name="modificar_edificacion", description= "Modifica una edificacion segun su nombre.")
    @app_commands.describe(nombre = "Nombre de la edificacion")
    async def modificarEdificacion(self, interaction: discord.Interaction, nombre:str):

        edificacionNegocio = EdificacionNegocio()
        edificacion = edificacionNegocio.buscarXnombre(nombre)

        if edificacion == None:
            await interaction.response.send_message("La edificacion no existe", ephemeral=True)
            return

        modal = ModalEdificacionModificar(edificacion)
        await interaction.response.send_modal(modal)

    
    @app_commands.command(name="agregar_edificacion", description= "Agrega una edificacion nueva.")
    @app_commands.describe(nombre = "Nombre de la edificacion")
    async def agregarEdificacion(self, interaction: discord.Interaction, nombre:str):

        modal = ModalEdificacionAgregar(nombre)
        await interaction.response.send_modal(modal)