from pyrogram import Client, filters
from pyrogram.types import ChatPrivileges
from Tanjiro import TanjiroUb, SUDO

@TanjiroUb.on_message(filters.command("promote", prefixes=".") & filters.me)
async def promote_user(_, message):
    mes = message
 
    if not message.reply_to_message:
        return await mes.edit("Please reply to the user you want to promote.")

    reply = message.reply_to_message
    chat_id = message.chat.id
    new_admin_id = reply.from_user.id
    bot_stats = await TanjiroUb.get_chat_member(chat_id, "self")
    
    if not bot_stats.privileges or not bot_stats.privileges.can_promote_members:
        return await mes.edit("I don't have the necessary privileges to promote members.")
    
    await mes.edit("Promoting the user...")
    await TanjiroUb.promote_chat_member(
        chat_id,
        new_admin_id,
        privileges=ChatPrivileges(
            can_change_info=True,
            can_delete_messages=True,
            can_pin_messages=True,
            can_invite_users=True,
            can_manage_video_chats=True,
            can_restrict_members=True
        )
    )
    await mes.edit(f"Successfully promoted {reply.from_user.mention} to admin!")

@TanjiroUb.on_message(filters.command("demote", prefixes=".") & filters.me)
async def demote_user(_, message):
    mes = message   

    if not message.reply_to_message:
        return await mes.edit("Please reply to the user you want to demote.")

    reply = message.reply_to_message
    chat_id = message.chat.id
    new_admin_id = reply.from_user.id
    bot_stats = await TanjiroUb.get_chat_member(chat_id, "self")
        
    if not bot_stats.privileges or not bot_stats.privileges.can_promote_members:
        return await mes.edit("I don't have the necessary privileges to demote members.")

    await mes.edit("Demoting the user...")
    await TanjiroUb.promote_chat_member(
        chat_id,
        new_admin_id,
        privileges=ChatPrivileges(
            can_change_info=False,
            can_invite_users=False,
            can_delete_messages=False,
            can_restrict_members=False,
            can_pin_messages=False,
            can_promote_members=False,
            can_manage_chat=False,
            can_manage_video_chats=False    
        )
    )
    await mes.edit(f"Successfully demoted {reply.from_user.mention} 😢.")
     
