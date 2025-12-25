from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from negocio.cultivoNegocio import CultivoNegocio
import discord

class ModalCultivoAgregar(discord.ui.Modal):
    
    def __init__(self, nombre):
        super().__init__(title=f"Agregar: {nombre}")
        self.nombre = nombre


        self.input_estacion = discord.ui.TextInput(
            label="Estacion (numero)",
            placeholder="0 Primavera, 1 Verano, 2 Otoño, 3 Cualquiera.",
        )
        self.add_item(self.input_estacion)


    async def on_submit(self, interaction: discord.Interaction):

        #Verificamos que todos los campos tengan algun valor valido
        if (not self.input_estacion.value.strip()):

            await interaction.response.send_message("Debe completar el campo.", ephemeral=True)
            return
        
        #Validamos que el valor sea numerico
        try:
            estacion = int(self.input_estacion.value)
            
        except ValueError:
            await interaction.response.send_message("No se ingreso un valor numerico.", ephemeral=True)
            return

        #Validamos el numero este dentro del rango
        if estacion < 0 or estacion > 3:
            await interaction.response.send_message("Debe ingresar valores numéricos entre 0 a 3.", ephemeral=True)
            return

        negocio = CultivoNegocio()
        agrego = negocio.agregar(self.nombre, estacion)

        if(agrego == -1):
            await interaction.response.send_message("Hubo un error al intentar agregar el cultivo.", ephemeral=True)
        elif(agrego):
            await interaction.response.send_message("Cultivo agregado exitosamente!", ephemeral=True)
        else:
            await interaction.response.send_message("Cultivo existente, intente con otro nombre.", ephemeral=True)