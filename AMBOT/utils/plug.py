import importlib
import logging
import os
import sys
from pathlib import Path

from AMBOTConfig import Config
from telethon.tl.types import InputMessagesFilterDocument
from AMBOT.clients.client_list import client_id
from AMBOT.clients.decs import hell_cmd
from AMBOT.clients.logger import LOGGER as LOGS
from AMBOT.clients.session import H2, H3, H4, H5, Hell, HellBot
from AMBOT.utils.cmds import CmdHelp
from AMBOT.utils.decorators import admin_cmd, command, sudo_cmd
from AMBOT.utils.extras import delete_hell, edit_or_reply
from AMBOT.utils.globals import LOAD_PLUG


# load plugins
def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        import AMBOT.utils

        path = Path(f"AMBOT/plugins/{shortname}.py")
        name = "AMBOT.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("⚡AMBOT⚡- Successfully imported " + shortname)
    else:
        import AMBOT.utils

        path = Path(f"AMBOT/plugins/{shortname}.py")
        name = "AMBOT.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = Hell
        mod.H1 = Hell
        mod.H2 = H2
        mod.H3 = H3
        mod.H4 = H4
        mod.H5 = H5
        mod.Hell = Hell
        mod.HellBot = HellBot
        mod.tbot = HellBot
        mod.tgbot = Hell.tgbot
        mod.command = command
        mod.CmdHelp = CmdHelp
        mod.client_id = client_id
        mod.logger = logging.getLogger(shortname)
        mod.Config = Config
        mod.borg = Hell
        mod.hellbot = Hell
        mod.edit_or_reply = edit_or_reply
        mod.eor = edit_or_reply
        mod.delete_hell = delete_hell
        mod.eod = delete_hell
        mod.Var = Config
        mod.admin_cmd = admin_cmd
        mod.hell_cmd = hell_cmd
        mod.sudo_cmd = sudo_cmd
        sys.modules["userbot.utils"] = AMBOT
        sys.modules["userbot"] = AMBOT
        sys.modules["userbot.events"] = AMBOT
        spec.loader.exec_module(mod)
        # for imports
        sys.modules["AMBOT.plugins." + shortname] = mod
        LOGS.info("⚡AMBOT⚡- Successfully Imported " + shortname)


# remove plugins
def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                Hell.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"AMBOT.plugins.{shortname}"

            for i in reversed(range(len(Hell._event_builders))):
                ev, cb = Hell._event_builders[i]
                if cb.__module__ == name:
                    del Hell._event_builders[i]
    except BaseException:
        raise ValueError


async def plug_channel(client, channel):
    if channel != 0:
        LOGS.info("⚡AMBOT⚡- PLUGIN CHANNEL DETECTED.")
        LOGS.info("⚡AMBOT⚡- Starting to load extra plugins.")
        plugs = await client.get_messages(channel, None, filter=InputMessagesFilterDocument)
        total = int(plugs.total)
        for plugins in range(total):
            plug_id = plugs[plugins].id
            plug_name = plugs[plugins].file.name
            if os.path.exists(f"AMBOT/plugins/{plug_name}"):
                return
            downloaded_file_name = await client.download_media(
                await client.get_messages(channel, ids=plug_id),
                "AMBOT/plugins/",
            )
            path1 = Path(downloaded_file_name)
            shortname = path1.stem
            try:
                load_module(shortname.replace(".py", ""))
            except Exception as e:
                LOGS.error(str(e))


# AMBOT 
