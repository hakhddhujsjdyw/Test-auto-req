

# pyrogram imports
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, enums, errors
from pyrogram.errors import UserNotParticipant, PeerIdInvalid, UserIsBlocked

# bots imports
from RknDeveloper.database import rkn_botz
from configs import rkn1
import random, asyncio, os


# Main Process _ _ _ _ _ Users Send Massage 🥀__🥀 Please 😢 Give Credit

@Client.on_chat_join_request()#filters.group | filters.channel & filters.private)
async def approve_request(bot, m):
    try:
        await rkn_botz.add_chat(bot, m)
        await bot.approve_chat_join_request(m.chat.id, m.from_user.id)
        img = random.choice(rkn1.SURPRICE)
        await bot.send_video(m.from_user.id, img, "**Hey, {}!\nWelcome To {}\n\n__Pᴏᴡᴇʀᴅ Bʏ : @RknDeveloper__**".format(m.from_user.mention, m.chat.title), reply_markup=InlineKeyboardMarkup([[
        InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
        ],[
        InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")]]))
        await rkn_botz.add_user(bot, m)
    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid as err:
        print(f"user isn't start bot (means group) Error- {err}")
    except Exception as err:
        print(f"Error\n{str(err)}")
        
   
# Start Massage _____ # Please 😢 Give Credit 

@Client.on_message(filters.command("start") & filters.private)
async def start_cmd(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    await message.reply_photo(photo=Rkn_Bots.RKN_PIC,
        caption=f"<b>Hey, {message.from_user.mention}\n\nI'm an auto-caption bot. I automatically edit captions for videos, audio files, and documents posted on channels.\n\nuse <code>/set_caption</code> to set caption\nUse<code>/delcaption</code> To delete caption and set caption to default.\n\nNote:All commands works on channels only</b>",
        reply_markup=types.InlineKeyboardMarkup([[
            types.InlineKeyboardButton('Main Channel', url='https://t.me/RknDeveloper'),
            types.InlineKeyboardButton('Help Group', url='https://t.me/Rkn_Bots_Support')
            ],[
            types.InlineKeyboardButton('🔥 Source Code 🔥', url='https://github.com/RknDeveloper/Rkn-AutoCaptionBot')
    ]]))
    

