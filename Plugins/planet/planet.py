from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from discord.ext import commands
from modmail.plugin_helpers import PluginCog

if TYPE_CHECKING:
    from discord.ext.commands import Context
    from modmail.plugin_helpers import ModmailBot, ModmailLogger

log: ModmailLogger = logging.getLogger(__name__)


class Planet(PluginCog):
    """This is a planet."""

    def __init__(self, bot: ModmailBot):
        """Initialize the Planet plugin."""
        self.bot = bot

    @commands.command()
    async def world(self, ctx: Context) -> None:
        """Tell you what planet you are on."""
        log.debug(f"The alien {ctx.author} has requested to know what planet they are on.")
        await ctx.send("earth")


def setup(bot: ModmailBot) -> None:
    """Add the Planet plugin to the bot."""
    bot.add_cog(Planet(bot))
