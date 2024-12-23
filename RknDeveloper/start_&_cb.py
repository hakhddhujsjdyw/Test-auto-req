# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Special Thanks To (https://github.com/JayMahakal98)
# Update Channel @Digital_Botz & @DigitalBotz_Support

"""
Apache License 2.0
Copyright (c) 2022 @RknDeveloper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/RknDeveloper
Repo Link : https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot
License Link : https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot/blob/main/LICENSE
"""

# pyrogram imports
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, enums, errors
from pyrogram.errors import UserNotParticipant, PeerIdInvalid, UserIsBlocked

# bots imports
from RknDeveloper.database import rkn_botz
from RknDeveloper.fs import force_sub
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
    

#🔥 Please Don't Remove Credit 💳 # ❣️ 
@Client.on_callback_query(filters.regex('about'))
async def about_query(bot, update):
	await update.message.edit_text(
	    #⚠️ don't change source code & source link ⚠️ #
	    text = """<b>» Mʏ Nᴀᴍᴇ: <a href='https://t.me/Rkn_AutoRequestApprovebot'>Aᴜᴛᴏ Jᴏɪɴ Rᴇǫᴜᴇsᴛ Bᴏᴛ</a>
‣ Cʀᴇᴀᴛᴏʀ : <a href='tg://settings'>ᴛʜɪs Pᴇʀsᴏɴ</a>
‣ Dᴇᴠᴇʟᴏᴘᴇʀ : <a href='https://t.me/RknDeveloperr'>ʀᴋɴ Dᴇᴠᴇʟᴏᴘᴇʀ</a>
‣ Lɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org'>Pʏʀᴏɢʀᴀᴍ</a>
‣ Lᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org'>Pʏᴛʜᴏɴ 3</a>
‣ Dᴀᴛᴀ Bᴀsᴇ : <a href='https://www.mongodb.com/'>Mᴏɴɢᴏ Dʙ</a>
‣ Bᴏᴛ Sᴇʀᴠᴇʀ : ‣[Vᴘs]‣<a href='https://app.koyeb.com/'>[Kᴏʏᴇʙ]</a>
‣ Sᴏᴜʀᴄᴇ : <a href='https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot'> Sᴏᴜʀᴄᴇ Cᴏᴅᴇ </a>
‣ Bᴜɪʟᴅ Sᴛᴀᴛᴜs : ᴠ2.1.1 [sᴛᴀʙʟᴇ]</b>""",
	    reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("❣️ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ ❣️", url="https://github.com/RknDeveloper/Rkn_Auto-Request-Approve-bot")],[
               InlineKeyboardButton("→ Bᴀᴄᴋ", callback_data = "start")
               ]]
            )
    )
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
# Update Channel @Digital_Botz & @DigitalBotz_Support
