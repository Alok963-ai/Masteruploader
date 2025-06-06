
`MultipleFiles/master (1).py`
```py
from pyrogram import Client as bot, filters
from config import Config
import shutil
import os
from master import masterdl

@bot.on_message(filters.command("drm"))
async def account_login(bot, m):
    """
    Handler for /drm command.
    Processes a provided master TXT file containing links,
    collects parameters interactively, and launches downloads/uploads.
    """
    try:
        Credit = Config.CREDIT
        editable = await m.reply_text('__Send 🗂️Master TXT🗂️ file for download__')

        # Listen for the document file from the same user in chat
        input_msg = await bot.listen(chat_id=m.chat.id, filters=filters.document & filters.user(m.from_user.id))

        # Check if the message has a document
        if not input_msg.document:
            await editable.edit("❌ Please send a document file.")
            return

        path = f"./downloads/{m.chat.id}"
        temp_dir = "./temp"
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir, exist_ok=True)

        # Process the received document: extract links and filename
        links, file_name = await masterdl.process_text_file_or_input(input_msg)

        await editable.edit(f"🔗 Total links found: __{len(links)}__\n\nSend starting link number (default is __1__):")
        input0 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        raw_text = input0.text
        await input0.delete(True)

        await editable.edit("__Enter Batch Name or send '1' to use the text file's filename:__")
        input1 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        raw_text0 = input1.text
        await input1.delete(True)
        if raw_text0 == '1':
            b_name = file_name
        else:
            b_name = raw_text0

        await editable.edit("__Enter resolution (e.g., 360, 480, 720):__")
        input2 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        raw_text2 = input2.text
        await input2.delete(True)

        await editable.edit(f"__Enter your name or send '1' to use credit name `{Credit}`:__")
        input3 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        raw_text3 = input3.text
        await input3.delete(True)
        if raw_text3 == '1':
            MR = Credit
        else:
            MR = raw_text3

        # Hardcoded token - consider securing this better if in production
        token = (
            "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
            "eyJleHAiOjE3NDI2MzYxNTkuNTc4LCJkYXRhIjp7Il9pZCI6IjY1OWZjZWU5YmI4YjFkMDAxOGFmYTExZCIsInVzZXJuYW1lIjoiODUzOTkyNjE5MCIsImZpcnN0TmFtZSI6IlNoaXR0dSIsImxhc3ROYW1lIjoiU2luZ2giLCJvcmdhbml6YXRpb24iOnsiX2lkIjoiNWViMzkzZWU5NWZhYjc0NjhhNzlkMTg5Iiwid2Vic2l0ZSI6InBoeXNpY3N3YWxsYWguY29tIiwibmFtZSI6IlBoeXNpY3N3YWxsYWgifSwiZW1haWwiOiJzaGl0dHVrdW1hcjM3QGdtYWlsLmNvbSIsInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsInR5cGUiOiJVU0VSIn0sImlhdCI6MTc0MjAzMTM1OX0."
            "HhM0JtZEyI4Laed4oQCmGkLjP-_5SvqqS1w-o5ZUbdU"
        )

        await editable.edit("Send the __Thumbnail URL__ or send `no` to skip:")
        input6 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        thumb = input6.text.strip()
        await input6.delete(True)

        await editable.edit(
            "__Please provide channel ID to upload videos,__ or send `/d` to upload here in this chat.\n"
            "__Make sure to make me admin in the channel for uploading, otherwise I can't upload.__"
        )
        input7 = await bot.listen(chat_id=m.chat.id, filters=filters.text & filters.user(m.from_user.id))
        channel_text = input7.text.strip()
        if channel_text.lower() == "/d":
            channel_id = m.chat.id
        else:
            channel_id = channel_text
        await input7.delete(True)

        # Try sending a test message in the target channel to confirm permissions
        try:
            await bot.send_message(chat_id=channel_id, text=f'🎯 **Target Batch - {b_name}**')
        except Exception:
            await m.reply_text(f"⚠️ Please make me admin in the channel.\n\nBot Made By 🔰『{Credit}』🔰")
            channel_id = m.chat.id  # fallback to current chat

        await editable.delete()

        # Kick off download and upload process
        await masterdl.process_links(
            links,
            raw_text,
            raw_text2,
            token,
            b_name,
            MR,
            channel_id,
            bot,
            m,
            path,
            thumb,
            Credit,
        )
    except Exception as e:
        await m.reply_text(
            f"⚠️ Downloading Failed ⚠️\n\nReason: {e}\n\n╰────⌈✨❤️ 『{Credit}』 ❤️✨⌋────╯
