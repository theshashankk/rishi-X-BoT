from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAEJar1gfUPxtIX1OutHd1sOi37QRKjBTQACPgADiHb1PyaUZ16x2sykHwQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Rishi](https://t.me/xD_Rishi).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Moi Op Wale Master", url="https://t.me/xD_Rishi")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/NiceJokeLol"
                    ),
                    InlineKeyboardButton(
                        "🎛️ Commands 🎛️", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "😎 Add To Your Group 😎", url="https://t.me/MusicExeBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Moi Op Wale Owner", url="https://t.me/@xD_Rishi")
                ]
            ]
        )
   )


