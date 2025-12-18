import discord
from discord.ext import commands
import logging
import os
import sys


class Bot(commands.Bot):

    def __init__(self):
        token = os.getenv("DISCORD_TOKEN")

        if not token:
            print("ERROR: La variable DISCORD_TOKEN no está definida.")
            sys.exit(1)

        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(
            command_prefix='.',
            intents=intents
        )

        self._token = token

    async def setup_hook(self):
        from cogs.cogs import Cogs
        await self.add_cog(Cogs(self))

        try:
            await self.tree.sync()
            print("Comandos sincronizados correctamente.")
        except Exception as error:
            print("Error al sincronizar comandos:", error)

    async def on_ready(self):
        print(f"{self.user} está activo!")