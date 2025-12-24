from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from negocio.bosqueNegocio import BosqueNegocio
from dominio.bosque import Bosque
import discord

class ModalBosqueModificar(discord.ui.Modal):
    
    def __init__(self, bosque:Bosque):
        super().__init__(title=f"Modificar: {bosque.getNombre()}")
        self.bosque = bosque


        self.input_grupo = discord.ui.TextInput(
            label="Grupo (numero)",
            default = str(self.bosque.getGrupo()),
            placeholder="Numero entre 0 a 3.",
        )
        self.add_item(self.input_grupo)


    async def on_submit(self, interaction: discord.Interaction):

        #Verificamos que todos los campos tengan algun valor valido
        if (not self.input_grupo.value.strip()):

            await interaction.response.send_message("Debe completar el campo.", ephemeral=True)
            return
        
        #Validamos que el valor sea numerico
        try:
            grupo = int(self.input_grupo.value)
            
        except ValueError:
            await interaction.response.send_message("No se ingreso un valor numerico.", ephemeral=True)
            return

        #Validamos el numero este dentro del rango
        if grupo < 0 or grupo > 3:
            await interaction.response.send_message("Debe ingresar valores numéricos entre 0 a 3.", ephemeral=True)
            return

        bosque = Bosque(self.bosque.getID(), self.bosque.getNombre(), grupo)
        
        negocio = BosqueNegocio()
        negocio.modificar(bosque)

        await interaction.response.send_message("¡Modificacion realizada exitosamente!", ephemeral=True)