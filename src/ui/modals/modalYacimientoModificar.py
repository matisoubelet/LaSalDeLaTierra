from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from negocio.yacimientoNegocio import YacimientoNegocio
from dominio.yacimiento import Yacimiento
import discord

class ModalYacimientoModificar(discord.ui.Modal):
    
    def __init__(self, yacimiento: Yacimiento):
        super().__init__(title=f"Modificar: {yacimiento.getNombre()}")
        self.yacimiento = yacimiento


        self.input_tipo = discord.ui.TextInput(
            label="Tipo (numero)",
            default=str(yacimiento.getTipo()),
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

        yacimiento = Yacimiento(self.yacimiento.getID(), self.yacimiento.getNombre(), tipo)

        negocio = YacimientoNegocio()
        negocio.modificar(yacimiento)

        await interaction.response.send_message("¡Modificacion realizada exitosamente!", ephemeral=True)