import discord
from dominio.animal import Animal
from negocio.animalNegocio import AnimalNegocio


class ViewAnimalEliminar(discord.ui.View):

    def __init__(self, animal: Animal, timeout: int = 60):
        super().__init__(timeout=timeout)
        self.animal = animal

    def crear_embed(self) -> discord.Embed:
        embed = discord.Embed(
            title="Confirmar eliminación",
            description="Estás a punto de eliminar el siguiente animal:",
            color=discord.Color.red()
        )

        if self.animal.getDomestico():

            embed.add_field(
                name=f"{self.animal.getNombre().upper()}\n" + "‾" * (len(self.animal.getNombre()) + 3),
                value= "Domesticado",
                inline=False
            )

        else:

            embed.add_field(
                name=f"{self.animal.getNombre().upper()}\n" + "‾" * (len(self.animal.getNombre()) + 3),
                value= "No domesticado",
                inline=False
            )

        embed.add_field(
                name="Grupo",
                value= str(self.animal.getGrupo()),
                inline=False
            )

        return embed


    @discord.ui.button(label="❌ Cancelar", style=discord.ButtonStyle.secondary)
    async def cancelar(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            content="Eliminación cancelada.",
            embed=None,
            view=None
        )

    @discord.ui.button(label="🗑️ Eliminar", style=discord.ButtonStyle.danger)
    async def eliminar(self, interaction: discord.Interaction, button: discord.ui.Button):
        
        animalNegocio = AnimalNegocio()
        resultado = animalNegocio.eliminar(self.animal.getNombre())

        if resultado == -1:
            await interaction.response.edit_message(content="Hubo un error al intentar eliminar.", embed=None, view=None)
            return
        
        await interaction.response.edit_message(content="Animal eliminado exitosamente!.", embed=None, view=None)