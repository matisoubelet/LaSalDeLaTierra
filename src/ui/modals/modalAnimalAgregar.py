from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from negocio.animalNegocio import AnimalNegocio
import discord

class ModalAnimalAgregar(discord.ui.Modal):
    
    def __init__(self, nombre):
        super().__init__(title=f"Agregar: {nombre}")
        self.nombre = nombre


        self.input_domestico = discord.ui.TextInput(
            label="Domestico (S/N)",
            placeholder="S o N"
        )
        self.add_item(self.input_domestico)


        self.input_grupo = discord.ui.TextInput(
            label="Grupo (numero)",
            placeholder="Numero entre 0 a 3.",
        )
        self.add_item(self.input_grupo)


    async def on_submit(self, interaction: discord.Interaction):

        #Verificamos que todos los campos tengan algun valor valido
        if (not self.input_domestico.value.strip()
            or not self.input_grupo.value.strip()
            ):

            await interaction.response.send_message("Debe todos los campos.", ephemeral=True)
            return
        
        #Verifica que el valor sea una S o una N
        if self.input_domestico.value.strip().upper() == "S" or self.input_domestico.value.strip().upper() == "N": 
            #Transforma a True o False segun lo que se haya tipeado
            domestico = self.input_domestico.value.strip().upper() == "S" 
        else:
            await interaction.response.send_message("El valor en 'Domestico' no es valido", ephemeral=True)
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

        negocio = AnimalNegocio()
        agrego = negocio.agregar(self.nombre, domestico, grupo)

        if(agrego == -1):
            await interaction.response.send_message("Hubo un error al intentar agregar el animal.", ephemeral=True)
        elif(agrego):
            await interaction.response.send_message("Animal agregado exitosamente!", ephemeral=True)
        else:
            await interaction.response.send_message("Animal existente, intente con otro nombre.", ephemeral=True)