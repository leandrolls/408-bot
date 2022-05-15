import requests
from discord.ext import commands
import discord
from translate import Translator

class Talks(commands.Cog):
    """ TALKS WITH USER """

    def __init__(self,bot):
        self.bot = bot

    @commands.command(name='ajuda', help="O Bot mostra todos os comandos")
    async def ajuda(self, ctx):
        embed_image = discord.Embed(title="PRECISANDO DE AJUDA? ", color=0xFFFFFF)
        embed_image.add_field(name="COMANDOS:", value="""
        +ajuda = Para exibir essa mensagem com os comandos e sua funções.
        +oi = Para o bot te cumprimentar.
        +regras = Para exibir as regras do servidor 408.
        +calcular = Para poder fazer operações matemáticas.
        +foto = Para gerar uma foto aleatória para você.
        +segredo = Para o bot lhe conta um segredo na DM.
        +conselho = Para ler um conselho.
        +kanye = Quer saber o Kanye West diria nessa situação? Esse é o comando.
        +norris = Para ler uma curiosidade sobre Chuck Norris.
        +fatos = Para ler uma curiosidade aleatoria sobre algo.
        +tedio = Para a resolução do seu tedio.
        """, inline=False)
        await ctx.send(embed=embed_image)

    @commands.command(name='oi', help="O Bot te cumprimenta")
    async def send_hello(self, ctx):
        embed_image = discord.Embed(title="BOT408", color=0xFFFFFF)
        embed_image.add_field(name=f"Olá!", value="Como você está? ", inline=False)
        await ctx.send(embed=embed_image)

    @commands.command(name="segredo", help="O Bot lhe conta um segredo")
    async def secret(ctx):
        try:
            await ctx.author.send("""É um segredo, não conte pra ninguem
            PALMEIRAS NAO TEM MUNDIAL!""")

        except discord.errors.Forbidden:
            await ctx.send(
                f"{ctx.author.name}, infelizmente não posso te conta o segredo :( \nHabilite receber mensagens de qualquer pessoa do servidor (Opções > Privacidade e Segurança)")

    @commands.command(name="regras", help="O Bot exibe as regras do servidor")
    async def rules(self, ctx):
        embed_image = discord.Embed(title="BOT408", color=0xFFFFFF)
        embed_image.add_field(name="Sobre as regras:", value=f"Você pode conferir as regras do servidor em: <#831679986272305182>", inline=False)
        await ctx.send(embed=embed_image)

    @commands.command(name="convite1", help="O bot lhe responde com um convite")
    async def invite(self, ctx):
        embed_image = discord.Embed(title="BOT408", color=0xFFFFFF)
        embed_image.add_field(name="Sobre convite:",
                              value=f"Você pode pegar um convite para este server em:  <#831675218573393920>", inline=False)
        await ctx.send(embed=embed_image)

    @commands.command(name="conselho", help="O bot lhe retorna um conselho aleatorio")
    async def advice(self, ctx):
        response = requests.get("https://api.adviceslip.com/advice")
        advice_json = response.json()
        advice = advice_json['slip']['advice']

        translator = Translator(to_lang="pt")
        advice_pt = translator.translate(advice)

        embed_image = discord.Embed(title="VAI UM CONSELHO AI?", color=0xFFFFFF)
        embed_image.add_field(name="Aqui vai um conselho:",
                              value=f"{advice_pt}",
                              inline=False)
        await ctx.send(embed=embed_image)


    @commands.command(name="kanye", help="O que o Kanye West faria em uma situação dessa ?")
    async def kanye(self, ctx):
        response = requests.get("https://api.kanye.rest/")
        kanye_json = response.json()
        kanye_words = kanye_json['quote']

        translator = Translator(to_lang="pt")
        kanye_pt = translator.translate(kanye_words)

        embed_image = discord.Embed(title="E O KANEY WEST HEIN ?", color=0xFFFFFF)
        embed_image.add_field(name="Isso é o que o Kanye West falaria:",
                              value=f"{kanye_pt}",
                              inline=False)
        await ctx.send(embed=embed_image)

#     @commands.command(name="cargom")
#     async def message_cargo(self, ctx):
#         await ctx.send("""
# Quer ganhar cargos aqui dentro ?
#
# No nosso servidor temos cargos que liberam canais específicos para o seu cargo.
#
# Joga algum jogo ? Reaja com o emoji referente ao jogo e libere os canais (texto e voz) específicos desse jogo.
#
# :city_dusk: - Sim City
# :desert: - Minecraft
# :red_car: - Rocket League
# :soccer: - FIFA
# :ox: - League Of Legends
# :knife: - Among Us
# :bulb: - Gartic
# :bomb: - Counter Strike
# :raccoon: - Pokémon
# :jigsaw: - Outros
#
#         """)

    @commands.command(name='norris', help="Piadas do ChuckNorris")
    async def norris(self, ctx):
        response = requests.get("https://api.chucknorris.io/jokes/random")
        norris_json = response.json()
        norris_words = norris_json['value']

        translator = Translator(to_lang="pt")
        norris_pt = translator.translate(norris_words)

        embed_image = discord.Embed(title="VAI UMA PIADA DO CHUCK AI? ", color=0xFFFFFF)
        embed_image.add_field(name="Toma uma piadinha:",
                              value=f"{norris_pt}",
                              inline=False)
        await ctx.send(embed=embed_image)

    @commands.command(name='fatos', help="Quer descobrir uma curiosidade aleatoria ?")
    async def facts(self, ctx):
        response = requests.get("https://asli-fun-fact-api.herokuapp.com/")
        facts_json = response.json()
        facts = facts_json['data']['fact']

        translator = Translator(to_lang="pt")
        facts_pt = translator.translate(facts)

        embed_image = discord.Embed(title="QUER UMA CURIOSIDADE ALEATORIA ?", color=0xFFFFFF)
        embed_image.add_field(name="Então toma:",
                              value=f"{facts_pt}",
                              inline=False)
        await ctx.send(embed=embed_image)


    @commands.command(name="tedio", help="Está entendiado ?")
    async def bored(self,ctx):
        response = requests.get("https://www.boredapi.com/api/activity/")
        bored_json = response.json()
        bored_activity = bored_json['activity']

        translator = Translator(to_lang="pt")
        bored_activity_pt = translator.translate(bored_activity)

        embed_image = discord.Embed(title="ESTÁ ENTEDIDADO ?", color=0xFFFFFF)
        embed_image.add_field(name="Aqui vai uma recomenadação: ",
                              value=f"{bored_activity_pt}",
                              inline=False)
        await ctx.send(embed=embed_image)

def setup(bot):
    bot.add_cog(Talks(bot))