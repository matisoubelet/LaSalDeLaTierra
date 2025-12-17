from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from models.terreno import Terreno
from negocio.terrenoNegocio import TerrenoNegocio
import discord

class ModalTerrenoAgregar(discord.ui.Modal):
    
    def __init__(self, nombre):
        super().__init__(title=f"Agregar: {nombre}")
        self.nombre = nombre


        self.input_descripcion = discord.ui.TextInput(
            label="Descripción",
            style=discord.TextStyle.paragraph,
            placeholder="Descripción de la edificación",
            max_length=500
        )
        self.add_item(self.input_descripcion)


    async def on_submit(self, interaction: discord.Interaction):

        #Verificamos que todos los campos tengan algun valor valido
        if (not self.input_descripcion.value.strip()):

            await interaction.response.send_message("Debe completar todos los campos.", ephemeral=True)
            return
        
        negocio = TerrenoNegocio()
        agrego = negocio.agregar(self.nombre, self.input_descripcion.value)

        if(agrego == -1):
            await interaction.response.send_message("Hubo un error al intentar agregar la edificacion.", ephemeral=True)
        elif(agrego):
            await interaction.response.send_message("¡Edificacion agregada exitosamente!", ephemeral=True)
        else:
            await interaction.response.send_message("Edificacion existente, intente con otro nombre.", ephemeral=True)