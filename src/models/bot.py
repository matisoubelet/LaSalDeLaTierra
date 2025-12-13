import discord
from discord.ext import commands, tasks #Para los slash commands
from discord import app_commands #Para los slash commands
import logging
from dotenv import load_dotenv
import os
import sys

class Bot(commands.Bot):
    
    def __init__(self):
        load_dotenv()
        token = os.getenv('DISCORD_TOKEN')

        if token is None:
            print("ERROR: La variable DISCORD_TOKEN no está definida.")
            sys.exit(1)

        self.token: str = token

        self.handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(command_prefix='.', intents=intents)
    

    async def on_ready(self):
        print(f"{self.user} está activo!")

    #Carga en el bot los cogs de texto que tengamos
    async def setup_hook(self):
        from cogs.cogsTexto import CogsTexto
        await self.add_cog(CogsTexto(self))  
        
        try:
            await self.tree.sync()
            print(f"Se han cargado con exito los comandos.")
        except Exception as error:
            print("Ocurrio un error intentando cargar los comandos: ", error)
