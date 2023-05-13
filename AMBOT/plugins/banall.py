import asyncio
from time import sleep

from telethon.errors import FloodWaitError
from telethon.tl import functions
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (ChannelParticipantsAdmins,
                               ChannelParticipantsKicked, ChatBannedRights,
                               UserStatusEmpty, UserStatusLastMonth,
                               UserStatusLastWeek, UserStatusOffline,
                               UserStatusOnline, UserStatusRecently)
from AMBOT.plugins import *

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)


@hell_cmd(pattern="kickall$", allow_sudo=False)
async def _(event):
    ForGo10God, _, _ = await client_id(event)
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, ForGo10God)
    )
    if not result.participant.admin_rights.ban_users:
        return await parse_error(event, "𝘼𝙙𝙢𝙞𝙣 𝘽𝙖𝙣𝙖𝙤 𝙈𝙪𝙟𝙝𝙚")
    hell = await eor(event, "**𝙂𝙞𝙧𝙡𝙁𝙧𝙞𝙚𝙣𝙙 𝙄𝙣𝙨𝙩𝙖𝙡𝙞𝙣𝙜**")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client.kick_participant(event.chat_id, user.id)
                success += 1
                await asyncio.sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await asyncio.sleep(0.5)
    await hell.edit("**𝙆𝙞𝙡𝙡𝙚𝙙 𝘽𝙔 𝘼𝙈𝘽𝙊𝙏**")
    await event.client.send_message(
        Config.LOGGER_ID,
        f"#KICKALL \n\nKicked Out  `{success}`  of  `{total}`  members",
    )


@hell_cmd(pattern="banall$", allow_sudo=False)
async def _(event):
    ForGo10God, _, _ = await client_id(event)
    result = await event.client(
        functions.channels.GetParticipantRequest(event.chat_id, ForGo10God)
    )
    if not result.participant.admin_rights.ban_users:
        return await parse_error(event, "𝘼𝙙𝙢𝙞𝙣 𝘽𝙖𝙣𝙖𝙤 𝙈𝙪𝙟𝙝𝙚")
    hell = await eor(event, "**𝙂𝙞𝙧𝙡𝙁𝙧𝙞𝙚𝙣𝙙 𝙄𝙣𝙨𝙩𝙖𝙡𝙞𝙣𝙜**")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
                success += 1
                await asyncio.sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await asyncio.sleep(0.5)
    await hell.edit("**𝙆𝙞𝙡𝙡𝙚𝙙 𝘽𝙔 𝘼𝙈𝘽𝙊𝙏**")
    await event.client.send_message(
        Config.LOGGER_ID,
        f"#BANALL \n\nSucessfully banned  `{success}`  out of  `{total}`  members!!",
    )


@hell_cmd(pattern="unbanall$")
async def _(event):
    if event.is_private:
        return
    xyz = await eor(event, "𝙎𝙚𝙖𝙧𝙘𝙝𝙞𝙣𝙜 𝙋𝙖𝙧𝙩𝙞𝙘𝙞𝙥𝙖𝙣𝙩 𝙇𝙞𝙨𝙩𝙨.")
    p = 0
    async for i in event.client.iter_participants(
        event.chat_id, filter=ChannelParticipantsKicked, aggressive=True
    ):
        rights = ChatBannedRights(until_date=0, view_messages=False)
        try:
            await event.client(
                functions.channels.EditBannedRequest(event.chat_id, i, rights)
            )
        except FloodWaitError as ex:
            LOGS.warn("sleeping for {} seconds".format(ex.seconds))
            sleep(ex.seconds)
        except Exception as ex:
            await xyz.edit(str(ex))
        else:
            p += 1
    await xyz.edit("{}: {} unbanned".format(event.chat_id, p))


@hell_cmd(pattern="ikuck(?:\s|$)([\s\S]*)")
async def _(event):
    if event.is_private:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not (chat.admin_rights or chat.creator):
            await parse_error(event, "𝙄'𝙢 𝙉𝙤𝙩 𝘼 𝙖𝙙𝙢𝙞𝙣 𝙝𝙚𝙧𝙚!")
            return
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    hell = await eor(event, "𝙎𝙚𝙖𝙧𝙘𝙝𝙞𝙣𝙜 𝙋𝙖𝙧𝙩𝙞𝙘𝙞𝙥𝙖𝙣𝙩 𝙇𝙞𝙨𝙩𝙨.")
    async for i in event.client.iter_participants(event.chat_id):
        p = p + 1
        rights = ChatBannedRights(until_date=None, view_messages=True)
        if isinstance(i.status, UserStatusEmpty):
            y = y + 1
            if "y" in input_str:
                status, e = await ban_user(event, event.chat_id, i, rights)
                if not status:
                    await parse_error(hell, "𝙄 𝙉𝙚𝙚𝙙 𝘼𝙙𝙢𝙞𝙣 𝙋𝙤𝙬𝙚𝙧 𝙗𝙖𝙣 𝙋𝙤𝙬𝙚𝙧 + 𝙂𝙧𝙤𝙪𝙥 𝙄𝙣𝙛𝙤 𝙁𝙤𝙧 𝙖𝙘𝙩𝙞𝙤𝙣!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusLastMonth):
            m = m + 1
            if "m" in input_str:
                status, e = await ban_user(event, event.chat_id, i, rights)
                if not status:
                    await parse_error(hell, "𝙄 𝙉𝙚𝙚𝙙 𝘼𝙙𝙢𝙞𝙣 𝙋𝙤𝙬𝙚𝙧 𝙗𝙖𝙣 𝙋𝙤𝙬𝙚𝙧 + 𝙂𝙧𝙤𝙪𝙥 𝙄𝙣𝙛𝙤 𝙁𝙤𝙧 𝙖𝙘𝙩𝙞𝙤𝙣!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusLastWeek):
            w = w + 1
            if "w" in input_str:
                status, e = await ban_user(event, event.chat_id, i, rights)
                if not status:
                    await parse_error(event, "𝙄 𝙉𝙚𝙚𝙙 𝘼𝙙𝙢𝙞𝙣 𝙋𝙤𝙬𝙚𝙧 𝙗𝙖𝙣 𝙋𝙤𝙬𝙚𝙧 + 𝙂𝙧𝙤𝙪𝙥 𝙄𝙣𝙛𝙤 𝙁𝙤𝙧 𝙖𝙘𝙩𝙞𝙤𝙣!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusOffline):
            o = o + 1
            if "o" in input_str:
                status, e = await ban_user(event, event.chat_id, i, rights)
                if not status:
                    await parse_error(event, "𝙄 𝙉𝙚𝙚𝙙 𝘼𝙙𝙢𝙞𝙣 𝙋𝙤𝙬𝙚𝙧 𝙗𝙖𝙣 𝙋𝙤𝙬𝙚𝙧 + 𝙂𝙧𝙤𝙪𝙥 𝙄𝙣𝙛𝙤 𝙁𝙤𝙧 𝙖𝙘𝙩𝙞𝙤𝙣!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusOnline):
            q = q + 1
            if "q" in input_str:
                status, e = await ban_user(event, event.chat_id, i, rights)
                if not status:
                    await parse_error(event, "𝙄 𝙉𝙚𝙚𝙙 𝘼𝙙𝙢𝙞𝙣 𝙋𝙤𝙬𝙚𝙧 𝙗𝙖𝙣 𝙋𝙤𝙬𝙚𝙧 + 𝙂𝙧𝙤𝙪𝙥 𝙄𝙣𝙛𝙤 𝙁𝙤𝙧 𝙖𝙘𝙩𝙞𝙤𝙣!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if isinstance(i.status, UserStatusRecently):
            r = r + 1
            if "r" in input_str:
                status, e = await ban_user(event, event.chat_id, i, rights)
                if not status:
                    await parse_error(event, "𝙄 𝙉𝙚𝙚𝙙 𝘼𝙙𝙢𝙞𝙣 𝙋𝙤𝙬𝙚𝙧 𝙗𝙖𝙣 𝙋𝙤𝙬𝙚𝙧 + 𝙂𝙧𝙤𝙪𝙥 𝙄𝙣𝙛𝙤 𝙁𝙤𝙧 𝙖𝙘𝙩𝙞𝙤𝙣!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        if i.bot:
            b = b + 1
            if "b" in input_str:
                status, e = await ban_user(event, event.chat_id, i, rights)
                if not status:
                    await parse_error(event, "𝙄 𝙉𝙚𝙚𝙙 𝘼𝙙𝙢𝙞𝙣 𝙋𝙤𝙬𝙚𝙧 𝙗𝙖𝙣 𝙋𝙤𝙬𝙚𝙧 + 𝙂𝙧𝙤𝙪𝙥 𝙄𝙣𝙛𝙤 𝙁𝙤𝙧 𝙖𝙘𝙩𝙞𝙤𝙣!")
                    e.append(str(e))
                    break
                else:
                    c = c + 1
        elif i.deleted:
            d = d + 1
            if "d" in input_str:
                status, e = await ban_user(event, event.chat_id, i, rights)
                if not status:
                    await parse_error(event, "𝙄 𝙉𝙚𝙚𝙙 𝘼𝙙𝙢𝙞𝙣 𝙋𝙤𝙬𝙚𝙧 𝙗𝙖𝙣 𝙋𝙤𝙬𝙚𝙧 + 𝙂𝙧𝙤𝙪𝙥 𝙄𝙣𝙛𝙤 𝙁𝙤𝙧 𝙖𝙘𝙩𝙞𝙤𝙣!")
                    e.append(str(e))
                else:
                    c = c + 1
        elif i.status is None:
            n = n + 1
    if input_str:
        required_string = """Kicked {} / {} users
Deleted Accounts: {}
UserStatusEmpty: {}
UserStatusLastMonth: {}
UserStatusLastWeek: {}
UserStatusOffline: {}
UserStatusOnline: {}
UserStatusRecently: {}
Bots: {}
None: {}"""
        await hell.edit(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await asyncio.sleep(5)
    await hell.edit(
        """Total: {} users
Deleted Accounts: {}
UserStatusEmpty: {}
UserStatusLastMonth: {}
UserStatusLastWeek: {}
UserStatusOffline: {}
UserStatusOnline: {}
UserStatusRecently: {}
Bots: {}
None: {}""".format(
            p, d, y, m, w, o, q, r, b, n
        )
    )


async def ban_user(event, chat_id, user_id, rights):
    try:
        await event.client(functions.channels.EditBannedRequest(chat_id, user_id, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)


@hell_cmd(pattern="blockall(?:\s|$)([\s\S]*)")
async def block_all(event):
    if event.is_private:
        return
    ForGo10God, _, _ = await client_id(event)
    hell = await eor(event, "𝘽𝙡𝙤𝙘𝙠𝙞𝙣𝙜 𝘼𝙡𝙡 𝙈𝙚𝙢𝙗𝙚𝙧𝙨 𝙄𝙣 𝙂𝙧𝙤𝙪𝙥 𝙈𝙖𝙨𝙨 𝙋𝙤𝙬𝙚𝙧...")
    failed = 0
    success = 0
    await hell.edit("**𝙎𝙩𝙖𝙧𝙩 𝙈𝙖𝙨𝙨 𝘽𝙡𝙤𝙘𝙠𝙞𝙣𝙜 !!**")
    async for user in event.client.iter_participants(event.chat_id):
        try:
            await event.client(functions.contacts.BlockRequest(id=user.id))
            success += 1
        except Exception as e:
            LOGS.info(str(e))
            failed += 1
    await hell.edit(f"**𝙈𝙖𝙨𝙨 𝘽𝙡𝙤𝙘𝙠 𝘿𝙤𝙣𝙚... !!** \n\n__Blocked:__ `{success} users` \n__Failed:__ `{failed} users`")


@hell_cmd(pattern="blockc(?:\s|$)([\s\S]*)")
async def block_contacts(event):
    if event.is_private:
        return
    ForGo10God, _, _ = await client_id(event)
    hell = await eor(event, "𝙈𝙖𝙨𝙨 𝘽𝙡𝙤𝙘𝙠𝙠𝙞𝙣𝙜 𝘼𝙡𝙡 𝙄𝙣 𝙘𝙤𝙣𝙩𝙖𝙘𝙩𝙨 𝙞𝙣 𝙏𝙝𝙞𝙨 𝙂𝙧𝙤𝙪𝙥")
    failed = 0
    success = 0
    await hell.edit("**𝙎𝙩𝙖𝙧𝙩 𝙈𝙖𝙨𝙨 𝘽𝙡𝙤𝙘𝙠𝙞𝙣𝙜 !!**")
    async for user in event.client.iter_participants(event.chat_id):
        result_ompho = await event.client(functions.contacts.GetContactsRequest(hash=0))
        if user in result_ompho:
            try:
                await event.client(functions.contacts.BlockRequest(id=user.id))
                success += 1
            except Exception as e:
                LOGS.info(str(e))
                failed += 1
        else:
            return await eod(hell, "𝙉𝙤 𝙁𝙤𝙪𝙣𝙙 𝘾𝙖𝙣𝙩𝙖𝙘𝙩 𝙐𝙨𝙚𝙧 𝙄𝙣 𝙏𝙝𝙞𝙨 𝙂𝙧𝙤𝙪𝙥")
    await hell.edit(f"**𝙈𝙖𝙨𝙨 𝘽𝙡𝙤𝙘𝙠 𝘿𝙤𝙣𝙚 𝙄𝙣 𝙏𝙝𝙞𝙨 𝙂𝙧𝙤𝙪𝙥 !!** \n\n__Blocked:__ `{success} users` \n__Failed:__ `{failed} users`")


@hell_cmd(pattern="blocknc(?:\s|$)([\s\S]*)")
async def block_noncontacts(event):
    if event.is_private:
        return
    ForGo10God, _, _ = await client_id(event)
    hell = await eor(event, "𝙈𝙖𝙨𝙨 𝘽𝙡𝙤𝙘𝙠𝙞𝙣𝙜 𝙉𝙤𝙣 𝘾𝙤𝙣𝙩𝙖𝙘𝙩𝙨 𝙄𝙣 𝙏𝙝𝙞𝙨 𝙂𝙧𝙤𝙪𝙥")
    failed = 0
    success = 0
    await hell.edit("**𝙈𝙖𝙨𝙨 𝘽𝙡𝙤𝙘𝙠𝙞𝙣𝙜 𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜 !!**")
    async for user in event.client.iter_participants(event.chat_id):
        result_ompho = await event.client(functions.contacts.GetContactsRequest(hash=0))
        if user not in result_ompho:
            try:
                await event.client(functions.contacts.BlockRequest(id=user.id))
                success += 1
            except Exception as e:
                LOGS.info(str(e))
                failed += 1
        else:
            return await eod(hell, "𝙉𝙤 𝙁𝙤𝙪𝙣𝙙  𝙉𝙤𝙣 𝘾𝙖𝙣𝙩𝙖𝙘𝙩  𝙐𝙨𝙚𝙧𝙨 𝙄𝙣 𝙏𝙝𝙞𝙨 𝙂𝙧𝙤𝙪𝙥")
    await hell.edit(f"**𝙈𝙖𝙨𝙨 𝘽𝙡𝙤𝙘𝙠 𝘿𝙤𝙣𝙚 !!** \n\n__Blocked:__ `{success} users` \n__Failed:__ `{failed} users`")


@hell_cmd(pattern = "unblockall(?:\s|$)([\s\S]*)")
async def ublock_all(event):
    if event.is_private:
        return
    ForGo10God, _, _ = await client_id(event)
    hell = await eor(event, "𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜")
    failed = 0
    success = 0
    await hell.edit("**𝘼𝙡𝙡 𝘽𝙡𝙤𝙘𝙠𝙚𝙙 𝙐𝙨𝙚𝙧𝙨 𝙈𝙖𝙨𝙨 𝙐𝙣𝘽𝙡𝙤𝙘𝙠𝙞𝙣𝙜  !!**")
    async for user in event.client.iter_participants(event.chat_id):
        try:
            await event.client(functions.contacts.UnblockRequest(id=user.id))
            success += 1
        except Exception as e:
            LOGS.info(str(e))
            failed += 1
    await hell.edit(f"**𝙐𝙨𝙚𝙧 𝙐𝙣𝘽𝙡𝙤𝙘𝙠𝙚𝙙 𝘿𝙤𝙣𝙚 !!** \n\n__Unblocked:__ `{success} users` \n__Failed:__ `{failed} users`")    


CmdHelp("banall").add_command(
    "ikuck", None, "Bans all users with given criteria. Deleted accounts, Last seen, Offline, Online, Recently, Bots, Etc."
).add_command(
    "unbanall", None, "Unbans all the user in the chat."
).add_command(
    "banall", None, "Bans all the user in the chat.."
).add_command(
    "kickall", None, "Kicks all the users in the chat..."
).add_command(
    "blockall", None, "Block all the members in the group."
).add_command(
    "blockc", None, "Block all the contact members in the group."
).add_command(
    "blocknc", None, "Block all the non-contact members in the group."
).add_command(
    "unblockall", None, "Unblock all the members in the group."
).add_info(
    "⚠️𝗔𝗠𝗕𝗢𝗧 𝗣𝗼𝘄𝗲𝗿 𝗚𝗿𝗼𝘂𝗽 𝗗𝗲𝘀𝘁𝗿𝗼𝘆𝗲𝗿"
).add_warning(
    "✅ Harmless Module."
).add()
