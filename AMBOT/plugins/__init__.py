from AMBOTConfig import Config, db_config, os_config
from AMBOT import HEROKU_APP, StartTime
from AMBOT.clients.client_list import (client_id, clients_list,
                                              get_user_id)
from AMBOT.clients.decs import hell_cmd, hell_handler
from AMBOT.clients.instaAPI import InstaGram
from AMBOT.clients.logger import LOGGER
from AMBOT.clients.session import (H2, H3, H4, H5, Hell, HellBot,
                                          validate_session)
from AMBOT.DB import gvar_sql
from AMBOT.helpers.anime import *
from AMBOT.helpers.classes import *
from AMBOT.helpers.convert import *
from AMBOT.helpers.exceptions import *
from AMBOT.helpers.formats import *
from AMBOT.helpers.gdriver import *
from AMBOT.helpers.google import *
from AMBOT.helpers.ig_helper import *
from AMBOT.helpers.image import *
from AMBOT.helpers.int_str import *
from AMBOT.helpers.mediatype import *
from AMBOT.helpers.mmf import *
from AMBOT.helpers.movies import *
from AMBOT.helpers.pasters import *
from AMBOT.helpers.pranks import *
from AMBOT.helpers.progress import *
from AMBOT.helpers.runner import *
from AMBOT.helpers.tools import *
from AMBOT.helpers.tweets import *
from AMBOT.helpers.users import *
from AMBOT.helpers.vids import *
from AMBOT.helpers.yt_helper import *
from AMBOT.strings import *
from AMBOT.utils.cmds import *
from AMBOT.utils.decorators import *
from AMBOT.utils.errors import *
from AMBOT.utils.extras import *
from AMBOT.utils.funcs import *
from AMBOT.utils.globals import *
from AMBOT.utils.plug import *
from AMBOT.utils.startup import *
from AMBOT.version import __hellver__, __telever__

cjb = "./AMBOTConfig/resources/pics/cjb.jpg"
hell_logo = "https://telegra.ph/file/9470b838234d9535b0f82.jpg"
restlo = "./AMBOTConfig/resources/pics/rest.jpeg"
shhh = "./AMBOTConfig/resources/pics/chup_madarchod.jpeg"
shuru = "./AMBOTConfig/resources/pics/shuru.jpg"
spotify_logo = "./AMBOTConfig/resources/pics/spotify.jpg"


hell_emoji = Config.EMOJI_IN_HELP
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hellbot_version = __hellver__
telethon_version = __telever__
abuse_m = "Enabled" if str(Config.ABUSE).lower() in enabled_list else "Disabled"
is_sudo = "True" if gvar_sql.gvarstat("SUDO_USERS") else "False"

my_channel = Config.MY_CHANNEL or "AbhiModszYT_Return"
my_group = Config.MY_GROUP or "AM_YTSupport"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/AbhiModszYT_Return"
grp_link = "https://t.me/AM_YTSupport"
hell_channel = f"[AbhiModszYT]({chnl_link})"
hell_grp = f"[AMBOT Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {count} : To get group members
  {first} : To use user first name
  {fullname} : To use user full name
  {last} : To use user last name
  {mention} :  To mention the user
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
  {title} : To get chat name in message
  {userid} : To use userid
  {username} : To use user username
"""

# AMBOT