import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import Client, Filters, ChatPermissions
from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, UserBannedInChannel

@pyrogram.Client.on_message(pyrogram.Filters.command(["rename"]))
async def rename_doc(bot, update):
    try:
        await bot.get_chat_member("Zed1Projctz", update.chat.id)
    except UserNotParticipant:
        await update.reply_text("Join @Zed1Projctz To Use Me")
    except UserBannedInChannel:
        await update.reply_text("You are Banned😌")
    except Exception:
        LOGGER.exception("Unable to verify user")
        await update.reply_text("Something wenr Wrong 😴")
    return False
