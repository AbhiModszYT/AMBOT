# FOR SELF HOST
# EDIT THIS FILE AND RENAME TO config.py TO MAKE THIS BOT WORKING
# FILL THESE VALUES ACCORDINGLY.

from AMBOTConfig.config import Config


class Development(Config):
    # get these values from my.telegram.org.
    
    APP_ID = 12227067  # 666666 is a placeholder. Fill your 6 digit api id
    API_HASH = "b463bedd791aa733ae2297e6520302fe"  # replace this with your api hash
    BOT_TOKEN = "6230935112:AAGa2tofpAG9IlD1vKp3Tb0Wvm4I7fRpR6U"  # Create a bot from @BotFather and paste the token here
    BOT_LIBRARY = "telethon"  # fill 'pyrogram' if you want pyrogram version of hellbot else leave it as it is.
    DATABASE_URL = "mongodb+srv://AbhiModszYT:AbhiModszYT@abhimodszyt.flmdtda.mongodb.net/?retryWrites=true&w=majority"  # A postgresql database url from elephantsql
    HELLBOT_SESSION = "Your value"  # telethon or pyrogram string according to BOT_LIBRARY
    HANDLER = "."  # Custom Command Handler
    SUDO_HANDLER = "!"  # Custom Command Handler for sudo users.


# end of required config
# AMBOT
