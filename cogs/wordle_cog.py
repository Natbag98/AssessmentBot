from discord.ext import commands
from discord.ext.commands.context import Context
import random


class WordleCog(commands.Cog):

    def __init__(self, bot: commands.Bot) -> None:
        """
        A cog that lets a discord user play wordle with this bot
        """
        self.bot = bot

        self.current_word = None
        self.guesses = 0

        self.la = self.get_words('La')
        self.ta = self.get_words('Ta')

    def get_words(self, file_to_open: str) -> list:
        """
        Opens a .txt file in the words folder and gets all the words contained in the file.
        """
        word_list = []
        with open(f'./words/{file_to_open}.txt') as file:
            words = file.readlines()
        [word_list.append(w[:-1]) for w in words]
        return word_list
    
    def reset(self, word: str | None) -> None:
        """
        Resets the wordle back to its default values.\n
        Current word will be set to word.
        """
        self.current_word = word
        self.guesses = 0

    def resolve_guess(self, word: str) -> str:
        """
        Add docstring
        """
        if word == self.current_word:
            self.reset(None)
            return 'Congrats!\nYou succesfully guessed the word.'
        
        word_list = []
        for letter in word:
            word_list.append(letter)
        current_word_list = []
        for letter in self.current_word:
            current_word_list.append(letter)

        display = ''
        for i, letter in enumerate(word_list):
            if current_word_list[i] == letter:
                display += f'{letter}: Green\n'
            elif letter in current_word_list:
                display += f'{letter}: Yellow\n'
            else:
                display += f'{letter}: Grey\n'
        
        self.guesses += 1
        if self.guesses == 5:
            s = f'\nYou did not guess the word in time.\nThe word was {self.current_word}.'
            self.reset(None)
            return f'{display}{s}'
        elif self.guesses == 4:
            return f'{display}\nYou are on your last guess'
        return display[:-1]

    @commands.command(name='new_wordle', help='Start a new wordle game')
    async def new_wordle(self, ctx: Context, *args):
        try:
            word = random.choice(self.la)
            self.reset(word)
            await ctx.send('New wordle started')

        except Exception as error:
            print(f'{error.__class__}: {error}')

    @commands.command(name='guess', help='Guess a word')
    async def guess(self, ctx: Context, word=None, *args):
        try:
            if self.current_word is not None:
                if len(word) == 5:
                    if word in self.la or word in self.ta:
                        s = self.resolve_guess(word)
                    else:
                        s = 'Invalid word'
                else:
                    s = 'Invalid word'
            else:
                s = 'No wordle currently in progress.\nPlease start one using $new_wordle'
            await ctx.send(s)

        except Exception as error:
            print(f'{error.__class__}: {error}')

async def setup(bot: commands.Bot):
    await bot.add_cog(WordleCog(bot))
    print('Cog Added')
