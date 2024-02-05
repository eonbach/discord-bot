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
 #if ctx.author.id == 751688827373879404:
    await ctx.reply(f'Команда {text} по вашему запросу созданна!') # Отправление сообщения при использовании команды
    category = await ctx.guild.create_category(f'Группа {text}') # создание категории по запросу

    # Каналы в этой категории:
    news = await category.create_text_channel(f'Новости') 
    await category.create_text_channel(f'чат')
    await category.create_text_channel(f'ресуры')
    # Войс каналы:
    await category.create_voice_channel(f'кодинг')
    await category.create_voice_channel(f'приятные беседы')
    
    guild = ctx.guild # сервер на котором находится пользователь
    nrole = await guild.create_role(name=f"{text}") # создание роли
    await ctx.author.add_roles(nrole) # выдача роли пользователю который юзнул команду

    nroleFORpeople = await guild.create_role(name=f"Участник: {text}") # создание роли
 
    
    
    permCategory = discord.PermissionOverwrite( # права @everyone
      read_messages=False  # запретить читать сообщения
    )
    await category.set_permissions(guild.default_role, overwrite=permCategory) # задать права категории


    permNews = discord.PermissionOverwrite( # ПРАВА КАНАЛА НОВОСТИ
     send_messages=False  # запретить отправлять сообщения
    )
    await news.add_permissions(permNews) # задать каналу новости в категории



    # Доступ к категории специально
    permissionsCAT = discord.PermissionOverwrite(
     read_messages = True
    )
    await category.set_permissions(nroleFORpeople, overwrite=permissionsCAT)


    user = guild.get_member(ctx.author.id)
    if user:
        permUser = discord.PermissionOverwrite( # доступ юзеру
          read_messages=True,
          send_messages=True
         )
        await category.set_permissions(user, overwrite=permUser)
       # pass 


@bot.command()
async def deleteDSJ(ctx): # удаляет категорию с каналами
 for channel in ctx.channel.category.channels: 
  await channel.delete() 
 await category.delete()

@bot.event # ивент ошибок
async def on_command_error(ctx,error):
     await ctx.send(f'```{error}```')

bot.run(TOKEN)
