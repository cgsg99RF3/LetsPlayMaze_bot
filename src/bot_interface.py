from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message,
                           ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from src.player import Player
from src.path import Path


class BotInterface:
    dp = Dispatcher()

    def __init__(self, token):
        self.bot = Bot(token=token)

    users_id = []
    users = dict()

    key_words = {
        '/start': 'Hi lets play',
        'PLAY': 'Set params(text /params <width> <height> <maze_type>)',
        'EXIT': 'THE END',
        '/help': '"/start" - start game\n'
                 '"/params <width> <height> <type>" - set maze params'
    }

    bt_up = KeyboardButton(text='⬆️')
    bt_down = KeyboardButton(text='⬇️')
    bt_right = KeyboardButton(text='➡️')
    bt_left = KeyboardButton(text='⬅️')
    bt_play = KeyboardButton(text='PLAY')
    bt_solve = KeyboardButton(text='SOLVE')
    bt_path = KeyboardButton(text='SHOW PATH')
    bt_exit = KeyboardButton(text='EXIT')
    bt_stop = KeyboardButton(text='STOP')

    move_keyboard = [[bt_up], [bt_left, bt_right], [bt_down], [bt_stop]]

    @staticmethod
    @dp.message(CommandStart())
    async def process_start_command(message: Message):
        if message.from_user.id not in BotInterface.users_id:
            BotInterface.users_id.append(message.from_user.id)
            new_player = Player(message)
            BotInterface.users[message.from_user.id] = new_player
        await message.answer(
            text=BotInterface.key_words['/start'],
            reply_markup=ReplyKeyboardMarkup(keyboard=[[BotInterface.bt_play]])
        )

    @staticmethod
    @dp.message(F.text == 'PLAY')
    async def process_play_command(message: Message):
        await message.answer(
            text=BotInterface.key_words['PLAY'],
            reply_markup=ReplyKeyboardRemove()
        )

    @dp.message(F.text.startswith('/params'))
    async def process_params_command(message: Message):
        params = message.text.split()
        cur_player = BotInterface.users[message.from_user.id]
        cur_player.create_maze(int(params[1]), int(params[2]), params[3])

        await message.answer(
            text=cur_player.draw(),
            reply_markup=ReplyKeyboardMarkup(keyboard=[[BotInterface.bt_solve, BotInterface.bt_path],
                                                       [BotInterface.bt_stop]])
        )

    @staticmethod
    @dp.message(F.text == 'SOLVE')
    async def process_play_command(message: Message):
        cur_player = BotInterface.users[message.from_user.id]
        cur_player.pos = [0, 0]
        await message.answer(
            text=cur_player.draw() + 'SOLVE',
            reply_markup=ReplyKeyboardMarkup(keyboard=BotInterface.move_keyboard)
        )

    @staticmethod
    @dp.message(F.text == '⬇️')
    async def process_play_command(message: Message):
        cur_player = BotInterface.users[message.from_user.id]
        text = [0, 1]
        cur_player.move(text)
        if (cur_player.check()):
            await message.answer(
                text=cur_player.draw() + 'YOU WON!',
                reply_markup=ReplyKeyboardMarkup(keyboard=[[BotInterface.bt_path],
                                                           [BotInterface.bt_stop]])
            )
        else:
            await message.answer(
                text=cur_player.draw(),
                reply_markup=ReplyKeyboardMarkup(keyboard=BotInterface.move_keyboard)
            )

    @staticmethod
    @dp.message(F.text == '⬆️')
    async def process_play_command(message: Message):
        cur_player = BotInterface.users[message.from_user.id]

        text = [0, -1]
        cur_player.move(text)
        if (cur_player.check()):
            await message.answer(
                text='YOU WON!\n' + cur_player.draw(),
                reply_markup=ReplyKeyboardMarkup(keyboard=[[BotInterface.bt_path],
                                                           [BotInterface.bt_stop]])
            )
        else:
            await message.answer(
                text=cur_player.draw(),
                reply_markup=ReplyKeyboardMarkup(keyboard=BotInterface.move_keyboard)
            )

    @staticmethod
    @dp.message(F.text == '➡️')
    async def process_play_command(message: Message):
        cur_player = BotInterface.users[message.from_user.id]

        text = [1, 0]
        cur_player.move(text)
        if (cur_player.check()):
            await message.answer(
                text='YOU WON!\n' + cur_player.draw(),
                reply_markup=ReplyKeyboardMarkup(keyboard=[[BotInterface.bt_path],
                                                           [BotInterface.bt_stop]])
            )
        else:
            await message.answer(
                text=cur_player.draw(),
                reply_markup=ReplyKeyboardMarkup(keyboard=BotInterface.move_keyboard)
            )

    @staticmethod
    @dp.message(F.text == '⬅️')
    async def process_play_command(message: Message):
        cur_player = BotInterface.users[message.from_user.id]

        text = [-1, 0]
        cur_player.move(text)
        if (cur_player.check()):
            await message.answer(
                text='YOU WON!\n' + cur_player.draw(),
                reply_markup=ReplyKeyboardMarkup(keyboard=[[BotInterface.bt_path],
                                                           [BotInterface.bt_stop]])
            )
        else:
            await message.answer(
                text=cur_player.draw(),
                reply_markup=ReplyKeyboardMarkup(keyboard=BotInterface.move_keyboard)
            )

    @staticmethod
    @dp.message(F.text == 'SHOW PATH')
    async def process_play_command(message: Message):
        cur_player = BotInterface.users[message.from_user.id]
        path = Path(cur_player.maze)
        path.find(0, 0, cur_player.maze)
        await message.answer(
            text=cur_player.draw(),
            reply_markup=ReplyKeyboardMarkup(keyboard=[[BotInterface.bt_exit]])
        )

    @staticmethod
    @dp.message(F.text == 'STOP')
    async def process_play_command(message: Message):
        cur_player = BotInterface.users[message.from_user.id]
        await message.answer(
            text=cur_player.draw(),
            reply_markup=ReplyKeyboardMarkup(keyboard=[[BotInterface.bt_path],
                                                       [BotInterface.bt_exit]])
        )

    @staticmethod
    @dp.message(F.text == 'EXIT')
    async def process_play_command(message: Message):
        cur_player = BotInterface.users[message.from_user.id]
        await message.answer(
            text= cur_player.draw() + BotInterface.key_words['EXIT'],
            reply_markup=ReplyKeyboardRemove()
        )

    @staticmethod
    @dp.message(F.text == '/help')
    async def process_help_command(message: Message):
        await message.answer(text=BotInterface.key_words['/help'])

    @staticmethod
    @dp.message()
    async def process_unknown_command(message: Message):
        await message.answer(text='Unknown command. Please, try again. To see all commands do /help')
    def run(self):
        BotInterface.dp.run_polling(self.bot)
