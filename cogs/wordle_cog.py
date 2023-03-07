from discord.ext import commands
from discord.ext.commands.context import Context


class WordleCog(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

        self.current_word = None
        self.guesses = 0

    @commands.command(name='new_wordle')
    async def new_wordle(self, ctx: Context, *args):
        try:
            if args:
                word = ' '.join(args)
                if len(word) == 5:
                    self.current_word = word
                    await ctx.send('Starting wordle with a five letter word')
                else:
                    await ctx.send('Please enter a valid word (5 letters long)')
            else:
                await ctx.send('Error')

        except Exception as error:
            print(f'{error.__class__}: {error}')


async def setup(bot: commands.Bot):
    await bot.add_cog(WordleCog(bot))
    print('Cog Added')
