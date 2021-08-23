import logging

from discord.ext import commands
from discord.ext.commands import Context
from modmail.plugin_helpers import ModmailBot, ModmailLogger, PluginCog

log: ModmailLogger = logging.getLogger(__name__)


class Planet(PluginCog):
    """This is a planet."""

    def __init__(self, bot: ModmailBot):
        """Initialize the Planet plugin."""
        self.bot = bot

    @commands.command()
    async def world(self, ctx: Context) -> None:
        """Tell you what planet you are on."""
        log.debug("The alien {0} has requested to know what planet they are on.".format(ctx.author))
        await ctx.send("earth")


def setup(bot: ModmailBot) -> None:
    """Add the Planet plugin to the bot."""
    bot.add_cog(Planet(bot))
