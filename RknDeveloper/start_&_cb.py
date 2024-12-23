
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
        await bot.text(m.from_user.id, "**Hey, {}!\nWelcome To {}\n\n__Pᴏᴡᴇʀᴅ Bʏ : @CinemaKalavaraTG**".format(m.from_user.mention, m.chat.title), reply_markup=InlineKeyboardMarkup([[
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

@Client.on_message(filters.command("start"))
async def start_commond(bot, m :Message):
    if m.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await rkn_botz.add_chat(bot, m)
        return await m.reply_text("**❣️ Hᴇʟʟᴏ {}!\n\nWʀɪᴛᴇ Mᴇ Pʀɪᴠᴀᴛᴇ Fᴏʀ Mᴏʀᴇ Dᴇᴛᴀɪʟs.**".format(m.from_user.first_name), reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Pʀɪᴠᴀᴛᴇ", url=f"https://t.me/{bot.username}?start=start")
                    ]
                ]
            ))
            
    await rkn_botz.add_user(bot, m)   
    await m.reply_text("**I'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Pᴏᴡᴇʀᴅ Bʏ : @CinemaKalavaraTG__**".format(m.from_user.mention), reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                    ],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("💥 Uᴘᴅᴀᴛᴇ 💥", url="https://t.me/+sT56Fh1VXZ81ZWRl")
                ],[
                InlineKeyboardButton("🔎 Sᴜᴘᴘᴏʀᴛ 🔍", url="https://t.me/+sT56Fh1VXZ81ZWRl")
            ]]))
            
 
@Client.on_callback_query(filters.regex("start"))
async def start_query(bot, cb : CallbackQuery):
    await cb.message.edit("**Hᴇy, {}!\n\nI'ᴍ Aɴ Aᴜᴛᴏ Aᴘᴘʀᴏᴠᴇ [Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛs]({}) Bᴏᴛ.\nI Cᴀɴ Aᴘᴘʀᴏᴠᴇ Usᴇʀs Iɴ Cʜᴀɴɴᴇʟs & Gʀᴏᴜᴘs.Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Aɴᴅ Gʀᴏᴜᴘ ᴀɴᴅ Pʀᴏᴍᴏᴛᴇ Mᴇ Tᴏ Aᴅᴍɪɴ Wɪᴛʜ Aᴅᴅ Mᴇᴍʙᴇʀs Pᴇʀᴍɪssɪᴏɴ.\n\n__Powerd By : @CinemaKalavaraTG__**".format(cb.from_user.mention), reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ ࿇", url=f"https://t.me/{bot.username}?startchannel=Bots4Sale&admin=invite_users+manage_chat")
                    ],[
                InlineKeyboardButton("✛ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ࿇", url=f"https://t.me/{bot.username}?startgroup=Bots4Sale&admin=invite_users+manage_chat")
                ],[
                InlineKeyboardButton("💥 Uᴘᴅᴀᴛᴇ 💥", url="https://t.me/+sT56Fh1VXZ81ZWRl")
                ],[
                InlineKeyboardButton("🔎 Sᴜᴘᴘᴏʀᴛ 🔍", url="https://t.me/+sT56Fh1VXZ81ZWRl")
            ]]))
    
