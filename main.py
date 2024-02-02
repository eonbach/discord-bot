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

bot.run(TOKEN)