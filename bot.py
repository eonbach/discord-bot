import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv

from config import *

load_dotenv(override=True)
TOKEN = getenv("TOKEN")


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.reaction_role_message_ids = reaction_role_message_ids

        self.emoji_to_role = {
            self.reaction_role_message_ids['specializations']: {
                "🌐": "Веб-разработка",
                "📱": "Мобильная разработка",
                "🖥️": "Десктоп разработка",
                "🎮": "Разработка игр",
                "🗃️": "Базы данных",
                "🤖": "Аналитика, МО",
                "🛠️": "Тестирование, DevOps",
                "🔒": "Кибербезопасность",
                "🔗": "Блокчейн",
                "🎨": "Дизайн, UI/UX",
                "🏗️": "Проектирование ПО"
            },
            self.reaction_role_message_ids['languages']: {
                "1️⃣": "Python",
                "2️⃣": "JavaScript",
                "3️⃣": "Ruby",
                "4️⃣": "Go",
                "5️⃣": "PHP",
                "6️⃣": "Java",
                "7️⃣": "C#",
                "8️⃣": "C | C++",
                "9️⃣": "HTML | CSS",
                "🔟": "SQL"
            }
        }
    
    async def on_ready(self):
        print(f'вход выполнен, {self.user}')

    async def on_message(self, message):
        if message.author.id == 652407336287076362: await self.process_commands(message)

    async def setup_hook(self):
        await self.load_extension('jishaku')
        await self.load_extension('cogs.teams_commands')
        await self.load_extension('cogs.reaction_roles')


intents = discord.Intents.all()
command_prefix = "!"

bot = MyBot(intents=intents, command_prefix=command_prefix)

bot.run(TOKEN)