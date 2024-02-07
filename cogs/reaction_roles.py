import discord as discord
from discord.ext import commands

from datetime import datetime


class ReactionRolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.message_id not in self.bot.reaction_role_message_ids.values():
            return
        
        guild = self.bot.get_guild(payload.guild_id)

        try:
            role_name = self.bot.emoji_to_role[payload.message_id][payload.emoji.name]
        except:
            return
        
        role = discord.utils.get(guild.roles, name=role_name)

        await payload.member.add_roles(role)

        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {payload.member}: +{role_name}')
    

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if payload.message_id not in self.bot.reaction_role_message_ids.values():
            return

        guild = self.bot.get_guild(payload.guild_id)

        try:
            role_name = self.bot.emoji_to_role[payload.message_id][payload.emoji.name]
        except:
            return
        
        role = discord.utils.get(guild.roles, name=role_name)

        member = guild.get_member(payload.user_id)

        await member.remove_roles(role)

        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} {member}: -{role_name}') 



async def setup(bot):
    print('reaction_roles cog loaded')
    await bot.add_cog(ReactionRolesCog(bot=bot))