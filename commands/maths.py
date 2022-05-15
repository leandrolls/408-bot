from discord.ext import commands

class Maths(commands.Cog):
    """ WORKS WITH MATH"""

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="calcular", help="Calcula o valor de uma expressão")
    async def calculate_expression(self,ctx, *expression):
        expression = ''.join(expression)
        response = eval(expression)

        await ctx.send("A resposta é: " + str(response))

def setup(bot):
    bot.add_cog(Maths(bot))