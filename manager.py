from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
from discord.ext import commands

class Manager(commands.Cog):
    """ MANEGING """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou pronto e usando o nome de {self.bot.user}')

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("Preencha todos os argumentos. Digite !help para exibir os argumentos dos comandos")
        elif isinstance(error, CommandNotFound):
            await ctx.send("Comando não encontrado. Digite !help para exibir os comandos")
        else:
            raise error

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if 'palavrao' in message.content:
            await message.channel.send(f'Não ofenda os usuários @{message.author.name}')
            await message.delete()


def setup(bot):
    bot.add_cog(Manager(bot))
