from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
import discord
from negocio import TerrenoNegocio, EdificacionNegocio, AccionesDeCiudadNegocio
from ui.modals import ModalTerrenoAgregar, ModalEdificacionAgregar, ModalEdificacionModificar, ModalTerrenoModificar
from ui.views import ViewTerrenoEliminar, ViewEdificacion, ViewEdificacionEliminar, ViewTerreno, ViewAccionesDeCiudad
class Cogs(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="terrenos", description= "Lista de terrenos")
    async def terrenos(self, interaction: discord.Interaction):
        terrenoNegocio = TerrenoNegocio()
        listTerrenos = terrenoNegocio.listar()

        if not listTerrenos:
            await interaction.response.send_message("No hay terrenos registrados.", ephemeral=True)
            return

        view = ViewTerreno(listTerrenos)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

    
    @app_commands.command(name="agregar_terreno", description= "Agrega un terreno nuevo.")
    @app_commands.describe(nombre = "Nombre del terreno")
    async def agregarTerreno(self, interaction: discord.Interaction, nombre:str):

        modal = ModalTerrenoAgregar(nombre)
        await interaction.response.send_modal(modal)

    
    @app_commands.command(name="modificar_terreno", description= "Modifica un terreno segun su nombre.")
    @app_commands.describe(nombre = "Nombre del terreno")
    async def modificarTerreno(self, interaction: discord.Interaction, nombre:str):

        terrenoNegocio = TerrenoNegocio()
        terreno = terrenoNegocio.buscarXnombre(nombre)

        if terreno is None:
            await interaction.response.send_message("El terreno no existe", ephemeral=True)
            return

        modal = ModalTerrenoModificar(terreno)
        await interaction.response.send_modal(modal)

    
    @app_commands.command(name="eliminar_terreno", description= "Elimina un terreno.")
    @app_commands.describe(nombre = "Nombre del terreno")
    async def eliminarTerreno(self, interaction: discord.Interaction, nombre:str):

        terrenoNegocio = TerrenoNegocio()
        terreno = terrenoNegocio.buscarXnombre(nombre)

        if terreno is None:
            await interaction.response.send_message("El terreno no existe", ephemeral=True)
            return
        
        view = ViewTerrenoEliminar(terreno)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
    

    @app_commands.command(name="edificaciones", description= "Lista de edificaciones")
    async def edificaciones(self, interaction: discord.Interaction):
        edificacionNegocio = EdificacionNegocio()
        listEdificaciones = edificacionNegocio.listar(0)

        if not listEdificaciones:
            await interaction.response.send_message("No hay edificaciones registradas.", ephemeral=True)
            return

        view = ViewEdificacion(listEdificaciones)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


    @app_commands.command(name="industria", description= "Lista de edificaciones con costo en industria")
    async def industria(self, interaction: discord.Interaction):
        edificacionNegocio = EdificacionNegocio()
        listEdificaciones = edificacionNegocio.listar(1)

        if not listEdificaciones:
            await interaction.response.send_message("No hay edificaciones registradas.", ephemeral=True)
            return

        view = ViewEdificacion(listEdificaciones)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


    @app_commands.command(name="riqueza", description= "Lista de edificaciones con costo en riqueza")
    async def riqueza(self, interaction: discord.Interaction):
        edificacionNegocio = EdificacionNegocio()
        listEdificaciones = edificacionNegocio.listar(2)

        if not listEdificaciones:
            await interaction.response.send_message("No hay edificaciones registradas.", ephemeral=True)
            return

        view = ViewEdificacion(listEdificaciones)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


    @app_commands.command(name="modificar_edificacion", description= "Modifica una edificacion segun su nombre.")
    @app_commands.describe(nombre = "Nombre de la edificacion")
    async def modificarEdificacion(self, interaction: discord.Interaction, nombre:str):

        edificacionNegocio = EdificacionNegocio()
        edificacion = edificacionNegocio.buscarXnombre(nombre)

        if edificacion is None:
            await interaction.response.send_message("La edificacion no existe", ephemeral=True)
            return

        modal = ModalEdificacionModificar(edificacion)
        await interaction.response.send_modal(modal)

    
    @app_commands.command(name="agregar_edificacion", description= "Agrega una edificacion nueva.")
    @app_commands.describe(nombre = "Nombre de la edificacion")
    async def agregarEdificacion(self, interaction: discord.Interaction, nombre:str):

        modal = ModalEdificacionAgregar(nombre)
        await interaction.response.send_modal(modal)

    
    @app_commands.command(name="eliminar_edificacion", description= "Elimina una edificacion.")
    @app_commands.describe(nombre = "Nombre de la edificacion")
    async def eliminarEdificacion(self, interaction: discord.Interaction, nombre:str):

        edificacionNegocio = EdificacionNegocio()
        edificacion = edificacionNegocio.buscarXnombre(nombre)

        if edificacion is None:
            await interaction.response.send_message("La edificacion no existe", ephemeral=True)
            return
        
        view = ViewEdificacionEliminar(edificacion)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)


    
    @app_commands.command(name="acciones_de_ciudad", description= "Lista de las acciones que puede tomar una ciudad.")
    async def accionesDeCiudad(self, interaction: discord.Interaction):

        accionesDeCiudadNegocio = AccionesDeCiudadNegocio()
        listAcciones = accionesDeCiudadNegocio.listar()

        if not listAcciones:
            await interaction.response.send_message("No hay acciones registradas.", ephemeral=True)
            return

        view = ViewAccionesDeCiudad(listAcciones)
        embed = view.crear_embed()

        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

