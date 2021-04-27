from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, 𝗜'𝗺 𖤍﷼༺𓆩ＡＮＵＳＨＫＡ𓆪•᭄♡﷼𖤍

I can play music in your group's voice call. Developed by [⚡ＡＮＵＳＨＫＡ⚡](https://t.me/Secret_girl_Anushka).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥 𝚈𝙾𝚄𝚁 𝙼𝙰𝙺𝙴𝚁 🔥", url="https://t.me/Secret_girl_anushka")
                  ],[
                    InlineKeyboardButton(
                        "🔰 𝙶𝚁𝙾𝚄𝙿 🔰", url="https://t.me/secret_society_new"
                    ),
                    InlineKeyboardButton(
                        "🎛️ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 🎛️", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "😎 𝙰𝙳𝙳 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 😎", url="https://t.me/AnuMusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𖤍﷼༺𓆩ＡＮＵＳＨＫＡ𓆪•᭄♡﷼𖤍 is on fire 🔥 ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😈 𝙷𝙴𝚁𝙴 𝙸𝚂 𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 😈", url="https://t.me/secret_society_new")
                ]
            ]
        )
   )


