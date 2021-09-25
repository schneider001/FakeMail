from aiogram.dispatcher.filters.state import StatesGroup, State


class Mail(StatesGroup):
    sender = State()
    receiver = State()
    title = State()
    body = State()
