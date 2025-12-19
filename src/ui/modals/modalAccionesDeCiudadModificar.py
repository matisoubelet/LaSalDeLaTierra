from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from dominio.accionesDeCiudad import AccionesDeCiudad
from negocio.accionesDeCiudadNegocio import AccionesDeCiudadNegocio
import discord

class ModalAccionesDeCiudadModificar(discord.ui.Modal):
    
    def __init__(self, accion:AccionesDeCiudad):
        super().__init__(title=f"Modificar: {accion.getNombre()}")
        self.accion = accion
        
        self.input_descripcion = discord.ui.TextInput(
            label="Descripción",
            default=str(accion.getDescripcion()),
            style=discord.TextStyle.paragraph,
            placeholder="Descripción de la accion",
            max_length=500
        )
        self.add_item(self.input_descripcion)


        self.input_requisito = discord.ui.TextInput(
            label="Requisito",
            default=str(accion.getRequisito()),
            placeholder="Requisito de la accion.",
            max_length=500
        )
        self.add_item(self.input_requisito)


        self.input_efecto = discord.ui.TextInput(
            label="Efecto (numero)",
            default=str(accion.getEfecto()),
            placeholder="Cantidad (usar 0 si no aplica)"
        )
        self.add_item(self.input_efecto)

      
        self.input_costos = discord.ui.TextInput(
            label="Costos (industria,poblacion,riqueza)",
            default=f"{accion.getIndustria()},{accion.getPoblacion()},{accion.getRiqueza()}",
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

        accion = AccionesDeCiudad(self.accion.getId(), self.accion.getNombre(),self.input_requisito.value, self.input_descripcion.value, efecto, industria, poblacion, riqueza)
        
        negocio = AccionesDeCiudadNegocio()
        negocio.modificar(accion)

        await interaction.response.send_message("¡Modificacion realizada exitosamente!", ephemeral=True)
