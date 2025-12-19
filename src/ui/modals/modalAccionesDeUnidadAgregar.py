from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from negocio.accionesDeUnidadNegocio import AccionesDeUnidadNegocio
import discord

class ModalAccionesDeUnidadAgregar(discord.ui.Modal):
    
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


        self.input_tipo = discord.ui.TextInput(
            label="Tipo (Numero)",
            placeholder="0 Militar, 1 Caravana, 2 Explorador, 3 Cualquiera"
        )
        self.add_item(self.input_tipo)

      
        self.input_industria = discord.ui.TextInput(
            label="Industria (Numero)",
            placeholder="Costo de industria"
        )
        self.add_item(self.input_industria)


        self.input_riqueza = discord.ui.TextInput(
            label="Riqueza (Numero)",
            placeholder="Costo de riqueza"
        )
        self.add_item(self.input_riqueza)


    async def on_submit(self, interaction: discord.Interaction):

        #Verificamos que todos los campos tengan algun valor valido
        if (
            not self.input_descripcion.value.strip()
            or not self.input_tipo.value.strip()
            or not self.input_industria.value.strip()
            or not self.input_riqueza.value.strip()
        ):
            await interaction.response.send_message("Debe completar todos los campos.", ephemeral=True)
            return
        
        #Validamos que todos los valores sean numericos
        try:
            tipo = int(self.input_tipo.value)
            industria = int(self.input_industria.value)
            riqueza = int(self.input_riqueza.value)
            
        except ValueError:
            await interaction.response.send_message("No se ingreso un valor numerico en tipo, industria o riqueza.", ephemeral=True)
            return

        #Validamos que los numeros no sean negativos
        if tipo < 0 or industria < 0 or riqueza < 0:
            await interaction.response.send_message("Debe ingresar valores numéricos mayor o iguales a 0.", ephemeral=True)
            return
        
        negocio = AccionesDeUnidadNegocio()
        agrego = negocio.agregar(self.nombre, self.input_tipo.value, self.input_descripcion.value, industria, riqueza)

        if(agrego == -1):
            await interaction.response.send_message("Hubo un error al intentar agregar la accion.", ephemeral=True)
        elif(agrego):
            await interaction.response.send_message("Accion agregada exitosamente!", ephemeral=True)
        else:
            await interaction.response.send_message("Accion existente, intente con otro nombre.", ephemeral=True)