import logging
from typing import TYPE_CHECKING

import discord
from discord.ext import commands
from discord.ext.commands import Context
from dulwich import porcelain
from dulwich.repo import Repo

import modmail
from modmail.addons.helpers import ExtMetadata, PluginCog


if TYPE_CHECKING:
    from dulwich.objects import Commit
EXT_METADATA = ExtMetadata()

logger: modmail.ModmailLogger = logging.getLogger(__name__)


class GitCog(PluginCog):
    """A few commands for getting info on the git repo."""

    def __init__(self, bot: modmail.ModmailBot):
        """Initialise variables."""
        self.bot = bot
        self.repo = Repo(".")

    @commands.command()
    async def git(self, ctx: Context) -> None:
        """Returns a little bit of info about the current commit."""
        head = self.repo.head()
        commit: "Commit" = self.repo[head]

        current_branch = porcelain.active_branch(self.repo)
        embed = discord.Embed(title="Current Repo")
        embed.url = f"https://github.com/discord-modmail/modmail/tree/{current_branch.decode()}"
        commit_info = {
            "Message": f"```diff\n{commit.message.decode().strip()}\n```",
            "SHA": head.decode(),
            "Author": commit.author.decode(),
        }
        branch_info = {
            "Tree": current_branch.decode(),
        }

        commit_embed_info = ""
        for k, v in commit_info.items():
            v = v.strip()
            commit_embed_info += f"{k}: {v}\n"
        embed.add_field(name="Commit", value=commit_embed_info)

        branch_embed_info = ""
        for k, v in branch_info.items():
            v = v.strip()
            branch_embed_info += f"{k}: {v}\n"
        embed.add_field(name="Branch", value=branch_embed_info)

        await ctx.send(embed=embed)


def setup(bot: modmail.ModmailBot) -> None:
    """Create and add a GitCog to the bot."""
    bot.add_cog(GitCog(bot))
