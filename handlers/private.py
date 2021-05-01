from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey there, 𝗜'𝗺 ⚡ 𝐂𝐎𝐅𝐅𝐈𝐍 𝐌𝐔𝐒𝐈𝐂 ™ ⚡

I can play music in your group's voice call. Developed by [⚡ 𝐑𝐢𝐒𝐇𝐢_𝐱𝐃 ⚡](https://t.me/xD_Rishi).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "♻ 𝐎𝐖𝐍𝐄𝐑 ♻", url="https://t.me/xD_Rishi")
                  ],[
                    InlineKeyboardButton(
                        "🔰 𝐆𝐑𝐎𝐔𝐏 🔰", url="https://t.me/NiceJokeLol"
                    ),
                    InlineKeyboardButton(
                        "🎛️ 𝐌𝐀𝐍𝐔𝐀𝐋 🎛️", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ 𝐀𝐃𝐃 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏 ➕", url="https://t.me/MusicExeBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⚡ 𝐂𝐎𝐅𝐅𝐈𝐍 ™ ⚡ is on fire 🔥 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😈 𝐇𝐄𝐑𝐄 𝐈𝐒 𝐌𝐘 𝐇𝐄𝐋𝐋 😈", url="https://t.me/Definitely_not")
                ]
            ]
        )
   )


