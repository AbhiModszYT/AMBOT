from random import choice

import requests
from AMBOT.plugins import *


@hell_cmd(pattern="love$")
async def love(e):
    txt = choice(LOVESTR)
    await eor(e, txt)


@hell_cmd(pattern="dhoka$")
async def katgya(e):
    txt = choice(DHOKA)
    await eor(e, txt)


@hell_cmd(pattern="same$")
async def metoo(e):
    txt = choice(METOOSTR)
    await eor(e, txt)


@hell_cmd(pattern="gda$")
async def noon(e):
    txt = choice(GDNOON)
    await eor(e, txt)


@hell_cmd(pattern="chase$")
async def police(e):
    txt = choice(CHASE_STR)
    await eor(e, txt)


@hell_cmd(pattern="nice$")
async def Sahih(e):
    txt = choice(CONGRATULATION)
    await eor(e, txt)


@hell_cmd(pattern="hi$")
async def hoi(e):
    txt = choice(HELLOSTR)
    await eor(e, txt)


@hell_cmd(pattern="bbye$")
async def bhago(e):
    txt = choice(BYESTR)
    await eor(e, txt)


@hell_cmd(pattern="gn$")
async def night(e):
    txt = choice(GDNIGHT)
    await eor(e, txt)


@hell_cmd(pattern="gm$")
async def morning(e):
    txt = choice(GDMORNING)
    await eor(e, txt)


@hell_cmd(pattern="quote(?:\s|$)([\s\S]*)")
async def quote_search(event):
    hell = await eor(event, "`Processing...`")
    input_str = event.pattern_match.group(1)
    if not input_str:
        api_url = "https://quotes.cwprojects.live/random"
        try:
            response = requests.get(api_url).json()
        except:
            response = None
    else:
        api_url = f"https://quotes.cwprojects.live/search/query={input_str}"
        try:
            response = choice(requests.get(api_url).json())
        except:
            response = None
    if response is not None:
        await hell.edit(f"`{response['text']}`")
    else:
        await parse_error(hell, "No quote found! Try again later.")


CmdHelp("quotes").add_command(
    "quote", "<input>", "Sends a random mind-blowing quote"
).add_command(
    "gm", None, "Sends a random Good Morning Quote"
).add_command(
    "gn", None, "Sends a random Good Night Quote"
).add_command(
    "bbye", None, "Sends a random Good Byee Quote"
).add_command(
    "hi", None, "Sends a random Hello msg"
).add_command(
    "nice", None, "Sends a random congratulations quote"
).add_command(
    "chase", None, "Sends a random Chase quote"
).add_command(
    "gda", None, "Sends a random Good Afternoon quote"
).add_command(
    "same", None, "Sends a text saying Mee too."
).add_command(
    "dhoka", None, "Sends a random Dhoka quote(katt gya bc)"
).add_command(
    "love", None, f"Sends a random love quote🥰. (A stage before {hl}dhoka)"
).add_info(
    "Random Quotes."
).add_warning(
    "✅ Harmless Module."
).add()
