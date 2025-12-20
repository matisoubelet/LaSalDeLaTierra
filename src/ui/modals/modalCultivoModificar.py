from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from dominio.cultivo import Cultivo
from negocio.cultivoNegocio import CultivoNegocio
import discord

class ModalCultivoModificar(discord.ui.Modal):
    
    def __init__(self, cultivo:Cultivo):
        super().__init__(title=f"Modificar: {cultivo.getNombre()}")
        self.cultivo = cultivo
        
        self.input_estacion = discord.ui.TextInput(
            label="Estacion (numero)",
            default= str(cultivo.getEstacion()),
            placeholder="0 Primavera, 1 Verano, 2 Otoño.",
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
        if estacion < 0 or estacion > 2:
            await interaction.response.send_message("Debe ingresar valores numéricos entre 0 a 2.", ephemeral=True)
            return

        cultivo = Cultivo(self.cultivo.getID(), self.cultivo.getNombre(), estacion)
        
        negocio = CultivoNegocio()
        negocio.modificar(cultivo)

        await interaction.response.send_message("¡Modificacion realizada exitosamente!", ephemeral=True)
