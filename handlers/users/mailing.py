from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from utils.tools.sendmail import FakeMail

from filters import IsPrivate
from loader import dp
from states import Mail


@dp.message_handler(Command("send_message"), IsPrivate())
async def enter_mail(message: types.Message):
    await message.answer("Введите email отправителя (любой на ваше усмотрение)")

    await Mail.sender.set()


@dp.message_handler(IsPrivate(), state=Mail.sender)
async def enter_sender(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(sender=answer)

    await message.answer("Введите email получателя")

    await Mail.next()


@dp.message_handler(IsPrivate(), state=Mail.receiver)
async def enter_receiver(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(receiver=answer)

    await message.answer("Введите тему сообщения")

    await Mail.next()


@dp.message_handler(IsPrivate(), state=Mail.title)
async def enter_title(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(title=answer)

    await message.answer("Введите сообщение")

    await Mail.next()


@dp.message_handler(IsPrivate(), state=Mail.body)
async def enter_body(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(body=answer)

    await message.answer("Оправляем сообщение..."
                         "Это может занять пару секунд...")

    data = await state.get_data()

    await state.finish()

    fake_mail = FakeMail(data.get("sender"), data.get("receiver"), data.get("title"), data.get("body"))

    fake_mail.send_mail()


