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
        'EXIT': 'THE END'
    }

    bt_up = KeyboardButton(text='⬆️')
    bt_down = KeyboardButton(text='⬇️')
    bt_right = KeyboardButton(text='➡️')
    bt_left = KeyboardButton(text='⬅️')

    move_keyboard = [[bt_up], [bt_left, bt_right], [bt_down]]

    @staticmethod
    @dp.message(CommandStart())
    async def process_start_command(message: Message):
        if message.from_user.id not in BotInterface.users_id:
            BotInterface.users_id.append(message.from_user.id)
            new_player = Player(message)
            BotInterface.users[message.from_user.id] = new_player
        await message.answer(
            text=BotInterface.key_words['/start'],
            reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='PLAY')]])
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
            reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='SOLVE'), KeyboardButton(text='SHOW PATH')],
                                                       [KeyboardButton(text='EXIT')]])
        )

    @staticmethod
    @dp.message(F.text == 'SOLVE')
    async def process_play_command(message: Message):
        await message.answer(
            text='SOLVE',
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
                text='YOU WON!\n' + cur_player.draw(),
                reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='SHOW PATH')],
                                                           [KeyboardButton(text='EXIT')]])
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
                reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='SHOW PATH')],
                                                           [KeyboardButton(text='EXIT')]])
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
                reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='SHOW PATH')],
                                                           [KeyboardButton(text='EXIT')]])
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
                reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='SHOW PATH')],
                                                           [KeyboardButton(text='EXIT')]])
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
            reply_markup=ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='SHOW PATH')],
                                                       [KeyboardButton(text='EXIT')]])
        )

    @staticmethod
    @dp.message(F.text == 'EXIT')
    async def process_play_command(message: Message):
        await message.answer(
            text=BotInterface.key_words['EXIT'],
            reply_markup=ReplyKeyboardRemove()
        )

    def run(self):
        BotInterface.dp.run_polling(self.bot)
