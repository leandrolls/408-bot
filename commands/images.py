from discord.ext import commands
import discord


class Images(commands.Cog):
    """ WORK WITH IMAGES """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="foto", help="O Bot retorna uma foto aleatória")
    async def get_random_image(self,ctx):
        url_image = "https://picsum.photos/200/300"
        embed_image = discord.Embed(
            title="Resultado",
            description="Foto aleatória",
            color=0xFFFFFF,
        )

        embed_image.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        embed_image.set_footer(text="Criado por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed_image.add_field(name="Teste", value="Teste de Embed")
        embed_image.add_field(name="Resolução da foto", value="200x300")
        embed_image.add_field(name="Exemplo Non Inline", value=url_image, inline=False)
        embed_image.set_image(url=url_image)

        await ctx.send(embed=embed_image)


def setup(bot):
    bot.add_cog(Images(bot))