from enum import Enum
import discord
from discord.ext import commands

class MemberConfigMode(Enum):
    ALL = 1
    SEPARATE = 2

class MemberConfigView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=120)
        self._mode = MemberConfigMode.ALL
        self._members = [
            "우사미",
            "여르미",
            "한결",
            "비몽",
            "에뇨",
            "샤르망",
        ]
        
    @property
    def description(self):
        desc = '## NotiArxiV 멤버 설정\n'
        if self._mode == MemberConfigMode.ALL:
            desc += '### 만들어질 채널\n- NotiArxiV'
        elif self._mode == MemberConfigMode.SEPARATE:
            desc += '### 만들어질 체널\n'
            for member in self._members:
                desc += f'- {member}\n'
        return desc
    
    @discord.ui.button(label = '한 채널에서 알림 받기', row=0)
    async def all_callback(self, interaction : discord.Interaction):
        self._mode = MemberConfigMode.ALL
        embed = interaction.message.embeds[0]
        embed.description = self.description
        await interaction.response.edit_message(view=self,embed=embed)

    @discord.ui.button(label = '채널을 세분화 해서 받기', row=0)
    async def separate_callback(self, interaction : discord.Interaction):
        self._mode = MemberConfigMode.SEPARATE
        embed = interaction.message.embeds[0]
        embed.description = self.description
        await interaction.response.edit_message(view=self,embed=embed)

    @discord.ui.select(
        placeholder="알림을 받을 멤버를 선택하세요",
        min_values=1, 
        max_values=7, 
        options=[
            discord.SelectOption(label="우사미", default=True),
            discord.SelectOption(label="여르미", default=True),
            discord.SelectOption(label="한결", default=True),
            discord.SelectOption(label="비몽", default=True),
            discord.SelectOption(label="에뇨", default=True),
            discord.SelectOption(label="샤르망", default=True),
            discord.SelectOption(label="고단씨"),
        ],
        row=2
    )

    async def select_option_callback(self, interaction: discord.Interaction, select: discord.ui.Select):
        self._members = select.values
        for option in select.options:
            option.default = option.label in self._members
        embed = interaction.message.embeds[0]
        embed.description = self.description
        await interaction.response.edit_message(view=self, embed=embed)

    async def _subscribe(self, channel, members):
        ...

    @discord.ui.button(label='✅ 설정하기', style=discord.ButtonStyle.primary, row=1)
    async def setting_button_callbask(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(
            view=None, embed=None, content="설정 중.."
        )
        channels = []
        if self._mode == MemberConfigMode.ALL:
            channel = await interaction.guild.create_text_channel("NotiArxiV")
            await self._subscribe(channel, self.members)
            channels.append(channel)

        elif self._mode == MemberConfigMode.SEPARATE:
            for member in self._members:
                channel = await interaction.guild.create_text_channel(member)
                await self._subscribe(channel, self.members)
                channels.append(channel)
        await interaction.edit_original_response(content='설정 완료!')

class MemberConfig(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="멤버설정")
    async def speed_setup(self, interaction: discord.Interaction):
        view = MemberConfigView()
        embed = discord.Embed(description=view.description, color=0x414141)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

async def setup(bot):
    await bot.add_cog(MemberConfig(bot))