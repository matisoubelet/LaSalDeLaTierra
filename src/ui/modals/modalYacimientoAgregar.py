from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from negocio.yacimientoNegocio import YacimientoNegocio
import discord

class ModalYacimientoAgregar(discord.ui.Modal):
    
    def __init__(self, nombre):
        super().__init__(title=f"Agregar: {nombre}")
        self.nombre = nombre


        self.input_tipo = discord.ui.TextInput(
            label="Tipo (numero)",
            placeholder="0 Piedra, 1 Gema, 2 Metal.",
        )
        self.add_item(self.input_tipo)


    async def on_submit(self, interaction: discord.Interaction):

        #Verificamos que todos los campos tengan algun valor valido
        if (not self.input_tipo.value.strip()):

            await interaction.response.send_message("Debe completar el campo.", ephemeral=True)
            return
        
        #Validamos que el valor sea numerico
        try:
            tipo = int(self.input_tipo.value)
            
        except ValueError:
            await interaction.response.send_message("No se ingreso un valor numerico.", ephemeral=True)
            return

        #Validamos el numero este dentro del rango
        if tipo < 0 or tipo > 2:
            await interaction.response.send_message("Debe ingresar valores numéricos entre 0 a 2.", ephemeral=True)
            return

        negocio = YacimientoNegocio()
        agrego = negocio.agregar(self.nombre, tipo)

        if(agrego == -1):
            await interaction.response.send_message("Hubo un error al intentar agregar el yacimiento.", ephemeral=True)
        elif(agrego):
            await interaction.response.send_message("Yacimiento agregado exitosamente!", ephemeral=True)
        else:
            await interaction.response.send_message("Yacimiento existente, intente con otro nombre.", ephemeral=True)