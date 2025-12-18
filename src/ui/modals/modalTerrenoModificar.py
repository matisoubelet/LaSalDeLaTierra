from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from dominio.terreno import Terreno
from negocio.terrenoNegocio import TerrenoNegocio
import discord

class ModalTerrenoModificar(discord.ui.Modal):
    
    def __init__(self, terreno:Terreno):
        super().__init__(title=f"Modificar: {terreno.getNombre()}")
        self.terreno = terreno
        
        self.input_descripcion = discord.ui.TextInput(
            label="Descripción",
            default=str(terreno.getDescripcion()),
            style=discord.TextStyle.paragraph,
            placeholder="Descripción del terreno",
            max_length=500
        )
        self.add_item(self.input_descripcion)


    async def on_submit(self, interaction: discord.Interaction):

        #Verificamos que el campo tenga algun valor:
        if (not self.input_descripcion.value.strip()):

            await interaction.response.send_message("Debe completar el campo.", ephemeral=True)
            return

        terreno = Terreno(self.terreno.getID(), self.terreno.getNombre(), self.input_descripcion.value)
        
        negocio = TerrenoNegocio()
        negocio.modificar(terreno)

        await interaction.response.send_message("¡Modificacion realizada exitosamente!", ephemeral=True)
