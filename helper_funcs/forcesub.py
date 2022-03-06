# (c) @AbirHasan2005 | @PredatorHackerzZ

import asyncio
from sample_config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

async def ForceSub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(Config.UPDATES_CHANNEL) if Config.UPDATE_CHANNEL.startswith("-100") else Config.UPDATE_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "banned":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Access Denied ⚠. Contact my [Master](https://t.me/Harshu_xD).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**<b>Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!\n\n⚜𝙿𝚘𝚠𝚎𝚛𝚎𝚍 𝙱𝚢 - 𝙷𝚊𝚛𝚜𝚑𝚞_𝚡𝙳</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join My Channel", url="https://t.me/StarterChannel")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something Went Wrong. Contact my [Master](https://t.me/Harshu_xD)",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
