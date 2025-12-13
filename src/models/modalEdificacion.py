from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
from models.edificacion import Edificacion
from negocio.edificacionNegocio import EdificacionNegocio
import discord

class ModalEdificacion(discord.ui.Modal):
    
    def __init__(self, edificacion:Edificacion):
        super().__init__(title=f"Modificar: {edificacion.getNombre()}")
        self.edificacion = edificacion
        
        self.input_descripcion = discord.ui.TextInput(
            label="Descripción",
            default=str(edificacion.getDescripcion()),
            style=discord.TextStyle.paragraph,
            placeholder="Descripción de la edificación",
            max_length=500,
            required=False
        )
        self.add_item(self.input_descripcion)

       
        self.input_efecto = discord.ui.TextInput(
            label="Efecto (numero)",
            default=str(edificacion.getEfecto()),
            placeholder="Cantidad (usar 0 si no aplica)",
            required=False
        )
        self.add_item(self.input_efecto)

      
        self.input_industria = discord.ui.TextInput(
            label="Costo de industria (numero)",
            default=str(edificacion.getIndustria()),
            placeholder="Cantidad (usar 0 si no aplica)",
            required=False
        )
        self.add_item(self.input_industria)

       
        self.input_riqueza = discord.ui.TextInput(
            label="Costo de riqueza (numero)",
            default=str(edificacion.getRiqueza()),
            placeholder="Cantidad (usar 0 si no aplica)",
            required=False
        )
        self.add_item(self.input_riqueza)

      
        self.input_riqXturno = discord.ui.TextInput(
            label="Genera riqueza por turno (S/N)",
            default=("S" if edificacion.getRiqXturno() else "N"),
            placeholder="S o N",
            required=False
        )
        self.add_item(self.input_riqXturno)

    async def on_submit(self, interaction: discord.Interaction):

        #Verificamos que todos los campos tengan algun valor valido
        if (
            not self.input_descripcion.value.strip()
            or not self.input_efecto.value.strip()
            or not self.input_industria.value.strip()
            or not self.input_riqueza.value.strip()
            or not self.input_riqXturno.value.strip()
        ):
            await interaction.response.send_message("Debe completar todos los campos.", ephemeral=True)
            return

        #Verifica que el valor sea una S o una N
        if self.input_riqXturno.value.strip().upper() == "S" or self.input_riqXturno.value.strip().upper() == "N": 
            #Transforma a True o False segun lo que se haya tipeado
            riqXturno = self.input_riqXturno.value.strip().upper() == "S" 
        else:
            await interaction.response.send_message("El valor en 'Riqueza por turno' no es valido", ephemeral=True)
            return
        
        try: #Validamos que todos los valores numericos sean correctos
            efecto = int(self.input_efecto.value)
            industria = int(self.input_industria.value)
            riqueza = int(self.input_riqueza.value)
        except ValueError:
            await interaction.response.send_message("No se ingreso un valor numerico en efecto, industria o riqueza.", ephemeral=True)
            return

        #Validamos que los numeros no sean negativos
        if efecto < 0 or industria < 0 or riqueza < 0:
            await interaction.response.send_message("Debe ingresar valores numéricos mayor o iguales a 0.", ephemeral=True)
            return


        edificacion = Edificacion(self.edificacion.getID(), self.edificacion.getNombre(), self.input_descripcion.value, efecto, industria, riqueza, riqXturno)
        
        negocio = EdificacionNegocio()
        negocio.modificar(edificacion)

        await interaction.response.send_message("¡Modificacion realizada exitosamente!", ephemeral=True)
