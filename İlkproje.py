import discord
from discord.ext import commands

intents = discord.Intents.default()
intents=discord.Intents.all()
intents.typing = False
intents.presences = False
 
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot olarak giriş yapıldı: {bot.user.name}')

@bot.event
async def on_member_join(member):
    print(f'{member.name} sunucuya katıldı. Kullanıcı ID: {member.id}')

bot.run('T')
