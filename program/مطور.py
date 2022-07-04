import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["المطور"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2e2a064f53abd2d6ad24c.jpg",
        caption=f"""᥀︙𝗢𝘄𝗻𝗲𝗿 𝗡𝗮𝗺𝗲 : [- 𝖸𝗎᥆𝗌𝗌ᥱ𝖥 𝖺ᥣ 𝖲𝖺ᥣᎥ𝗁 .](t.me/GGG66) \n\n ᥀︙𝗢𝘄𝗻𝗲𝗿 𝗨𝘀𝗲𝗿 : @GGG66 \n\n ᥀︙𝗢𝘄𝗻𝗲𝗿 𝗶𝗗 : 1005593710""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- 𝖸𝗎᥆𝗌𝗌ᥱ𝖥 𝖺ᥣ 𝖲𝖺ᥣᎥ𝗁 .", url=f"https://t.me/GGG66"),
                ],[
                    InlineKeyboardButton(
                        "‹ 𝖣𝖾𝗏𝖤𝗏𝖺𝗇 𝖳𝖾𝖠𝗆 .", url="https://t.me/vrrrrvr"),
                ],
            ]
        ),
    )
