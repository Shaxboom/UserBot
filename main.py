
import time

import pyfiglet
import os, sys
from telethon import TelegramClient, events, sync


def clearscreen():
    if sys.platform == "linux2":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


text = "\033[1;36mGlobalUserBot - Telegram akauntingiz uchun havfis Userbot\nGlobalUserBot - faqatgina animatsialar uchun tayyorlangan user bot\nHarkuni yangilanish boradi\nGlobalUserBot yangiliklari va Yangi modullarni telegram kanalimizda korishingiz mumkun\nUser botimiz hafsizlik siri uni serverga ulanmagani\nhttps://t.me/GLOBALUSERBOT_uz\n ###########################################\n"
clearscreen()
os.system("termux-open-url https://t.me/GLOBALUSERBOT_uz")
print(pyfiglet.figlet_format("Gloabal"))
print(text)

ip_id = input('Api_Id kiriting: ')
ip_hash = input('Api_hash kiriting')

api_id = ip_id
api_hash = ip_hash

client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    if '.moon' in event.raw_text:
        d = [ '🌑',  '🌘', '🌗', '🌖', '🌕', '🌚', '🌑', '🌒', '🌓', '🌔', '🌕', '🌚',]
        time.sleep(0.5)
        for i in range(5):
            time.sleep(0.5)
            for j in d:
                time.sleep(0.5)
                await event.edit(j)
    elif ".type" == event.raw_text[:5] and len(event.raw_text) > 6:
        orig_text = event.raw_text.split(".type ", maxsplit=1)[1]
        text = orig_text
        pb = ""
        typing_symbol = "▒"

        while (pb != orig_text):
            try:
                await event.edit(pb + typing_symbol)
                time.sleep(0.09)

                pb += text[0]
                text = text[1:]

                await event.edit(pb)
                time.sleep(0.09)

            except Exception as e:
                print(e)

    elif '.police' in event.raw_text:
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
         await event.edit("🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴\n🔵🔵🔵🔵⚪⚪🔴🔴🔴🔴")
         await event.edit("🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵\n🔴🔴🔴🔴⚪⚪🔵🔵🔵🔵")
    elif '.loading' in event.raw_text:
        await event.edit("🔳◼️◼️◼️◼️◼️◼️◼️◼️◼️10%")
        await event.edit("🔳🔳◼️◼️◼️◼️◼️◼️◼️◼️20%")
        await event.edit("🔳🔳🔳◼️◼️◼️◼️◼️◼️◼️ 30%")
        await event.edit("🔳🔳🔳🔳◼️◼️◼️◼️◼️◼️40%")
        await event.edit("🔳🔳🔳🔳🔳◼️◼️◼️◼️◼️50%")
        await event.edit("🔳🔳🔳🔳🔳🔳◼️◼️◼️◼️ 60%")
        await event.edit("🔳🔳🔳🔳🔳🔳🔳◼️◼️◼️70%")
        await event.edit("🔳🔳🔳🔳🔳🔳🔳🔳◼️◼️80%")
        await event.edit("🔳🔳🔳🔳🔳🔳🔳🔳🔳◼️ 90%")
        await event.edit("🔳🔳🔳🔳🔳🔳🔳🔳🔳🔳100%")
    elif '.love' in event.raw_text:
        await event.edit("❤️‍🔥❤️❤️❤️❤️❤️❤️❤️❤️❤️ 10%")
        await event.edit("❤️‍🔥❤️‍🔥❤️❤️❤️❤️❤️❤️❤️❤️ 20%")
        await event.edit("❤️‍🔥❤️‍🔥❤️‍🔥❤️❤️❤️❤️❤️❤️❤️ 30%")
        await event.edit("❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️❤️❤️❤️❤️❤️ 40%")
        await event.edit("❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️❤️❤️❤️❤️ 50%")
        await event.edit("❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️❤️❤️❤️ 60%")
        await event.edit("❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️❤️❤️ 70%")
        await event.edit("❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️❤️ 80%")
        await event.edit("❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️ 90%")
        await event.edit("❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥 100%")
        await event.edit("❤️‍🔥 I love you")
    elif '.fuck' in event.raw_text:
        await event.edit("👉========👊")
        await event.edit("👉=======👊")
        await event.edit("👉======👊")
        await event.edit("👉=====👊")
        await event.edit("👉====👊")
        await event.edit("👉===👊")
        await event.edit("👉==👊")
        await event.edit("👉=👊")
        await event.edit("👉👊💦")
        await event.edit("👉========👊")
        await event.edit("👉=======👊")
        await event.edit("👉======👊")
        await event.edit("👉=====👊")
        await event.edit("👉====👊")
        await event.edit("👉===👊")
        await event.edit("👉==👊")
        await event.edit("👉=👊")
        await event.edit("👉👊💦")
        await event.edit("👉========👊")
        await event.edit("👉=======👊")
        await event.edit("👉======👊")
        await event.edit("👉=====👊")
        await event.edit("👉====👊")
        await event.edit("👉===👊")
        await event.edit("👉==👊")
        await event.edit("👉=👊")
        await event.edit("👉👊💦")
        await event.edit("👉========👊")
        await event.edit("👉=======👊")
        await event.edit("👉======👊")
        await event.edit("👉=====👊")
        await event.edit("👉====👊")
        await event.edit("👉===👊")
        await event.edit("👉==👊")
        await event.edit("👉=👊")
        await event.edit("👉👊💦")
        await event.edit("👉========👊")
        await event.edit("👉=======👊")
        await event.edit("👉======👊")
        await event.edit("👉=====👊")
        await event.edit("👉====👊")
        await event.edit("👉===👊")
        await event.edit("👉==👊")
        await event.edit("👉=👊")
        await event.edit("👉👊💦")
        await event.edit("👉========👊")
        await event.edit("👉=======👊")
        await event.edit("👉======👊")
        await event.edit("👉=====👊")
        await event.edit("👉====👊")
        await event.edit("👉===👊")
        await event.edit("👉==👊")
        await event.edit("👉=👊")
        await event.edit("👉👊💦")
        await event.edit("Fuck You")
    elif '.magic' in event.raw_text:
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("❤️🧡💛💚💙💜🖤🤍🤎")
         await event.edit("🤎🤍🖤💜💙💚💛🧡❤️")
         await event.edit("Magic❤️")
    elif ".Juma" in event.raw_text:
        await event.edit("🌛👿👿👿👿👿👿👿👿👿")
        await event.edit("🌛🌛👿👿👿👿👿👿👿👿")
        await event.edit("🌛🌛🌛👿👿👿👿👿👿👿")
        await event.edit("🌛🌛🌛🌛👿👿👿👿👿👿")
        await event.edit("🌛🌛🌛🌛🌛👿👿👿👿👿")
        await event.edit("🌛🌛🌛🌛🌛🌛👿👿👿👿")
        await event.edit("🌛🌛🌛🌛🌛🌛🌛👿👿👿")
        await event.edit("🌛🌛🌛🌛🌛🌛🌛🌛👿👿")
        await event.edit("🌛🌛🌛🌛🌛🌛🌛🌛🌛👿")
        await event.edit("🌛🌛🌛🌛🌛🌛🌛🌛🌛🌛")
        await event.edit("Dostim Juma Muborak")

    elif '.clock' in event.raw_text:
        await event.edit("🕛")
        await event.edit("🕐")
        await event.edit("🕑")
        await event.edit("🕔")
        await event.edit("🕖")
        await event.edit("🕘")
        await event.edit("🕛")
        await event.edit("🕐")
        await event.edit("🕑")
        await event.edit("🕔")
        await event.edit("🕖")
        await event.edit("🕘")
        await event.edit("🕛")
        await event.edit("🕐")
        await event.edit("🕑")
        await event.edit("🕔")
        await event.edit("🕖")
        await event.edit("🕘")
        await event.edit("🕛")
        await event.edit("🕐")
        await event.edit("🕑")
        await event.edit("🕔")
        await event.edit("🕖")
        await event.edit("🕘")
        await event.edit("🕛")
        await event.edit("🕐")
        await event.edit("🕑")
        await event.edit("🕔")
        await event.edit("🕖")
        await event.edit("🕘")
        await event.edit("🕛")
        await event.edit("🕐")
        await event.edit("🕑")
        await event.edit("🕔")
        await event.edit("🕖")
        await event.edit("🕘")
        await event.edit("🕛")
        await event.edit("🕐")
        await event.edit("🕑")
        await event.edit("🕔")
        await event.edit("🕖")
        await event.edit("🕘")
        await event.edit("🕛")
        await event.edit("🕐")
        await event.edit("🕑")
        await event.edit("🕔")
        await event.edit("🕖")
        await event.edit("🕘")
        await event.edit("🕛")

    elif '.sweets' in event.raw_text:
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")
        await event.edit("🥮🍡🍧🍨🍦🥧🍭")
        await event.edit("🍭🥧🍦🍨🍧🍡🥮")

     


    elif '.info' in event.raw_text:
        await event.edit("""
        animoation[10]
        function[1]
        modules[0]
        art[0]

-------------------------------------------|
        animation:
        .clock - [Soat animatsiyasi]
        .love - [Sevgi ishor]
        .fuck - [Negativlarga animatsiya]
        .moon - [Oy animatsiyasi]
        .smayl - [Smayllar animatsiyasi]
        .loading - [Yuklash animatsiyasi]
        .police - [Politsiya animatsiyasi]
        .magic - [Ishlatsangiz bilasiz]
        .sweets - [Shirinliklar animatsiyasi]
        .Juma - [Juma tabriki]
-------------------------------------------------|                
        function:
        .type - [Text terish efekti]
        
-------------------------------------------------|
        modules:
        
        Tez orada qoshiladi
        
-------------------------------------------------|
        Arts:
        
        Tez orada qoshiladi
                                                  
-------------------------------------------------|                    """)

client.start()
client.run_until_disconnected()