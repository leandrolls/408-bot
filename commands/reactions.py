from discord import channel
from discord.ext import commands

class React(commands.Cog):
    """ REACTIONS  """

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self,reaction, user):

        chid = 938822019838009415
        if reaction.emoji == "🌆" :
            if reaction.message.channel.id == chid:
                role = user.guild.get_role(937210119874293770)
                await user.add_roles(role)
                print("CONCLUIDO COM SUCESSO")
            else:
                print("Comando nao realizado")

        elif reaction.emoji == "🏜":
            if reaction.message.channel.id == chid:
                role = user.guild.get_role(938823475219542096)
                await user.add_roles(role)

        elif reaction.emoji == "🚗":
            if reaction.message.channel.id == chid:
                role = user.guild.get_role(938823535214878782)
                await user.add_roles(role)

        elif reaction.emoji == "⚽":
            if reaction.message.channel.id == chid:
                role = user.guild.get_role(938823581473837117)
                await user.add_roles(role)

        elif reaction.emoji == "🐂":
            if reaction.message.channel.id == chid:
                role = user.guild.get_role(938823615699369994)
                await user.add_roles(role)

        elif reaction.emoji == "🔪":
            if reaction.message.channel.id == chid:
                role = user.guild.get_role(938824308015382539)
                await user.add_roles(role)

        elif reaction.emoji == "💡":
            if reaction.message.channel.id == chid:
                role = user.guild.get_role(938824390601236531)
                await user.add_roles(role)

        elif reaction.emoji == "💣":
            if reaction.message.channel.id == chid:
                role = user.guild.get_role(938824467273121883)
                await user.add_roles(role)

        elif reaction.emoji == "🧩":
            if reaction.message.channel.id == chid:
                role = user.guild.get_role(938824927853805599)
                await user.add_roles(role)

        elif reaction.emoji == "🦝":
            if reaction.message.channel.id == chid:
                role = user.guild.get_role(938824596403154955)
                await user.add_roles(role)


def setup(bot):
    bot.add_cog(React(bot))