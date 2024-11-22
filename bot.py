import discord
import random
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

cleanlist = [
    "Kağıt: 2 ila 6 hafta. Gazete veya kağıt mendil gibi ince kağıtlar daha hızlı, karton gibi daha kalın kağıtlar daha yavaş ayrışır.",
    "Pamuklu kumaş: 1 ila 5 ay. Doğal malzeme olduğu için pamuklu kumaşlar hızlıca ayrışır. Sentetik karışımlar ise çok daha uzun sürer.",
    "Ahşap: 1 ila 3 yılİşlenmemiş, doğal ahşap daha hızlı ayrışır. Vernikli veya boyalı ahşap çok daha uzun süre dayanabilir.",
    "Sigara izmariti: 1 ila 5 yıl. İçindeki plastik ve kimyasallar nedeniyle oldukça uzun sürede ayrışır. Çevreye zararlıdır.",
    "Plastik poşet: 400 ila 1.000 yıl. Güneş ışığına maruz kaldığında daha hızlı parçalanır ancak mikroplastik olarak çevrede kalır.",
    "Alüminyum kutu: 200 ila 500 yıl. Geri dönüştürülebilir ancak doğaya bırakıldığında çok uzun süre bozulmadan kalır.",
    "Cam şişe: 1 milyon yıl veya daha fazla. Doğada neredeyse hiç bozulmaz. Ancak geri dönüştürülebilir ve sonsuz kez kullanılabilir.",
    "Plastik şişe: 450 yıl veya daha fazla. Yavaş yavaş mikroplastiklere dönüşür ve tamamen kaybolmaz.",
    "Köpük (Strafor): 500 yıl veya daha fazla. Çok uzun süre doğada kalır ve küçük parçalara ayrılarak çevreye zarar verir.",
    "Konserve kutusu: 50 yıl. Paslanabilir ancak tamamen yok olması uzun sürer."
    ]

@bot.command()
async def funfacts(ctx):
    pull_from_list = random.choice(cleanlist)
    await ctx.send(pull_from_list)


bot.run("token")
