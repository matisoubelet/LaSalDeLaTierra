from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from dominio.accionesDeUnidad import AccionesDeUnidad
from negocio.accionesDeUnidadNegocio import AccionesDeUnidadNegocio
import discord

class ModalAccionesDeUnidadModificar(discord.ui.Modal):
    
    def __init__(self, accion:AccionesDeUnidad):
        super().__init__(title=f"Modificar: {accion.getNombre()}")
        self.accion = accion
        
        
        self.input_descripcion = discord.ui.TextInput(
            label="Descripción",
            style=discord.TextStyle.paragraph,
            default=(accion.getDescripcion()),
            placeholder="Descripción de la accion",
            max_length=500
        )
        self.add_item(self.input_descripcion)


        self.input_tipo = discord.ui.TextInput(
            label="Tipo (Numero)",
            default=(accion.getTipo()),
            placeholder="0 Militar, 1 Caravana, 2 Explorador, 3 Cualquiera"
        )
        self.add_item(self.input_tipo)

      
        self.input_industria = discord.ui.TextInput(
            label="Industria (Numero)",
            default=(accion.getIndustria()),
            placeholder="Costo de industria"
        )
        self.add_item(self.input_industria)


        self.input_riqueza = discord.ui.TextInput(
            label="Riqueza (Numero)",
            default=(accion.getRiqueza()),
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

        accion = AccionesDeUnidad(self.accion.getId(), self.accion.getNombre(),self.input_tipo.value, self.input_descripcion.value, industria, riqueza)
        
        negocio = AccionesDeUnidadNegocio()
        negocio.modificar(accion)

        await interaction.response.send_message("¡Modificacion realizada exitosamente!", ephemeral=True)
