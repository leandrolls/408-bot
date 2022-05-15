import discord
from discord.ext import commands
import requests

class Pokemon(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="pokedex", help="Esse comando lhe retorna informações sobre o pokemon pesquisado")
    async def pokemon(self, ctx, namepoke):

        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{namepoke}")
            data = response.json()

            if data:
                idpoke = data['id']
                idspecie = data['species']['url']
                habilidades = []
                movimentos = []
                tipos = []
                evolution_chain = []
                no_damage_to = []
                half_damage_to = []
                double_damage_to = []
                half_damage_from = []
                no_damage_from = []
                double_damage_from = []
                i = 0
                j = 0

                responseevo = requests.get(f"{idspecie}")
                dataevo = responseevo.json()
                cadeiaevo = dataevo['evolution_chain']['url']
                response_cadeia = requests.get(f"{cadeiaevo}")
                json_example = response_cadeia.json()

                evolution_chain.append(json_example['chain']['species']['name'].capitalize())
                while i < len(json_example['chain']['evolves_to']):
                    evolution_chain.append(json_example['chain']['evolves_to'][i]['species']['name'].capitalize())

                    while j < len(json_example['chain']['evolves_to'][i]['evolves_to']):
                        evolution_chain.append(json_example['chain']['evolves_to'][i]['evolves_to'][j]['species']['name'].capitalize())
                        j += 1

                    i += 1

                for i in data['types']:
                    addt = i['type']['name'].capitalize()
                    tipos.append(addt)
                name = tipos[0]

                response_type = requests.get(f"https://pokeapi.co/api/v2/type/{name.lower()}/")
                json_types = response_type.json()


                for i in json_types['damage_relations']['no_damage_to']:
                    nomes_no_damage_to = i['name'].capitalize()
                    no_damage_to.append(nomes_no_damage_to)
                if no_damage_to == []:
                    no_damage_to = ['N/A']

                for i in json_types['damage_relations']['half_damage_to']:
                    nomes_half_damage_to = i['name'].capitalize()
                    half_damage_to.append(nomes_half_damage_to)
                if half_damage_to == []:
                    half_damage_to = ['N/A']

                for i in json_types['damage_relations']['double_damage_to']:
                    nomes_double_damage_to = i['name'].capitalize()
                    double_damage_to.append(nomes_double_damage_to)
                if double_damage_to == []:
                    double_damage_to = ['N/A']

                for i in json_types['damage_relations']['no_damage_from']:
                    nomes_no_damage_from = i['name'].capitalize()
                    no_damage_from.append(nomes_no_damage_from)
                if no_damage_from == []:
                    no_damage_from = ['N/A']

                for i in json_types['damage_relations']['half_damage_from']:
                    nomes_half_damage_from = i['name'].capitalize()
                    half_damage_from.append(nomes_half_damage_from)
                if half_damage_from == []:
                    half_damage_from = ['N/A']

                for i in json_types['damage_relations']['double_damage_from']:
                    nomes_double_damage_from = i['name'].capitalize()
                    double_damage_from.append(nomes_double_damage_from)
                if double_damage_from == []:
                    double_damage_from = ['N/A']

                for i in data['abilities']:
                    addh = i['ability']['name'].capitalize()
                    habilidades.append(addh)

                for p in data['moves']:
                    add = p['move']['name']
                    movimentos.append(add)

                embed_image = discord.Embed(title=f"{namepoke.upper()}",color=0xFFFFFF)
                embed_image.set_image(url=f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{idpoke}.png")
                embed_image.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
                embed_image.set_footer(text="Criado por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)
                embed_image.add_field(name="Tipo", value= ', '.join(tipos))
                embed_image.add_field(name="Cadeia de evolução", value= ', '.join(evolution_chain), inline=True)
                embed_image.add_field(name="Habilidades", value= ', '.join(habilidades), inline=False)

                for i in data['stats']:
                    estatisticas_name = i['stat']['name'].capitalize()
                    estatisticadado = i['base_stat']
                    embed_image.add_field(name=f"{estatisticas_name}", value=f"{estatisticadado}", inline=True)

                embed_image.add_field(name="Receberá Dobro De Dano de:", value= ', '.join(double_damage_from), inline=True)
                embed_image.add_field(name="Receberá Sem Dano de:", value=', '.join(no_damage_from), inline=True)
                embed_image.add_field(name="Receberá Metade Do Dano de:", value=', '.join(half_damage_from), inline=True)
                embed_image.add_field(name="Dará Dobro de Dano para:", value= ', '.join(double_damage_to), inline=True)
                embed_image.add_field(name="Dará Sem Dano para:", value=', '.join(no_damage_to), inline=True)
                embed_image.add_field(name="Dará Metade de Dado para:", value=', '.join(half_damage_to), inline=True)
                embed_image.add_field(name="Movimentos", value= ', '.join(movimentos), inline=False)

                await ctx.send(embed=embed_image)

            else:
                await ctx.send(f"Inválido. Escreva !ajuda para exibir os comandos")

        except:
            await ctx.send("Não encontramos esse Pokémon \nTem certeza que escreveu o nome certo do Pokémon ?")


def setup(bot):
    bot.add_cog(Pokemon(bot))
