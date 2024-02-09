import discord as discord
from discord.ext import commands

# custom leader error 
class LeaderError(commands.CheckFailure):
    pass

class TeamsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_leader():
        # is leader or admin / mod check
        async def predicate(ctx):
            if any('Лидер' in name for name in [role.name for role in ctx.author.roles]): return True
            else: raise LeaderError('Вы не являетесь лидером ни одной команды.')
        # return commands.check(predicate) and commands.is_owner()
        return commands.check(predicate)

    @is_leader()
    @commands.hybrid_group(name='team', aliases=['t'])
    async def _team_command(self, ctx, /):
        # send a guide
        print(ctx)
        pass
    
    @_team_command.command(name='create', aliases=['c', 'setup', 's'])
    async def _team_create_command(self, ctx, /):

        await ctx.guild.fetch_channels()
        last_cat = 1
        for cat in ctx.guild.categories: 
            if 'Группа №' in cat.name: last_cat += 1

        color = discord.Color.random()
        group_leader_role = await ctx.guild.create_role(name=f'Лидер № {last_cat}', color=color)
        group_member_role = await ctx.guild.create_role(name=f'Группа № {last_cat}', color=color)
        supervisor_role = discord.utils.find(lambda role: 'Куратор' in role.name, ctx.guild.roles)
        helper_role = discord.utils.find(lambda role: 'Хелпер' in role.name, ctx.guild.roles)
        moderator_role = discord.utils.find(lambda role: 'Модератор' in role.name, ctx.guild.roles)

        group_divider_position = discord.utils.find(lambda r: 'Группы' in r.name, ctx.guild.roles).position - 1

        await group_leader_role.edit(position=group_divider_position-1)
        await group_member_role.edit(position=group_divider_position-1)

        group_category_overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            group_leader_role: discord.PermissionOverwrite(read_messages=True, connect=True),
            group_member_role: discord.PermissionOverwrite(read_messages=True, connect=True),
            supervisor_role: discord.PermissionOverwrite(read_messages=True),
            helper_role: discord.PermissionOverwrite(read_messages=True),
            moderator_role: discord.PermissionOverwrite(read_messages=True)
        }
        
        locked_channel_overwrites = group_category_overwrites.copy()
        locked_channel_overwrites[group_member_role].update(send_messages=False)

        category = await ctx.guild.create_category(f'Группа № {last_cat}', overwrites=group_category_overwrites)

        await category.create_text_channel('『📰』новости', overwrites=locked_channel_overwrites)
        await category.create_text_channel('『📂』ресурсы', overwrites=locked_channel_overwrites)
        await category.create_text_channel('『💬』чат')
        await category.create_stage_channel('『🗣』Собрание')
        await category.create_voice_channel('『🗣』Общение')
    
    @is_leader()
    @_team_command.command(name='edit', aliases=['e'])
    async def _team_edit_command(self, ctx, team_num: int = None):
        # edit
        print(ctx)
        pass

    @is_leader()
    @_team_command.command(name='add', aliases=['a'])
    async def _team_add_command(self, ctx, team_num: int = None):
        # add members
        print(ctx)
        pass

    @is_leader()
    @_team_command.command(name='remove', aliases=['r', 'kick', 'k'])
    async def _team_remove_command(self, ctx, team_num: int = None):
        # remove members
        print(ctx)
        pass


async def setup(bot):
    print('teams_commands cog loaded')
    await bot.add_cog(TeamsCog(bot=bot))
