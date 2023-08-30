from aiogram import Bot, Dispatcher,types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.types import URLInputFile

import asyncio

from aiogram.filters import Text, Command

from config import TOKEN_API

from aiogram.types import Message

from trauma_photo import trauma_photo_0, trauma_photo_1, trauma_photo_2, trauma_photo_3, trauma_photo_4, trauma_photo_5

from cyberpunk_photo import cyberpunk_photo_0, cyberpunk_photo_1, cyberpunk_photo_2

from arthoe_photo import art_hoe_0, art_hoe_1, art_hoe_2

from usa_photo import usa_0, usa_1, usa_2

bot = Bot(TOKEN_API)

dp = Dispatcher()

kb_0 = [
        [types.KeyboardButton(text="🤕Traumacore💔")],
        [types.KeyboardButton(text="🦾Cyberpunk🦿")],
        [types.KeyboardButton(text="🌻Art Hoe🌻")],
        [types.KeyboardButton(text="🇺🇸Americana🇺🇸")],
        [types.KeyboardButton(text="Общая информация 📝")]
    ]

kb_1 = [  
        [types.KeyboardButton(text = 'Назад🔙')] 
        ]

@dp.message(Command('start'))
async def cmd_start(message:types.Message):
    await message.answer('Привет, котик 😼! Введи комманду /menu, чтобы появилось меню с выбором эстетики 💫 и информацией 💻')
    await message.delete()

@dp.message(Command('menu'))
async def cmd_menu(message:types.Message):
    
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_0)
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_0,
        resize_keyboard=True,
        input_field_placeholder="Выберите эстетику🤔"
    )


    await message.answer("Твоё меню", reply_markup=keyboard)
    await message.delete()

@dp.message(Text("🤕Traumacore💔"))
async def cmd_traumacore(message:types.Message):
        # 1 фото traumacore
        await bot.send_photo(photo=trauma_photo_0, chat_id=message.from_user.id)
        # 2 фото traumacore
        await bot.send_photo(photo=trauma_photo_1, chat_id=message.from_user.id)
        # 3 фото traumacore
        await bot.send_photo(photo=trauma_photo_2, chat_id=message.from_user.id)
        # 4 фото traumacore
        await bot.send_photo(photo=trauma_photo_3, chat_id=message.from_user.id)
        # 5 фото traumacore
        await bot.send_photo(photo=trauma_photo_4, chat_id=message.from_user.id)
        # 6 фото traumacore
        await bot.send_photo(photo=trauma_photo_5, chat_id=message.from_user.id)

        keyboard = types.ReplyKeyboardMarkup(keyboard=kb_1)    
        keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_1,
        resize_keyboard=True,
        input_field_placeholder="Выберите эстетику"
    )
        await message.answer("Можешь вернуться обратно⬅", reply_markup=keyboard)
        await message.delete()

@dp.message(Text("🦾Cyberpunk🦿"))
async def cmd_traumacore(message:types.Message):
        # 1 фото cyberpunk
        await bot.send_photo(photo=cyberpunk_photo_0, chat_id=message.from_user.id)
        # 2 фото cyberpunk
        await bot.send_photo(photo=cyberpunk_photo_1, chat_id=message.from_user.id)
        # 3 фото cyberpunk
        await bot.send_photo(photo=cyberpunk_photo_2, chat_id=message.from_user.id)
        
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb_1)    
        keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_1,
        resize_keyboard=True,
        input_field_placeholder="Выберите эстетику"
    )
        await message.answer("Можешь вернуться обратно⬅", reply_markup=keyboard)
        await message.delete()

@dp.message(Text("🌻Art Hoe🌻"))
async def cmd_art_hoe(message:types.Message):
     # 1 фото art hoe
     await bot.send_photo(photo=art_hoe_0, chat_id=message.from_user.id)
     # 2 фото art hoe
     await bot.send_photo(photo=art_hoe_1, chat_id=message.from_user.id)
     # 3 фото art hoe
     await bot.send_photo(photo=art_hoe_2, chat_id=message.from_user.id)

     keyboard = types.ReplyKeyboardMarkup(keyboard=kb_1)    
     keyboard = types.ReplyKeyboardMarkup(
     keyboard=kb_1,
     resize_keyboard=True,
     input_field_placeholder="Выберите эстетику"
     )
     await message.answer("Можешь вернуться обратно⬅", reply_markup=keyboard)
     await message.delete()

@dp.message(Text("🇺🇸Americana🇺🇸"))
async def cmd_usa(message:types.Message):
     # 1 фото art hoe
     await bot.send_photo(photo=usa_0, chat_id=message.from_user.id)
     # 2 фото art hoe
     await bot.send_photo(photo=usa_1, chat_id=message.from_user.id)
     # 3 фото art hoe
     await bot.send_photo(photo=usa_2, chat_id=message.from_user.id)

     keyboard = types.ReplyKeyboardMarkup(keyboard=kb_1)    
     keyboard = types.ReplyKeyboardMarkup(
     keyboard=kb_1,
     resize_keyboard=True,
     input_field_placeholder="Выберите эстетику"
     )
     await message.answer("Можешь вернуться обратно⬅", reply_markup=keyboard)
     await message.delete()

@dp.message(Text("Общая информация 📝"))
async def cmd_information(message:types.Message):
     await message.answer("😊Данный бот позволяет выбрать эстетику из этих фото📸 и отправить её в чат💻.На данный момент это только начальная версия бота❗")
     await message.delete()

@dp.message(Text("Назад🔙"))   
async def cmd_back(message:types.Message):
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_0)
    
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb_0,
        resize_keyboard=True,
        input_field_placeholder="Выберите эстетику"
    )


    await message.answer("Твоё меню", reply_markup=keyboard)
    await message.delete()


    
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())