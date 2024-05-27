from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ R⃠E⃠P⃠O⃠ T⃠O⃠ N⃠H⃠I⃠ D⃠U⃠N⃠G⃠A⃠ T⃠U⃠J⃠H⃠A⃠ ✪
 
 ➲ 𝐍𝐢𝐜𝐡𝐚 𝐝𝐚𝐤𝐡 𝐛𝐨𝐡𝐚𝐭 𝐬𝐚 𝐜𝐨𝐦𝐦𝐞𝐧𝐝 𝐡𝐚 𝐭𝐫𝐲 𝐤𝐚𝐫 ✰
 
 ➲ 𝐑𝐄𝐏𝐎 𝐊𝐀 𝐁𝐀𝐀𝐓 𝐀𝐏𝐍𝐀 𝐃𝐈𝐌𝐀𝐆 𝐒𝐀 𝐔𝐃𝐀 𝐃𝐀 ✰
 
 ➲ 𝐌𝐀𝐑𝐀 𝐒𝐀𝐓𝐇 𝐀𝐊 𝐁𝐀𝐀𝐑 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐊𝐀𝐑 ✰
 
 ➲ 𝐎𝐈𝐒𝐀 𝐓𝐔 𝐑𝐄𝐏𝐎 𝐋𝐀𝐊𝐀 𝐊𝐀𝐘𝐀 𝐊𝐀𝐑𝐀 𝐆𝐀  ✰
 
 ➲ 𝐑𝐄𝐏𝐎 𝐄𝐃𝐈𝐓 𝐊𝐀𝐄𝐍𝐀 𝐓𝐎 𝐓𝐀𝐑𝐀 𝐊𝐎 𝐀𝐓𝐀 𝐍𝐇𝐈 ✰
 
 ► 𝐌𝐀𝐑𝐀 𝐊𝐎 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐊𝐀𝐑 𝐌𝐀 𝐀𝐊 𝐑𝐄𝐏𝐎 𝐃𝐀𝐃𝐔𝐍𝐆𝐀
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝔸𝔻𝔻 𝕄𝔼 𝔹𝔸𝔹𝕐", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝐈𝐒𝐌𝐀 𝐉𝐎𝐈𝐍 𝐊𝐀𝐑 𝐌𝐀 𝐇𝐄𝐋𝐏 𝐊𝐀𝐑𝐔𝐍𝐆𝐀", url="https://t.me/anokhikeduniya"),
          InlineKeyboardButton("𝐀𝐑𝐀 𝐌𝐀 𝐇𝐔 𝐎𝐖𝐍𝐄𝐑", url="https://t.me/II_SB_ANGLE_II"),
          ],
               [
                InlineKeyboardButton("𝔻ℙ", url="https://t.me/anokhikeduniya"),

],
[
              InlineKeyboardButton("𝕊𝕋𝕐𝕃𝕀𝕊ℍ ℕ𝔸𝕄𝔼", url=f"https://t.me/anokhikeduniya"),
              InlineKeyboardButton("︎𝕊𝕋𝕐𝕃𝕀𝕊ℍ 𝔹𝕀𝕆", url=f"https://t.me/anokhikeduniya"),
              ],
              [
              InlineKeyboardButton("𝔹𝕆𝕐𝕊 𝔻ℙ", url=f"https://t.me/anokhikeduniya"),
InlineKeyboardButton("𝔾𝕀ℝ𝕃𝕊 𝔻ℙ", url=f"https://t.me/anokhikeduniya"),
],
[
InlineKeyboardButton("𝕃𝕆𝕍𝔼 𝕊ℍ𝕐ℝ𝕀𝔼", url=f"https://t.me/anokhikeduniya"),
InlineKeyboardButton("ℂ𝕆𝕌ℙ𝕃𝔼 𝔻ℙ", url=f"https://t.me/anokhikeduniya"),
],
[
              InlineKeyboardButton("𝕊𝔸𝔻𝔻ℙ", url=f"https://t.me/anokhikeduniya"),
              InlineKeyboardButton("𝕃𝕆𝕍𝔼 𝔻ℙ", url=f"https://t.me/anokhikeduniya"),
              ],
              [
              InlineKeyboardButton("𝕊𝔸𝔻 𝕍𝕀𝔻𝔼𝕆", url=f"https://t.me/anokhikeduniya"),
InlineKeyboardButton("𝕃𝕆𝕍𝔼 𝕍𝕀𝔻𝔼𝕆", url=f"https://t.me/anokhikeduniya"),
],
[
InlineKeyboardButton("𝕔𝕙𝕒𝕟𝕟𝕖𝕝", url=f"https://t.me/anokhikeduniya"),
InlineKeyboardButton("𝕣𝕖𝕡𝕠", url=f"https://t.me/anokhikeduniya"),
],
[
InlineKeyboardButton("𝕦𝕣𝕗𝕚 𝕛𝕒𝕧𝕖𝕕", url=f"https://t.me/anokhikeduniya"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/faa1f3ad7116e33d9f402.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("𝕓𝕤𝕕𝕜 𝕣𝕖𝕡𝕠 𝕝𝕒𝕜𝕒 𝕒𝕡𝕟𝕒 𝕘𝕒𝕟𝕕 𝕞𝕒 𝕕𝕒𝕝𝕒 𝕘𝕒 𝕜𝕒𝕪𝕒 ")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://t.me/anokhikeduniya) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/anokhikeduniya)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


