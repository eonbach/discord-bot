import discord
from discord.ext import commands
from os import getenv
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(override=True)
TOKEN = getenv("TOKEN")

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.reaction_role_message_ids = (1203436981531709442, 1203437020022841455)
        self.emoji_to_role = {
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
                "🏗️": "Проектирование ПО",
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


    async def on_ready(self):
        print(f'вход выполнен, {self.user}')

    async def on_message(self, message):
        if message.author.id == 652407336287076362: await self.process_commands(message)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.message_id not in self.reaction_role_message_ids:
            return
        
        guild = self.get_guild(payload.guild_id)

        try:
            role_name = self.emoji_to_role[payload.emoji.name]
        except:
            return
        
        role = discord.utils.get(guild.roles, name=role_name)

        await payload.member.add_roles(role)

        print(f'{datetime.now().strftime("%Y-%j-%d %H:%M:%S")} {payload.member}: +{role_name}')
    

    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if payload.message_id not in self.reaction_role_message_ids:
            return

        guild = self.get_guild(payload.guild_id)

        try:
            role_name = self.emoji_to_role[payload.emoji.name]
        except:
            return
        
        role = discord.utils.get(guild.roles, name=role_name)

        member = guild.get_member(payload.user_id)

        await member.remove_roles(role)

        print(f'{datetime.now().strftime("%Y-%j-%d %H:%M:%S")} {member}: -{role_name}')


intents = discord.Intents.all()
command_prefix = "."

bot = MyBot(intents=intents, command_prefix=command_prefix)

bot.run(TOKEN)