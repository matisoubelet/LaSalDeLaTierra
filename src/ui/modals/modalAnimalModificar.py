from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from negocio.animalNegocio import AnimalNegocio
from dominio.animal import Animal
import discord

class ModalAnimalModificar(discord.ui.Modal):
    
    def __init__(self, animal:Animal):
        super().__init__(title=f"Modificar: {animal.getNombre()}")
        self.animal = animal

        self.input_domestico = discord.ui.TextInput(
            label="Domestico (S/N)",
            default=("S" if animal.getDomestico() else "N"),
            placeholder="S o N"
        )
        self.add_item(self.input_domestico)


        self.input_grupo = discord.ui.TextInput(
            label="Grupo (numero)",
            default = str(animal.getGrupo()),
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
        
        animal = Animal(self.animal.getID(), self.animal.getNombre(), domestico, grupo)

        negocio = AnimalNegocio()
        negocio.modificar(animal)

        await interaction.response.send_message("¡Modificacion realizada exitosamente!", ephemeral=True)