from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from negocio.accionesDeCiudadNegocio import AccionesDeCiudadNegocio
import discord

class ModalAccionesDeCiudadAgregar(discord.ui.Modal):
    
    def __init__(self, nombre):
        super().__init__(title=f"Agregar: {nombre}")
        self.nombre = nombre


        self.input_descripcion = discord.ui.TextInput(
            label="Descripción",
            style=discord.TextStyle.paragraph,
            placeholder="Descripción de la accion",
            max_length=500
        )
        self.add_item(self.input_descripcion)


        self.input_requisito = discord.ui.TextInput(
            label="Requisito",
            placeholder="Requisito de la accion.",
            max_length=500
        )
        self.add_item(self.input_requisito)


        self.input_efecto = discord.ui.TextInput(
            label="Efecto (numero)",
            placeholder="Cantidad (usar 0 si no aplica)"
        )
        self.add_item(self.input_efecto)

      
        self.input_costos = discord.ui.TextInput(
            label="Costos (industria,poblacion,riqueza)",
            placeholder="Ej: 5,2,4"
        )
        self.add_item(self.input_costos)



    async def on_submit(self, interaction: discord.Interaction):

        #Verificamos que todos los campos tengan algun valor valido
        if (
            not self.input_descripcion.value.strip()
            or not self.input_requisito.value.strip()
            or not self.input_efecto.value.strip()
            or not self.input_costos.value.strip()
        ):
            await interaction.response.send_message("Debe completar todos los campos.", ephemeral=True)
            return
        
        #Validamos que todos los valores sean numericos
        try:
            efecto = int(self.input_efecto.value)
            industria, poblacion, riqueza = map(int,self.input_costos.value.split(",")) #Guarda en cada variable un numero, separando por la ","
        except ValueError:
            await interaction.response.send_message("Costos inválidos. Use el formato: industria,poblacion,riqueza", ephemeral=True)
            return

        #Validamos que los numeros no sean negativos
        if efecto < 0 or industria < 0 or poblacion < 0 or riqueza < 0:
            await interaction.response.send_message("Debe ingresar valores numéricos mayor o iguales a 0.", ephemeral=True)
            return
        
        negocio = AccionesDeCiudadNegocio()
        agrego = negocio.agregar(self.nombre, self.input_requisito.value, self.input_descripcion.value, efecto, industria, poblacion, riqueza)

        if(agrego == -1):
            await interaction.response.send_message("Hubo un error al intentar agregar la accion.", ephemeral=True)
        elif(agrego):
            await interaction.response.send_message("Accion agregada exitosamente!", ephemeral=True)
        else:
            await interaction.response.send_message("Accion existente, intente con otro nombre.", ephemeral=True)