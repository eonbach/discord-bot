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
async def createDSJ(ctx, text): 
    ''' Создание группы >createDSJ *number* '''
    n = text
    guild = ctx.guild
    group_leader_role = await guild.create_role(name=f'Лидер № {n}')
    group_member_role = await guild.create_role(name=f'Группа № {n}')

    await ctx.author.add_roles(group_leader_role) 

    group_category_overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        group_leader_role: discord.PermissionOverwrite(read_messages=True, connect=True),
        group_member_role: discord.PermissionOverwrite(read_messages=True, connect=True)
    }

    category = await guild.create_category(f'Группа № {n}', overwrites=group_category_overwrites)

    locked_channel_overwrites = group_category_overwrites
    locked_channel_overwrites[group_member_role].update(send_messages=False)

    news = await category.create_text_channel('новости', overwrites=locked_channel_overwrites)
    await category.create_text_channel('ресурсы', overwrites=locked_channel_overwrites)
    await category.create_text_channel('чат')
    await category.create_voice_channel('кодинг')
    await category.create_voice_channel('общение')

    await ctx.reply(f'Группа {n}: созданна по вашему запросу') 

@bot.command()
async def deleteDSJ(ctx, text):
 ''' Удаление группы >deleteDSJ *number* '''
 n = text
 guild = ctx.guild
 category = get(guild.categories, name=f'Группа № {n}')
 for channel in category.channels:
   await channel.delete()
 await category.delete()
 await discord.utils.get(guild.roles, name=f'Лидер № {nt}').delete()
 await discord.utils.get(guild.roles, name=f'Участник № {n}').delete()
 await discord.utils.get(guild.roles, name=f'Группа № {n}').delete()

@bot.command()
async def addDSJ(ctx, text, member:discord.Member ):
 ''' Добавление участника в группу >addDSJ *number* *mention* '''
 n = text
 guild = ctx.guild
 group_leader_role = get(guild.roles, name=f'Лидер № {n}')
 group_member_role = get(guild.roles, name=f'Участник № {n}')
 
 if group_leader_role in ctx.author.roles:
     succes = await member.add_roles(group_member_role)
     if succes:
      await ctx.reply(f'Участник {member.mention} был добавлен в вашу группу:{n}!')
     else:
      await ctx.reply(f'Не удалось добавить участника в группу')
 else:
     await ctx.reply(f'Данной группы не существует или же вы не лидер группы')

@bot.command()
async def removeDSJ(ctx, text, member:discord.Member ):
 ''' Удаление участника из группы >removeDSJ *number* *mention* '''
 n = text
 guild = ctx.guild
 group_leader_role = get(guild.roles, name=f'Лидер № {n}')
 group_member_role = get(guild.roles, name=f'Участник № {n}')
 
 if group_leader_role in ctx.author.roles:
     succes = await member.remove_roles(group_member_role)
     if succes:
      await ctx.reply(f'Участник {member.mention} был удалён из вашей группы:{n}!')
     else:
      await ctx.reply(f'Не удалось удалить участника из группы')
 else:
     await ctx.reply(f'Данной группы не существует или же вы не лидер группы')

#@bot.event # ивент ошибок
#async def on_command_error(ctx,error):
  #   await ctx.send(f'```{error}```')

bot.run(TOKEN)
