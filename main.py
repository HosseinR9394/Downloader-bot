from aiogram import Bot,Dispatcher,executor,types
import requests as rq
import os

bot = Bot("Your Telegram bot token")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def welcome(pm: types.message):
    await pm.answer("Please send your download link 😊")

@dp.message_handler()
async def welcome(pm: types.message):
    dl = pm.text
    await pm.answer("I got your link 🤓")
    try:
        res = rq.get(dl)
    except Exception as e:
        await pm.answer("Your download link is invalid 😐")
    file_name = res.url[dl.rfind("/")+1:]

    await pm.answer("Your file is being downloaded.please wait 🙏")
    with open(file_name,"wb") as f:
        for chunk in res.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)
    await pm.answer("Your file has been downloaded 🫡 ")
    await pm.answer("Wait to upload 👇")
    await bot.send_document(
        chat_id=pm.from_user.id,
        document=open(file_name,"rb")
    )
    os.remove(file_name)


if __name__ == "__main__":
    executor.start_polling(dp)
