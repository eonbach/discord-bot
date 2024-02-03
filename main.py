import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
from json import load


load_dotenv()
TOKEN = getenv("TOKEN")


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.reaction_role_message_id = 1202923966738726953
        self.emoji_to_role = {
            "🌐": "Веб-разработка",
            "📱": "Мобильная разработка",
            "🖥️": "Десктоп разработка",
            "🎮": "Разработка игр",
            "🗃️": "Базы данных",
            "🤖": "Анализ данных, МО",
            "🛠️": "Тестирование, DevOps",
            "🔒": "Кибербезопасность",
            "🔗": "Блокчейн",
            "🎨": "Дизайн, UI/UX",
            "🏗️": "Проектирование ПО"
        }


    async def on_ready(self):
        print(f'вход выполнен, {self.user}')


    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.message_id != self.reaction_role_message_id:
            return
        
        guild = self.get_guild(payload.guild_id)

        try:
            role_name = self.emoji_to_role[payload.emoji.name]
        except:
            return
        
        role = discord.utils.get(guild.roles, name=role_name)

        await payload.member.add_roles(role)

        print(f'{payload.member}: +{role_name}')
    

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if payload.message_id != self.reaction_role_message_id:
            return

        guild = self.get_guild(payload.guild_id)

        try:
            role_name = self.emoji_to_role[payload.emoji.name]
        except:
            return
        
        role = discord.utils.get(guild.roles, name=role_name)

        member = guild.get_member(payload.user_id)

        await member.remove_roles(role)

        print(f'{member}: -{role_name}')


intents = discord.Intents.all()
command_prefix = "."

bot = MyBot(intents=intents, command_prefix=command_prefix)

@bot.command() # основная структура команды
async def createDSJ(ctx,*,text): # функция и перемены, * отвечает за пробелы в text
 if ctx.author.id == 751688827373879404
    await ctx.reply(f'Команда {text} по вашему запросу созданна!') # Отправление сообщения при использовании команды
    channel = await ctx.guild.create_category(f'Группа {text}') # создание категории по запросу
    # Каналы в этой категории:
    news = await channel.create_text_channel(f'Новости') 
    await channel.create_text_channel(f'чат')
    await channel.create_text_channel(f'ресуры')
    # Войс каналы:
    await channel.create_voice_channel(f'кодинг')
    await channel.create_voice_channel(f'приятные беседы')
    
    guild = ctx.guild # сервер на котором находится пользователь
    nrole = await guild.create_role(name=f"{text}") # создание роли
    await ctx.author.add_roles(nrole) # выдача роли пользователю который юзнул команду
    
    everyone_role = guild.default_role # опознаёт @everyone 
    permissioEVE = discord.PermissionOverwrite( #запрещает @everyone смотреть
                read_messages=False,  # запретить читать сообщения
            )
    await channel.set_permissions(everyone_role, overwrite=permissioEVE) # задать права категории

    permissions = discord.PermissionOverwrite( #  права категории
      read_messages=True,
      send_messages=True
    )

    permissioEVE = discord.PermissionOverwrite( # ПРАВА КАНАЛА НОВОСТИ
       send_messages=False  # запретить отправлять сообщения
    )
    await news.set_permissions(everyone_role, overwrite=permissioEVE) # задать права категории


     user = guild.get_member(ctx.author.id)
     if user:
        await channel.set_permissions(user, overwrite=permissions)
      pass

bot.run(TOKEN)
